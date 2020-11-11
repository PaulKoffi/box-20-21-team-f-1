from flask import Flask

from server.controllers.eventRegistrationController import eventRegistrationControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(eventRegistrationControllerBlueprint)
    return app
