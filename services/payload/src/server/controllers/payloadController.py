from flask import Blueprint
from server.services.payloadService import PayloadService

payloadService = PayloadService()
payloadControllerBlueprint = Blueprint('payloadController', __name__, )


@payloadControllerBlueprint.route('/payloads')
def geteAllPayloads():
    return payloadService.getAllPayloads()


@payloadControllerBlueprint.route('/payload/<string:id>')
def getPayloadById(id):
    return payloadService.getPayloadById(id)
