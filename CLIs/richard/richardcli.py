from xmlrpc.client import ServerProxy
import requests
from kafka import KafkaProducer
from bson.json_util import dumps, loads

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

ROCKETS_STATES_BASE_URL = "http://localhost:5000"
s = ServerProxy('http://localhost:9000')

if __name__ == "__main__":
    while True:
        command = input().split(' ')
        if (command[0] == "quit"):
            print("Bye")
            break
        if(command[0] == "startpoll"):
            response = s.getResponsesPoll(command[1],command[2])
            print(response)
        if(command[0] == "decide"):
            print("The rocket {} at {} : {}".format(command[3],command[2],command[1]))
        if(command[0] == "destroy"):
            print(command[1] + "\n" + command[2])
            # data = {'action' : "destroy",
            #     'siteName' : command[1],
            #         'rocketName' : command[2]}
            # producer.send('launcherTopic', value=data)
            responseDestruction = requests.put("{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, command[1], command[2], 1))
            # responseDestruction = requests.put("{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, command[1], command[2], 0))

