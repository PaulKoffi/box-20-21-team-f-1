from server.resources.rocketResource import RocketResource


class RocketService:
    rocketResource = RocketResource()

    def getAllRockets(self):
        return self.rocketResource.getAllRockets()

    def getRocketById(self, id):
        return self.rocketResource.getRocketById(id)

    def setRocketStatus(self, id):
        return self.rocketResource.setRocketStatus(id)

    def setRocketSpeed(self, id, speed):
        return self.rocketResource.setRocketSpeed(id, speed)
    
