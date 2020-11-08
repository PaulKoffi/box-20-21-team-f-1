from server.resources.satelliteResource import SatelliteResource


class SatelliteService:
    satelliteResource = SatelliteResource()

    def getAllSatellites(self):
        return self.satelliteResource.getAllSatellites()

    def getSatelliteById(self, id):
        return self.satelliteResource.getSatelliteById(id)

    def setSatelliteFuel(self, id, fuelToAdd):
        return self.satelliteResource.setSatelliteFuel(id, fuelToAdd)

