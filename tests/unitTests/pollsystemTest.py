from kafka import KafkaConsumer
from json import loads, dumps
import queue

queueresponse = queue.Queue()

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollSystemTest-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic', 'polltoryresponsetopic'])

elonResponses = []
toryResponses = []

queueElonResponses = queue.Queue()
queueToryResponses = queue.Queue()

def canbelanched(elonResponse,toryResponse):
    if elonResponse == 'GO' and toryResponse == 'GO':
        return True
    else:
        return False

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    if (topic_retrieve == 'pollelonresponsetopic'):
        # print(message)
        if (message['response']['rocketName'] == "VEGA-6000"):
            assert message['response']['status'] == "ready to go"
            data = {'elonResponse': 'GO', 'request': message['request']}
            elonResponses.append(data)
            if (queueToryResponses.empty()):
                queueElonResponses.put(data)
            else:
                responseTory = queueToryResponses.get()
                assert responseTory['toryResponse'] == 'NOGO'
                assert canbelanched(data['elonResponse'],responseTory['toryResponse']) == False
                print (canbelanched(data['elonResponse'],responseTory['toryResponse']))
        else:
            assert message['response']['status'] == "ready to go"
            data = {'elonResponse': 'GO', 'request': message['request']}
            elonResponses.append(data)
            # print(elonResponses)
            # if (len(toryResponses) > 1):
            #     responseTory = toryResponses[1]
            if (queueToryResponses.empty()):
                queueElonResponses.put(data)
            else:
                responseTory = queueToryResponses.get()
                assert responseTory['toryResponse'] == 'GO'
                assert canbelanched(data['elonResponse'],responseTory['toryResponse']) == True
                print (canbelanched(data['elonResponse'],responseTory['toryResponse']))

    else:
        responseTory = message['response']
        if(responseTory['name'] == "Toulouse"):
            assert responseTory['wind'] > 10
            data = {'toryResponse' : 'NOGO', 'request': message['request']}
            toryResponses.append(data)
            # if (len(elonResponses) > 0):
            #     responseElon = elonResponses[0]
            if (queueElonResponses.empty()):
                queueToryResponses.put(data)
            else:
                responseElon = queueElonResponses.get()
                assert responseElon['elonResponse'] == 'GO'
                assert canbelanched(data['toryResponse'],responseElon['elonResponse']) == False
                print (canbelanched(data['toryResponse'],responseElon['elonResponse']))

        else:
            assert responseTory['wind'] < 10
            data = {'toryResponse' : 'GO', 'request': message['request']}
            toryResponses.append(data)
            # print(toryResponses)
            # if (len(elonResponses) > 1):
            #     responseElon = elonResponses[1]
            if (queueElonResponses.empty()):
                queueToryResponses.put(data)
            else:
                responseElon = queueElonResponses.get()
                assert responseElon['elonResponse'] == 'GO'
                assert canbelanched(data['toryResponse'],responseElon['elonResponse']) == True
                print (canbelanched(data['toryResponse'],responseElon['elonResponse']))
