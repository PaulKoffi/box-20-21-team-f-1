from flask import Flask

from server.controllers.satelliteController import satelliteControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(satelliteControllerBlueprint)
    return app
