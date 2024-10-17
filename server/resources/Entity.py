import logging

import utils.db as db
from flask import request
from flask_restful import Resource


class Entity(Resource):
    def get(self, entity_id):
        return db.query_document_by_id("entities", entity_id)

    def put(self, entity_id):
        data = request.get_json()
        return db.upsert_document("entities", data, entity_id)


class EntityList(Resource):
    def get(self):
        args = request.args
        page_number = args.get("page", default=0, type=int)

        return db.query_collection("entities", page_number)
