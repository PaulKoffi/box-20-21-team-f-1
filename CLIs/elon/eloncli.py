import requests
from xmlrpc.client import ServerProxy

BASE_URL = "http://localhost:8000"
rocket = ServerProxy('http://localhost:8888')


if __name__ == "__main__":
    while True:
        command = input().split(' ')
        if (command[0] == "quit"):
            print("Bye")
            break
        if(command[0] == "rockets"):
            response = requests.get("{}/rockets".format(BASE_URL))
            print(response.json())
        if(command[0] == "rocket"):
            response = requests.get("{}/rocket/{}".format(BASE_URL,command[1]))
            print(response.json())
        if(command[0] == "poll"):
            print("The rocket: {} can {}".format(command[1], command[1]))
        if(command[0] == "sendStates"):
            rocket.sendStates(command[1],command[2])
        