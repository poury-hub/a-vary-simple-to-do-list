import json


def readboy():
    with open("s.json", "r") as f:
        data = json.load(f)
        for i in data:
            
            print("ID:" + str(i["ID"]))

            print("Titel:" + str(i["Title"]))

            if(i["Done"] == True):
                print("Done")
            else:
                print("still not finished")
            
            print("---------------------------")
            