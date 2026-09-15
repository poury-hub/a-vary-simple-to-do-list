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
    try:
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
        return True
    except(Exception):
        return False





    
    
    