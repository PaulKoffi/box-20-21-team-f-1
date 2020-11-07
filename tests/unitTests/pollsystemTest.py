from kafka import KafkaConsumer
from json import loads, dumps
import queue

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollSystemTest-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic', 'polltoryresponsetopic'])

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
        if (message['response']['rocketName'] == "VEGA-6000"):
            assert message['response']['status'] == "ready to go"
            data = {'elonResponse': 'GO', 'request': message['request']}
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
            if (queueToryResponses.empty()):
                queueElonResponses.put(data)
            else:
                responseTory = queueToryResponses.get()
                assert responseTory['toryResponse'] == 'GO'
                assert canbelanched(data['elonResponse'],responseTory['toryResponse']) == True

    else:
        responseTory = message['response']
        if(responseTory['name'] == "Toulouse"):
            assert responseTory['wind'] > 10
            data = {'toryResponse' : 'NOGO', 'request': message['request']}
            if (queueElonResponses.empty()):
                queueToryResponses.put(data)
            else:
                responseElon = queueElonResponses.get()
                assert responseElon['elonResponse'] == 'GO'
                assert canbelanched(data['toryResponse'],responseElon['elonResponse']) == False

        else:
            assert responseTory['wind'] < 10
            data = {'toryResponse' : 'GO', 'request': message['request']}
            if (queueElonResponses.empty()):
                queueToryResponses.put(data)
            else:
                responseElon = queueElonResponses.get()
                assert responseElon['elonResponse'] == 'GO'
                assert canbelanched(data['toryResponse'],responseElon['elonResponse']) == True
