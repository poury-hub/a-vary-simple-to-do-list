import json

def Doner(id):
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


def deleter(id):
    index = id - 1
    with open("s.json" , "r") as f:
        try:
            data = json.load(f)
        except (json.JSONDecodeError):
            return False
    try:
        del data[index]

    except(IndexError):
        return False

    else:
        for i in range(index , len(data)):
            data[i]["ID"] = i + 1


