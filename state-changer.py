import json

def Doner(id):
    with open("s.json" , "r") as f:
        try:
            data = json.load(f)
        except (json.JSONDecodeError):
            return False
    try:
        (data[id]["Done"]) = True
    except(IndexError):
        return False
    else:
        with open("s.json" , 'w') as ff:
            json.dump(data , ff)
        return True


if(Doner(1)):         #for test
    print("ok")