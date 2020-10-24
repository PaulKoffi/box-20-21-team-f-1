from flask import Blueprint, request
from server.services.deliveryService import DeliveryService

deliveryService = DeliveryService()
deliveryControllerBlueprint = Blueprint('deliveryController', __name__ )

@deliveryControllerBlueprint.route('/payload/payloadByRocketName/<string:rocketName>', methods=['GET'])
def getPayloadByRocketName(rocketName):
    return deliveryService.getPayloadByRocketName(rocketName)

@deliveryControllerBlueprint.route('/payload/payloadBySatelliteName/<string:satelliteName>', methods=['GET'])
def getPayloadBySatelliteName(satelliteName):
    return deliveryService.getPayloadBySatelliteName(satelliteName)

@deliveryControllerBlueprint.route('/payload', methods=['POST'])
def addPayload():
    body = request.get_json()
    # print(body["customerName"])
    return deliveryService.addPayload(body["customerName"], body["customerMail"], int(body["finalPosition"]), body["x"], body["y"], body["satellite"])


@deliveryControllerBlueprint.route('/payload/setPastMissionValue', methods=['POST'])
def setPastMissionValue():
    body = request.get_json()
    # print(body["customerName"])
    return deliveryService.setPastMissionValue(body["rocketName"])

@deliveryControllerBlueprint.route('/payload/setStatus', methods=['POST'])
def setStatus():
    body = request.get_json()
    # print(body["customerName"])
    return deliveryService.setStatus(body["rocketName"])