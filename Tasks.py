import json
from datetime import datetime
#Functions for the commands


def list_task(args):
    tasks = load_task()
    #Gets the max length of description to determine width
    widthofdescription = max(
        len("DESCRIPTION"),
        max((len(task["description"]) for task in tasks), default = 0)
    ) + 3
    #Table formatting for the current list of tasks
    print(f"{'ID':<5}{'DESCRIPTION':<{widthofdescription}}{'STATUS':<15}{'CREATED'}")
    print("-" * (5 + widthofdescription + 15 + 10))

    #Check each task and if it matches the status provided by the user, only list those tasks, otherwise just list all
    if args.status is not None:
        tasks = [task for task in tasks if task["status"] == args.status]
    for task in tasks:
            #Formatting so the table looks aligned
            print(f"{task['id']:<5}{task['description']:<{widthofdescription}}{task['status']:<15}{task['createdAt'][:10]}")






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
#Updates a specific tasks (using ID)
def update_task(args):
    tasks = load_task()
    for task in tasks:
        if task["id"] == args.id:
            if args.description:
                task["description"] = args.description
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

