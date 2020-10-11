import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

myquery = {"rocketName": "VEGA-4000"}
newvalues = {"$set": {"launch": False, "secondStep": False}}
db.rocketActions.update_one(myquery, newvalues)
db.payloads.delete_many({"satellite": "CORSAIRE"})
db.rocketinventories.delete_many({"rocketName": "VEGA-4000"})

myquery = {"rocketName": "SOUL-9000"}
newvalues = {"$set": {"launch": False, "secondStep": False}}
db.rocketActions.update_one(myquery, newvalues)
db.payloads.delete_many({"satellite": "PERSEUS"})
db.rocketinventories.delete_many({"rocketName": "SOUL-9000"})
