from xmlrpc.client import ServerProxy
import requests

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
            print(response.split(' '))
        if(command[0] == "decide"):
            print("The rocket {} at {} : {}".format(command[3],command[2],command[1]))
        if(command[0] == "destroy"):
            responseDestruction = requests.put("{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, command[1], command[2], 1))
