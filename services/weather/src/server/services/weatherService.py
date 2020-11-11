from server.resources.weatherResource import WeatherResource


class WeatherService:
    weatherResource = WeatherResource()

    def getAllSites(self):
        return self.weatherResource.getAllSites()

    def getSiteByName(self, siteName):
        return self.weatherResource.getSiteByName(siteName)

    # def setRocketStatus(self, id):
    #     return self.rocketResource.setRocketStatus(id)

    # def setRocketSpeed(self, id, speed):
    #     return self.rocketResource.setRocketSpeed(id, speed)
    
