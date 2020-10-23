from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads, dumps

from server.services.rocketService import RocketService

rocketService = RocketService()

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

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
    print(message)
    print (message['rocketName'])
    rocket_request = {'response': rocketService.getRocketById(message['rocketName']), 'request': message}
    print(rocket_request)
    producer.send('pollelonresponsetopic',value=rocket_request)