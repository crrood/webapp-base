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
        return response, result_code

    data = client.find_one({"_id": object_id})

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
            response = f"inserted document with id {result.upserted_id}"

        result_code = 200
    else:
        result = client.insert_one(data)
        response = f"inserted with id {result.inserted_id}"
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


def reset() -> str:
    """Drop the DB and refill with test data from utils/testData/entity.json"""
    client = get_client()
    client.drop_database(DATABASE)

    # populate testing data
    with open("resources/resources.json") as f:
        sample_data = json.load(f)

    client = get_database()
    for resource in sample_data:
        result = client[resource].insert_one(sample_data[resource])

    return f"db reset - test resource id = {result.inserted_id}"


# utility methods
def convert_to_oid(id):
    return ObjectId(id)
