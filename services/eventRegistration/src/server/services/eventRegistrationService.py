from server.resources.eventRegistrationResource import EventRegistrationResource


class EventRegistrationService:
    eventRegistrationResource = EventRegistrationResource()

    def getLogBySatelliteName(self, satelliteName):
        return self.eventRegistrationResource.getLogBySatelliteName(satelliteName)

    def addLog(self, rocketName, siteName, satelliteName, message):
        return self.eventRegistrationResource.addLog(rocketName, siteName, satelliteName, message)
