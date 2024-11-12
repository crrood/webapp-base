import json
import logging
import os

from bson import ObjectId, json_util
from flask import Response, jsonify, make_response
from pymongo import MongoClient

DATABASE = "mongoDatabase"
ITEMS_PER_PAGE = 10


# connect to DB
def get_client() -> MongoClient:
    mongodb_username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
    mongodb_password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
    mongodb_connstring = f"mongodb://{mongodb_username}:{mongodb_password}@mongodb"
    client = MongoClient(mongodb_connstring)
    return client


def get_database() -> MongoClient:
    client = get_client()
    return client[DATABASE]


def get_collection(collection: str) -> MongoClient:
    client = get_database()
    return client[collection]


def query_collection(collection: str, page_number: int) -> Response:
    """Query n documents from a collection, offset by page_number

    Parameters:
    collection (string): Name of the db collection
    page_number (int): Offset to query from, 0-indexed

    Returns:
    (Response): Body is an array of JSON documents
    """
    client = get_collection(collection)

    offset = page_number * ITEMS_PER_PAGE
    results = client.find(limit=ITEMS_PER_PAGE, skip=offset)

    result_array = []
    for result in results:
        result_array.append(json.loads(json_util.dumps(result)))

    return make_response(jsonify(result_array), 200)


def query_document_by_id(collection: str, id: str) -> Response:
    """Query a document from the database using an _id value

    Parameters:
    collection (string): Name of the db collection
    id (string): ID of the document - must convert to an ObjectId

    Returns:
    (Response): JSON dump of document OR error string
    """
    client = get_collection(collection)
    try:
        object_id = convert_to_oid(id)
    except:
        response = f"Could not convert {id} to ObjectId"
        result_code = 422
        return make_response(response, result_code)

    data = client.find_one({"_id": object_id})
    logging.info(data)

    if data != None:
        response = json.loads(json_util.dumps(data))
        result_code = 200
    else:
        response = f"id {id} not found in {collection}"
        result_code = 404

    return make_response(response, result_code)


def upsert_document(collection: str, data: dict, query: dict = None) -> Response:
    """Upsert a document in the database

    Parameters:
    collection (string): Name of the db collection
    data (dict): JSON document to be upserted
    query (mongoQuery, optional): Query to find document to replace

    Returns:
    (Response): Status message
    """
    # mongo throws an error if incoming data attempts to update the immutable _id field
    logging.info(data)
    data.pop("_id", None)
    client = get_collection(collection)

    if query is not None:
        result = client.replace_one(query, data, upsert=True)
        logging.info(result.raw_result)
        if result.modified_count > 0:
            response = f"updated document"
        else:
            response = str(result.upserted_id)

        result_code = 200
    else:
        result = client.insert_one(data)
        response = str(result.inserted_id)
        result_code = 200

    return make_response(response, result_code)


def upsert_document_by_id(collection: str, data: dict, id: str) -> Response:
    """Upsert a document in the database

    Parameters:
    collection (string): Name of the db collection
    data (dict): JSON document to be upserted
    id (string): ID of the document - must convert to an ObjectId

    Returns:
    (Response): Status message
    """
    try:
        object_id = convert_to_oid(id)
    except:
        response = f"Could not convert {id} to ObjectId"
        result_code = 422
        return response, result_code

    return upsert_document(collection, data, {"_id": object_id})


def delete_document_by_id(collection: str, id: str) -> Response:
    """Delete a document from the database

    Parameters:
    collection (string): Name of the db collection
    id (string): ID of the document - must convert to an ObjectId

    Returns:
    (Response): Status message
    """
    client = get_collection(collection)
    try:
        object_id = convert_to_oid(id)
    except:
        response = f"Could not convert {id} to ObjectId"
        result_code = 422
        return make_response(response, result_code)

    result = client.delete_one({"_id": object_id})

    if result.deleted_count > 0:
        response = f"deleted document with id {id}"
        result_code = 200
    else:
        response = f"id {id} not found in {collection}"
        result_code = 404

    return make_response(response, result_code)


def reset() -> str:
    """Drop the DB and refill with test data from resources.json"""
    client = get_client()
    client.drop_database(DATABASE)

    with open("config/resources.json") as f:
        sample_data = json.load(f)

    client = get_database()
    for resource in sample_data:
        for i in range(len(sample_data[resource])):
            result = client[resource].insert_one(sample_data[resource][i])

    return f"db reset - test resource id = {result.inserted_id}"


def test_db():
    """Upserts a document, queries the collection, queries the document,
    updates the document, and deletes the document"""
    test_data = {"name": "test", "value": 42}
    response = upsert_document("test", test_data)
    if response.status_code != 200:
        return f"upsert failed: {response.data}"
    id = response.data.decode("utf-8")

    response = query_collection("test", 0)
    if response.status_code != 200:
        return f"query collection failed: {response.data}"
    if len(json.loads(response.data)) == 0:
        return "query collection failed: no results"
    if json.loads(response.data)[0]["value"] != 42:
        return f"query collection failed: wrong data\n{response.data}"

    response = query_document_by_id("test", id)
    if response.status_code != 200:
        return f"query document failed: {response.data}"
    if json.loads(response.data)["value"] != 42:
        return f"query document failed: wrong data\n{response.data}"

    response = upsert_document_by_id("test", {"name": "test", "value": 43}, id)
    if response.status_code != 200:
        return f"update failed: {response.data}"
    response = query_document_by_id("test", id)
    if response.status_code != 200:
        return f"query document after update failed: {response.data}"
    if json.loads(response.data)["value"] != 43:
        return f"query document after update failed: wrong data\n{response.data}"

    response = delete_document_by_id("test", id)
    if response.status_code != 200:
        return f"delete failed: {response.data}"
    response = query_document_by_id("test", id)
    if response.status_code != 404:
        return f"query document after delete failed: {response.data}"

    get_database().drop_collection("test")

    return "DB test passed"


# utility methods
def convert_to_oid(id):
    return ObjectId(id)
