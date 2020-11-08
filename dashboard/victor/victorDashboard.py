from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer
from time import sleep

sleep(10)

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='victor-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(['supplierTopic'])

for msg in consumer:
    message = msg.value

    if message['action'] == "launchSupplier":
        print(message['supplierName'] + " is asked to supply the satellite " + message['satelliteName'])

    if message['action'] == "notLaunchedYet":
        print("Satellite "+ message['satelliteName'] + " is not launched yet", end='')

    if message['action'] == "supplied":
        print(message['supplierName'] + " have supplied the satellite " + message['satelliteName'])

    if message['action'] == "back":
        print(message['supplierName'] + " is back on earth " )