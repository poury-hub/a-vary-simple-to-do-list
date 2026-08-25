import json

def Doner(id):
    id = id - 1
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