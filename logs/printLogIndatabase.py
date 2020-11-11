import pymongo
import json
from bson.json_util import dumps, loads

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

log = json.loads(dumps(db.logEvent.find()))

for l in log:
    print(l)
