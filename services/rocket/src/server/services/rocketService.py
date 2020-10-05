from services.rocket.src.server.resources.rocketResource import RocketResource


class RocketService:
    rocketResource = RocketResource()

    def getAllRockets(self):
        return self.rocketResource.getAllRockets()

    def getRocketById(self, id):
        return self.rocketResource.getRocketById(id)
