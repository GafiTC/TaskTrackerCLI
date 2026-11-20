import json
import argparse
from Tasks import load_task,save_task, add_task, delete_task

#def  update_task()



parser = argparse.ArgumentParser(description="Simple Task Tracker")
subparsers = parser.add_subparsers(dest="command",required=True)

addTaskParser = subparsers.add_parser("add", help = "Task to be added")
addTaskParser.add_argument("task", help = "Name of task")
addTaskParser.set_defaults(func=add_task)

updateTaskParser = subparsers.add_parser("update", help = "Update a task")
updateTaskParser.add_argument("task", help = "Task id to be updated")

deleteTaskParser = subparsers.add_parser("delete", help= "Delete a task")
deleteTaskParser.add_argument("id",type=int, help = "Task id to be deleted")
deleteTaskParser.set_defaults(func=delete_task)

args = parser.parse_args()

if args.command == "add":
    args.func(args.task)

elif args.command == "delete":
    args.func(args.id)














