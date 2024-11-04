import logging

import utils.db as db
from flask import request
from flask_restful import Resource


class ResourceBase(Resource):
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def get(self, resource_id):
        return db.query_document_by_id(self.resource_name, resource_id)

    def put(self, resource_id):
        data = request.get_json()
        return db.upsert_document(self.resource_name, data, resource_id)


class ResourceBaseList(Resource):
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def get(self):
        page_number = request.args.get("page", default=0, type=int)
        return db.query_collection(self.resource_name, page_number)
