from flask import Flask

from server.controllers.supplierController import supplierControllerBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(supplierControllerBlueprint)
    return app
