from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'eventCollectortopic',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='mary-dashboard',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for msg in consumer:
    message = msg.value
    # topic_retrieve = msg.topic
    print(' ========> {}'.format(message["value"]))