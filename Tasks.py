import json
from datetime import datetime
#Functions for the commands

def add_task(args):
    tasks = load_task()
    next_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": next_id,
        "description": args.task,
        "status": "todo",
        "createdAt": datetime.now().isoformat(timespec="seconds"),
        "updatedAt": datetime.now().isoformat(timespec= "seconds")
    }
    tasks.append(new_task)
    print("Task added successfully (ID:%s)" % next_id)
    save_task(tasks)

#Deletes automatically if done, if not, asks user if they're sure
def delete_task(args):
    tasks = load_task()
    for task in tasks:
        if task["id"] == args.id:
            if task["status"] != "done":
                confirm = input("Task is NOT done, Delete anyway? (Y/n): ")
                if confirm.upper()!= "Y":
                    print("Deletion stopped")
                    return
            tasks.remove(task)
            #Update the ids so that they aren't static
            for index, taskRemaining in enumerate(tasks,start=1):
                taskRemaining["id"] = index

            save_task(tasks)
            print("Task deleted")
            return

def update_task(args):
    tasks = load_task()
    for task in tasks:
        if task["id"] == args.id:
            if args.description:
                task["description"] = args.description
                task["updatedAt"] = datetime.now().isoformat(timespec="seconds")
            if args.status:
                task["status"] = args.status
                task["updatedAt"] = datetime.now().isoformat(timespec="seconds")
            save_task(tasks)
            break
        else:
            print("Task not found")




#Functions for accessing/modifying JSON with tasks

def load_task():
    with open("tasks.json","r") as f:
        d = json.load(f)
    return d

def save_task(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=3)

