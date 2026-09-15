import json


def GoToJson(data):
    with open("s.json" , "w") as ff:
        json.dump(data , ff , indent = 4)

def getdata():
    with open("s.json" , "r") as ff:
        try:
            data = json.load(ff)
        except (json.JSONDecodeError):
            return False
    return data