from flask import Blueprint
from server.services.rocketStatesService import RocketStatesService

rocketStatesService = RocketStatesService()
rocketStatesControllerBlueprint = Blueprint('rocketStatesController', __name__)


@rocketStatesControllerBlueprint.route('/rocketsStates/secondStep/<string:siteName>/<string:rocketName>',
                                       methods=['GET'])
def getSecondStepByNameAndSite(siteName, rocketName):
    return rocketStatesService.getSecondStepByNameAndSite(siteName, rocketName)


@rocketStatesControllerBlueprint.route('/rocketsStates/destruction/<string:siteName>/<string:rocketName>',
                                       methods=['GET'])
def getDestructionByNameAndSite(siteName, rocketName):
    return rocketStatesService.getDestructionByNameAndSite(siteName, rocketName)


@rocketStatesControllerBlueprint.route('/rocketsStates/launching/<string:siteName>/<string:rocketName>',
                                       methods=['GET'])
def getLaunchingByNameAndSite(siteName, rocketName):
    return rocketStatesService.getLaunchingByNameAndSite(siteName, rocketName)


@rocketStatesControllerBlueprint.route('/rocketsStates/secondStep/<string:siteName>/<string:rocketName>/<int:state>',
                                       methods=['PUT'])
def putSecondStepByNameAndSite(siteName, rocketName, state):
    return rocketStatesService.putSecondStepByNameAndSite(siteName, rocketName, state)


@rocketStatesControllerBlueprint.route('/rocketsStates/destruction/<string:siteName>/<string:rocketName>/<int:state>',
                                       methods=['PUT'])
def putDestructionByNameAndSite(siteName, rocketName, state):
    return rocketStatesService.putDestructionByNameAndSite(siteName, rocketName, state)


@rocketStatesControllerBlueprint.route('/rocketsStates/launching/<string:siteName>/<string:rocketName>/<int:state>',
                                       methods=['PUT'])
def putLaunchingByNameAndSite(siteName, rocketName, state):
    return rocketStatesService.putLaunchingByNameAndSite(siteName, rocketName, state)
