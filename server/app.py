import logging
import os

import utils.db as db
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# TODO: import resources dynamically from resources folder using importlib
from resources.ResourceFactory import ResourceFactory, ResourceListFactory

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
api = Api(app)

# TODO: restrict resources to front-end container, once it exists
CORS(app)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# add REST resources
api.add_resource(ResourceListFactory("entities"), "/entities")
api.add_resource(ResourceFactory("entities"), "/entities/<string:resource_id>")

# landing page
@app.route("/", methods=["GET"])
def landing_page():
    return "Server is up and running!"


# nuke all DB entries and replace with test data
@app.route("/resetDB")
def reset_db():
    logging.warn("resetting DB")
    return db.reset()


if __name__ == "__main__":
    app.run(debug=True)
