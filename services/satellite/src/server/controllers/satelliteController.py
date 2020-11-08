from flask import Blueprint
from server.services.satelliteService import SatelliteService

satelliteService = SatelliteService()
satelliteControllerBlueprint = Blueprint('satelliteController', __name__, )


@satelliteControllerBlueprint.route('/satellites')
def getAllSatellites():
    return satelliteService.getAllSatellites()


@satelliteControllerBlueprint.route('/satellite/<string:id>')
def getsatelliteById(id):
    return satelliteService.getSatelliteById(id)

@satelliteControllerBlueprint.route('/satellite/addFuel/<string:id>/<int:fuel>', methods=['PUT'])
def setSatelliteFuel(id, fuel):
    return satelliteService.setSatelliteFuel(id,fuel)
