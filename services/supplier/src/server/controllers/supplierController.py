from flask import Blueprint
from server.services.supplierService import FuelSupplierService

supplierService = FuelSupplierService()
supplierControllerBlueprint = Blueprint('supplierController', __name__, )


@supplierControllerBlueprint.route('/suppliers')
def getAllSuppliers():
    return supplierService.getAllSuppliers()


@supplierControllerBlueprint.route('/supplier/<string:id>')
def getFuelSupplierByName(id):
    return supplierService.getFuelSupplierByName(id)

@supplierControllerBlueprint.route('/supplier/setFuelSupplierNotAvailable/<string:id>', methods=['PUT'])
def setFuelSupplierNotAvailable(id):
    return supplierService.setFuelSupplierNotAvailable(id)

@supplierControllerBlueprint.route('/supplier/setFuelSupplierAvailable/<string:id>', methods=['PUT'])
def setFuelSupplierAvailable(id):
    return supplierService.setFuelSupplierAvailable(id)

@supplierControllerBlueprint.route('/supplier/setSupplierFuel/<string:id>/<int:fuel>', methods=['PUT'])
def setSupplierFuel(id, fuel):
    return supplierService.setSupplierFuel(id,fuel)


@supplierControllerBlueprint.route('/supplier/setSatelliteToSupply/<string:id>/<string:satellite>', methods=['PUT'])
def setSatelliteToSupply(id, satellite):
    return supplierService.setSatelliteToSupply(id,satellite)