from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads
from time import sleep
from json import dumps
import queue

queueresponse = queue.Queue()

sleep(10)

# 'localhost:9092' is where producer is running
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


def launch(rocket, site):
    print("Launching " + rocket + " from " + site)
    data = {'action': "launch",
            'siteName': site,
            'rocketName': rocket}
    m = {
        'value': "__________________________________________________________________________________________________________________________________"}
    producer.send('eventCollectortopic', value=m)
    m = {'value': "\n"}
    producer.send('eventCollectortopic', value=m)
    producer.send('launcherTopic', value=data)
    global queueresponse
    queueresponse.queue.clear()


launchElon = True
launchTory = True
siteName = ""
rocketName = ""

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
                print("ici t")
                print(responseTory)
                if (responseTory['toryResponse'] == 'GO'):
                    print("The rocket can be launched")
                    launch(rocketName, siteName)

                queueresponse.queue.clear()

        else:
            print("the rocket cannot be launched")
            queueresponse.queue.clear()

    else:
        responseTory = message['response']
        # print(responseTory)
        if (responseTory['wind'] < 10):
            # print(message['request'])
            data = {'toryResponse': 'GO', 'request': message['request']}
            rocketName = message['request']['rocketName']
            siteName = message['request']['siteName']
            if (queueresponse.empty()):
                queueresponse.put(data)
            else:
                elonResponse = queueresponse.get()
                print(elonResponse)

                if (elonResponse['elonResponse'] == 'GO'):
                    print("The rocket can be launched")
                    launch(rocketName, siteName)
                queueresponse.queue.clear()


        else:
            print("the rocket cannot be launched")
            queueresponse.queue.clear()
