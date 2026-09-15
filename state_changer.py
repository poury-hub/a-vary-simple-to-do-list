import json
import helpers 


def Done(id):
    index = id - 1
    if(helpers.getdata() == False):
        return False
    else:
        data = helpers.getdata()

    try:
        (data[index]["Done"]) = True

    except(IndexError):
        return False

    else:
        helpers.GoToJson(data)
        return True


def Deleter(id):
    index = id - 1
    if(helpers.getdata() == False):
        return False
    else:
        data = helpers.getdata()

    try:
        del data[index]

    except(IndexError):
        return False

    else:
        for i in range(index , len(data)):
            data[i]["ID"] = i + 1  #index in is always 1 less that ID 
        helpers.GoToJson(data)
        return True

