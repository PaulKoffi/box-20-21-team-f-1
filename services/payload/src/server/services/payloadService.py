from server.resources.payloadResource import PayloadResource


class PayloadService:
    payloadResource = PayloadResource()

    def getAllPayloads(self):
        return self.payloadResource.getAllPayloads()

    def getPayloadById(self, id):
        return self.payloadResource.getPayloadById(id)