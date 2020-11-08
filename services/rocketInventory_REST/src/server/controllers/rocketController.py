from flask import Blueprint
from server.services.rocketService import RocketService

rocketService = RocketService()
rocketControllerBlueprint = Blueprint('rocketController', __name__, )


@rocketControllerBlueprint.route('/rockets')
def getAllRockets():
    return rocketService.getAllRockets()


@rocketControllerBlueprint.route('/rocket/<string:id>')
def getRocketById(id):
    return rocketService.getRocketById(id)

@rocketControllerBlueprint.route('/rocketN/<string:id>')
def getRocketByN(id):
    return rocketService.getRocketByN(id)


@rocketControllerBlueprint.route('/rocket/setStatus/<string:id>', methods=['POST'])
def setRocketStatus(id):
    return rocketService.setRocketStatus(id)


@rocketControllerBlueprint.route('/rocket/setRocketSpeed/<string:id>/<int:speed>', methods=['PUT'])
def setRocketSpeed(id, speed):
    return rocketService.setRocketSpeed(id,speed)