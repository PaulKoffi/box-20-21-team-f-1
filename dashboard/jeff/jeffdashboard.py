from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer
from time import sleep

sleep(5)

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='jeff-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(['rocketTopic', 'rocketSTopic'])

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic

    if message['action'] == "running" and topic_retrieve == "rocketTopic":
        print(message['rocketName'] + " FIRST STAGE || " + " at position " + message['state'])
    elif message['action'] == "destroy" and topic_retrieve == "rocketTopic":
        print(message['msg'])
    elif message['action'] == "running" and topic_retrieve == "rocketSTopic":
        print(message['rocketName'] + " SECOND STAGE || " + " at position " + message['state'])
