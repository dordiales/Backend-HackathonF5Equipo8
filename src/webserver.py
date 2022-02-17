from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/examples", methods=["GET"])
    def get_all_examples():
        all_examples = repositories["examples"].get_all()
        return object_to_json(all_examples)

    @app.route("/api/experiences", methods=["GET"])
    def get_all_experiences():
        all_experiences = repositories["experiences"].get_all()
        return object_to_json(all_experiences)

    @app.route("/api/guides", methods=["GET"])
    def get_all_guides():
        all_experiences = repositories["guides"].get_all()
        return object_to_json(all_experiences)

    return app
