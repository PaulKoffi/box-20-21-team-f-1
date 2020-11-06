from kafka import KafkaConsumer
from json import loads, dumps
import queue
import requests
import pymongo
from kafka import KafkaProducer

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
        print(message['rocketName'] + "FIRST STAGE || " + " at position " + message['state'])
    elif message['action'] == "running" and topic_retrieve == "rocketSSTopic":
        print(message['rocketName'] + "SECOND STAGE || " + " at position " + message['state'])

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
