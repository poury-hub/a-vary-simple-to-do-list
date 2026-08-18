import json


def append_to_json(j , new):
    with open(j , "r") as f:
        try:
            data = json.load(f)
        except (json.JSONDecodeError):
            data=[]

        data.append(new)
        with open(j , "w") as f:
            json.dump(data , f)


def add_task(title):
    with open("s.json", "r") as f:
        try:
            T = json.load(f)
        except(json.JSONDecodeError):
            T = []
        new_task={
            "ID" : len(T)+1,
            "Title" : title,
            "Done" : False
        }
        
    append_to_json("s.json" , new_task)
    return


# while(1):
#     title=input("Enter ur task: ")     #for testing
#     add_task(title)


    
    
    