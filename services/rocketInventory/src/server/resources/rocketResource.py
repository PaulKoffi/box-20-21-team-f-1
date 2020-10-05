from flask import jsonify

rockets = {
    "nice": {"status": "ready to go"},
    "cotonou": {"status": "it's risky"},
    "himalaya": {"status": "aborted"},
}


class RocketResource():
    def getAllRockets(self):
        return jsonify(rockets)

    def getRocketById(self, id):
        return jsonify(rockets[id])
