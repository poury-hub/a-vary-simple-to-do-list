import json

with open("s.json", "r") as f:
    data = json.load(f)
    for i in data:
        
        print("ID:" + str(i["ID"]))

        print("Titel:" + str(i["Titel"]))

        if(i["Done"] == True):
            print("Done")
        else:
            print("still not finished")
        
        print("---------------------------")
        
