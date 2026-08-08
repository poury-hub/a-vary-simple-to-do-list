title=input("Enter ur task: ")
tasks=[]

def add_task(tasks, title):
    new_task={
        "ID" : len(tasks)+1,
        "Tile" : title,
        "Done" : False
    }

    tasks.append(new_task)
    return tasks

add_task(tasks, title)
print(tasks)
