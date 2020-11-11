from server.resources.deliveryResource import DeliveryResource


class DeliveryService:
    deliveryResource = DeliveryResource()


    def getPayloadByRocketName(self, rocketName):
        return self.deliveryResource.getPayloadByRocketName(rocketName)

    def getPayloadBySatelliteName(self, satelliteName):
        return self.deliveryResource.getPayloadBySatelliteName(satelliteName)

    def setPastMissionValue(self, rocketName):
        return self.deliveryResource.setPastMissionValue(rocketName)

    def setStatus(self, rocketName,satelitte):
        return self.deliveryResource.setStatus(rocketName,satelitte)

    def addPayload(self, customerName, customerMail, finalPosition, x, y, satellite):
        return self.deliveryResource.addPayload(customerName, customerMail, finalPosition, x, y, satellite)
