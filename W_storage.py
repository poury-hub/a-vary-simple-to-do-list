import json
import helpers

def append_to_json(new):
    if(helpers.getdata() == False):
        data = []
    else:
        data = helpers.getdata()

    data.append(new)
    helpers.GoToJson(data)


def add_task(title):
    if(helpers.getdata() == False):
        T = []
    else:
        T = helpers.getdata()
        
        new_task={
            "ID" : len(T)+1,
            "Title" : title,
            "Done" : False
        }
        
    append_to_json(new_task)
    return


# while(1):
#     title=input("Enter ur task: ")     #for testing
#     add_task(title)


    
    
    