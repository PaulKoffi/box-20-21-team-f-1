from flask import jsonify

payloads = {
    "satelite1": {
        "position": {"x": 1.0, "y":1.0},
        "vitesse": 30.0,
        "customer": {"name":"Paul-Marie"},
        "rocketName": "Arianne-240",
    },
    "satelite2": {
        "position": {"x": 1.0, "y":1.0},
        "vitesse": 30.0,
        "customer": {"name":"Paul-Marie"},
        "rocketName": "Arianne-2800",
    },
    "satelite3": {
        "position": {"x": 1.0, "y":1.0},
        "vitesse": 30.0,
        "customer": {"name":"Paul-Marie"},
        "rocketName": "Arianne-2460",
    },
}

class PayloadResource():
    def getAllPayloads(self):
        return jsonify(payloads)

    def getPayloadtById(self, id):
        return jsonify(payloads[id])