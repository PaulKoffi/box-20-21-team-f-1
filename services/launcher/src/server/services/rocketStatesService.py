from server.resources.rocketStatesResource import RocketStatesResource


class RocketStatesService:
    rocketStatesResource = RocketStatesResource()

    
    def getSecondStepByNameAndSite(self,siteName,rocketName):
        return self.rocketStatesResource.getSecondStepByNameAndSite(siteName,rocketName)

    def getDestructionByNameAndSite(self,siteName,rocketName):
        return self.rocketStatesResource.getDestructionByNameAndSite(siteName,rocketName)

    def getLaunchingByNameAndSite(self,siteName,rocketName):
        return self.rocketStatesResource.getLaunchingByNameAndSite(siteName,rocketName)

    
    def putSecondStepByNameAndSite(self,siteName,rocketName,newState):
        return self.rocketStatesResource.putSecondStepByNameAndSite(siteName,rocketName,newState)

    def putDestructionByNameAndSite(self,siteName,rocketName,newState):
        return self.rocketStatesResource.putDestructionByNameAndSite(siteName,rocketName,newState)

    def putLaunchingByNameAndSite(self,siteName,rocketName,newState):
        return self.rocketStatesResource.putLaunchingByNameAndSite(siteName,rocketName,newState)
        
