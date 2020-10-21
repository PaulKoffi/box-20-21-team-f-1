from kafka import KafkaConsumer
from json import loads

# from server.services.rocketService import RocketService

consumer = KafkaConsumer(
    'Pollrequesttopic',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='rocketInventory-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    print('{} added to {}'.format(message, topic_retrieve))