from flask import Blueprint, request
from server.services.eventRegistrationService import EventRegistrationService

eventRegistrationService = EventRegistrationService()
eventRegistrationControllerBlueprint = Blueprint('eventRegistrationController', __name__ )

@eventRegistrationControllerBlueprint.route('/eventRegistration/<string:satelliteName>', methods=['GET'])
def getLogBySatelliteName(satelliteName):
    return eventRegistrationService.getLogBySatelliteName(satelliteName)

@eventRegistrationControllerBlueprint.route('/eventRegistration', methods=['POST'])
def addLog():
    body = request.get_json()
    # print(body["customerName"])
    return eventRegistrationService.addLog(body["rocketName"], body["siteName"], body["message"], body["satelliteName"])
