import requests

BASE_URL = "http://0.0.0.0:8000"
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