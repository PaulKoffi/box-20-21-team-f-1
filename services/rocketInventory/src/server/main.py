from flask import Flask

from server.controllers.rocketController import rocketControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(rocketControllerBlueprint)
    return app
