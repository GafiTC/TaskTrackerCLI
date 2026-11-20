import json

#Functions for the commands

def add_task(title, done= False):
    tasks = load_task()
    next_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": next_id,
        "description": title,
        "done": done
    }
    tasks.append(new_task)
    print("Task added successfully (ID: %s" % next_id)
    save_task(tasks)

#Deletes automatically if done, if not, asks user if they're sure
def delete_task(task_id):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            if not task["done"]:
                confirm = input("Task is NOT done, Delete anyway? (Y/n): ")
                if confirm.upper()!= "Y":
                    print("Deletion stopped")
                    return
            tasks.remove(task)
            save_task(tasks)
            print("Task deleted")
            return

#Functions for accessing/modifying JSON with tasks

def load_task():
    with open("tasks.json","r") as f:
        d = json.load(f)
    return d

def save_task(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=3)

