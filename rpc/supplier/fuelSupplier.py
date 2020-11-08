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

DELIVERY_STATES_BASE_URL = "http://localhost:7000"
SUPPLIER_BASE_URL = "http://localhost:2650"
SATELLITE_BASE_URL = "http://localhost:3550"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

time.sleep(5)
consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='supplier',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe('supplierTopic')


for msg in consumer:
    message = msg.value
    if (msg.topic == 'supplierTopic' and message['action'] == 'launchSupplier'):
        supplierName = message['supplierName']
        satelliteName = message['satelliteName']
        currentPayload = requests.get("{}/payload/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, satelliteName))
        satellite=requests.get("{}/satellite/{}".format(SATELLITE_BASE_URL, satelliteName))
        supplier = requests.get("{}/payload/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, satelliteName))
        if currentPayload.json()["past"]==False:
            data = {'action': 'notLaunchedYet',
            'supplierName': supplierName,
            'satelliteName': satelliteName}
            producer.send('supplierTopic', value=data)
        else:
            requests.put("{}/supplier/setFuelSupplierNotAvailable/{}".format(SUPPLIER_BASE_URL, supplierName))

            requests.put("{}/supplier/setSatelliteToSupply/{}/{}".format(SUPPLIER_BASE_URL, supplierName,satelliteName ))
            time.sleep(5)

            requests.put("{}/satellite/addFuel/{}/{}".format(SATELLITE_BASE_URL, satelliteName, satellite.json()["fuel"] ))
            requests.put("{}/supplier/setSupplierFuel/{}/{}".format(SUPPLIER_BASE_URL, supplierName,0 ))
            data = {'action': 'supplied',
            'supplierName': supplierName,
            'satelliteName': satelliteName}
            producer.send('supplierTopic', value=data)
            time.sleep(5)

            data = {'action': 'back',
            'supplierName': supplierName,
            'satelliteName': satelliteName}
            producer.send('supplierTopic', value=data)
            requests.put("{}/supplier/setFuelSupplierAvailable/{}".format(SUPPLIER_BASE_URL, supplierName))