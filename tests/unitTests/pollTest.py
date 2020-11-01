from kafka import KafkaConsumer
from kafka import KafkaProducer

from json import loads, dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


data = {'siteName': 'Paris',
            'rocketName': 'VEGA-6000'}
producer.send('Pollrequesttopic', value=data)

print('aaaaa')

data1 = {'siteName': 'Paris',
            'rocketName': 'Challenger-6000'}
producer.send('Pollrequesttopic', value=data1)

print('bbbb')

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollTest-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['launcherTopic'])

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    print(topic_retrieve)
    print(message)
    if message ['action'] == 'launch' : 
        print("it's works !!!!")
    if message ['siteName']  == 'Paris' : 
        print("it's works !!!!")
    if message ['rocketName'] == 'Challenger-6000' : 
        print("it's works !!!!")

    print("it's works !!!")
    # consumer.close()
    break