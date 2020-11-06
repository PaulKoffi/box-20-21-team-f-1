from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer
from kafka import KafkaProducer
import constants

destroy = False
stop = False

rocket = SimpleXMLRPCServer(('localhost', 8888), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumerDestruction = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='f-destruction-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumerDestruction.subscribe(["launcherTopic"])

for msg in consumerDestruction:
    print("OK")
    constants.my_variable.append("a list with")
    message = msg.value
    if message['action'] == "destroy":
        print("__________________ DESTRUCTION________________________")
        destroy = True
