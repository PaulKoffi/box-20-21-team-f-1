import requests

BASE_URL = "http://localhost:3000"
if __name__ == "__main__":
    while True:
        command = input().split(' ')
        if (command[0] == "quit"):
            print("Bye")
            break
        if (command[0] == "site"):
            response = requests.get("{}/site".format(BASE_URL))
            print(response.json())
        if (command[0] == "siteByName"):
            response = requests.get("{}/siteByName/{}".format(BASE_URL, command[1]))
            print(response.json())
