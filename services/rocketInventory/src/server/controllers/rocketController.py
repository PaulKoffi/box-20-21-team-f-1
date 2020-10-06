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
