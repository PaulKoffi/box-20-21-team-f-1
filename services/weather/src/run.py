from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads, dumps
from time import sleep

from server.services.weatherService import WeatherService

weatherService = WeatherService()

sleep(5)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    'Pollrequesttopic',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='weather-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    print(message)
    print(message['siteName'])
    weather_request = {'response': weatherService.getSiteByName(message['siteName']), 'request': message}
    print(weather_request)
    producer.send('polltoryresponsetopic',value=weather_request)