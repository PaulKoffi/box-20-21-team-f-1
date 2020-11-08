from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads
from time import sleep
from json import dumps
import queue

sleep(10)


def launch(rocket, site):
    print("Launching " + rocket + " from " + site)
    data = {'action': "launch",
            'siteName': site,
            'rocketName': rocket}
    producer.send('launcherTopic', value=data)


launchElon = True
launchTory = True
siteName = ""
rocketName = ""
queueresponse = queue.Queue()

# 'localhost:9092' is where producer is running
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystem-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic', 'polltoryresponsetopic'])

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    if (topic_retrieve == 'pollelonresponsetopic'):
        if (message['response']['status'] != "it's risky"):
            data = {'elonResponse': 'GO', 'request': message['request']}
            rocketName = message['request']['rocketName']
            siteName = message['request']['siteName']
            if (queueresponse.empty()):
                queueresponse.put(data)
            else:
                responseTory = queueresponse.get()
                if (responseTory['toryResponse'] == 'GO'):
                    print("The rocket can be launched")
                    launch(rocketName, siteName)
        else:
            print("the rocket cannot be launched")

    else:
        responseTory = message['response']
        # print(responseTory)
        if(responseTory['wind'] < 10):
            # print(message['request'])
            data = {'toryResponse' : 'GO', 'request': message['request']}
            rocketName = message['request']['rocketName']
            siteName = message['request']['siteName']
            if (queueresponse.empty()):
                queueresponse.put(data)
            else:
                elonResponse = queueresponse.get()
                print(elonResponse)
                
                if(elonResponse['elonResponse'] == 'GO'):
                    print("The rocket can be launched")
                    launch(rocketName, siteName)

        else:
            print("the rocket cannot be launched")
