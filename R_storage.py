import json
import helpers



def readboy():
    data = helpers.getdata()

    for i in data:
        
        print("ID:" + str(i["ID"]))

        print("Titel:" + str(i["Title"]))

        if(i["Done"] == True):
            print("Done")
        else:
            print("still not finished")
            
        print("---------------------------")
            