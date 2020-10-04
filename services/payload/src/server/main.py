from flask import Flask

from server.controllers.payloadController import payloadControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(payloadControllerBlueprint)
    return app
