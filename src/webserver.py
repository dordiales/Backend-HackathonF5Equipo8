from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def wellcome():
        return "<h1>Local Experience API</h1>\n<h3>Bienvenido, por favor lea el README.md antes de utilizar esta api</h3>"

    @app.route("/api/experiences", methods=["GET"])
    def get_all_experiences():
        all_experiences = repositories["experiences"].get_all()
        return object_to_json(all_experiences)

    @app.route("/api/guides", methods=["GET"])
    def get_all_guides():
        all_experiences = repositories["guides"].get_all()
        return object_to_json(all_experiences)

    return app
