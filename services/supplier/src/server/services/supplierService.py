from server.resources.supplierResource import FuelSupplierResource


class FuelSupplierService:
    fuelSupplierResource = FuelSupplierResource()

    def getAllSuppliers(self):
        return self.fuelSupplierResource.getAllSuppliers()

    def getFuelSupplierByName(self,id):
        return self.fuelSupplierResource.getFuelSupplierByName(id)

    def setFuelSupplierAvailable(self, id):
        return self.fuelSupplierResource.setFuelSupplierAvailable( id)

    def setFuelSupplierNotAvailable(self, id):
        return self.fuelSupplierResource.setFuelSupplierNotAvailable( id)

    def setSupplierFuel(self, id, fuel):
        return self.fuelSupplierResource.setSupplierFuel(id, fuel)

    def setSatelliteToSupply(self, id, satellite):
        return self.fuelSupplierResource.setSupplierFuel(id, satellite)