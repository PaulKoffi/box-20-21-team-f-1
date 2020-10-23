from kafka import KafkaConsumer
from json import loads
import queue

queueresponse = queue.Queue()

consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='pollsystem-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic','polltoryresponsetopic'])

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    if(topic_retrieve == 'pollelonresponsetopic'):
        if(message['response']['status'] != "it's risky"):
            data = {'elonResponse' : 'GO', 'request': message['response']['request']}
            if(queueresponse.empty()):
                queueresponse.put(data)
            else:
                responseTory = queueresponse.get()
                if(responseTory['toryResponse'] == 'GO'):
                    print("The rocket can be launched")
        else:
            print("the rocket cannot be launched")

    else:
        responseTory = loads(message['response'])
        print(responseTory)
        if(responseTory[0]['wind'] < 10):
            print(message['request'])
            data = {'toryResponse' : 'GO', 'request': message['request']}
            if(queueresponse.empty()):
                queueresponse.put(data)
            else:
                elonResponse = queueresponse.get()
                if(responseTory['elonRespnse'] == 'GO'):
                    print("The rocket can be launched")
        else:
            print("the rocket cannot be launched")

    # print(message)