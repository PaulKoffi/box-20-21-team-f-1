import requests
from xmlrpc.client import ServerProxy

BASE_URL = "http://127.0.0.1:8000"
serverLaucher = ServerProxy('http://localhost:8888')
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
            print("The rocket: {} can {}".format(command[1], command[2]))
        if(command[0] == "sendRocketStates"):
            serverLaucher.sendRocketStates(command[1],command[2])
