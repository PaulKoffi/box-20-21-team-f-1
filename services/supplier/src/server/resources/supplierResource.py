from flask import jsonify
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


class FuelSupplierResource():
    def getAllSuppliers(self):
        response = json.loads(dumps(db.fuelSuplier.find()))
        # print(response)
        return jsonify(response)

    def getFuelSupplierByName(self, id):
        return jsonify(json.loads(dumps(db.fuelSuplier.find_one({"supplierName": id}))))

    def setFuelSupplierAvailable(self, id):
        myquery = {"supplierName": id}
        newvalues = {"$set": {"available":True}}
        db.fuelSuplier.update_one(myquery, newvalues)
        return jsonify(json.loads(dumps(db.fuelSuplier.find_one({"supplierName": id}))))

    def setFuelSupplierNotAvailable(self, id):
        myquery = {"supplierName": id}
        newvalues = {"$set": {"available":False}}
        db.fuelSuplier.update_one(myquery, newvalues)
        return jsonify(json.loads(dumps(db.fuelSuplier.find_one({"supplierName": id}))))

    def setSupplierFuel(self, id, fuel):
        myquery = {"supplierName": id}
        actuelFuel = json.loads(dumps(db.fuelSuplier.find_one(myquery)))["fuel"]
        newvalues = {"$set": {"fuel": fuel}}
        db.fuelSuplier.update_one(myquery, newvalues)
        return str(actuelFuel)

    def setSatelliteToSupply(self, id, satellite):
        myquery = {"supplierName": id}
        actuelSatellite = json.loads(dumps(db.fuelSuplier.find_one(myquery)))["satellite"]
        newvalues = {"$set": {"satellite": satellite}}
        db.fuelSuplier.update_one(myquery, newvalues)
        return str(actuelSatellite)