import logging
import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.Entity import Entity, EntityList

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
api = Api(app)

# TODO restrict resources to front-end container, once it exists
CORS(app)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


# landing page
@app.route("/", methods=["GET"])
def landing_page():
    return "Server is up and running!"


api.add_resource(EntityList, "/entities")
api.add_resource(Entity, "/entities/<string:entity_id>")


# nuke all DB entries and replace with test data
@app.route("/resetDB")
def reset_db():
    logging.warn("resetting DB")
    return db.reset()


if __name__ == "__main__":
    app.run(debug=True)
