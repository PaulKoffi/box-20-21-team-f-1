from flask import Flask

from server.controllers.deliveryController import deliveryControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(deliveryControllerBlueprint)
    return app
