from flask import Flask

from server.controllers.rocketStatesController import rocketStatesControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(rocketStatesControllerBlueprint)
    return app
