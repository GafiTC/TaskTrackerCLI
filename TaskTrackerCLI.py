import json
import argparse
from Tasks import load_task,save_task, add_task, delete_task, update_task, list_task
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple Task Tracker")
subparsers = parser.add_subparsers(dest="command",required=True)

listAllTasks = subparsers.add_parser("list", help = "Lists all the current asks")
listAllTasks.add_argument(
    "status",
    nargs="?",
    choices = ["todo","in-progress","done"],
    default=None,
    help = "Which task status do you want listed"
)
listAllTasks.set_defaults(func=list_task)



addTaskParser = subparsers.add_parser("add", help = "Task to be added")
addTaskParser.add_argument("task", help = "Name of task")
addTaskParser.set_defaults(func=add_task)

updateTaskParser = subparsers.add_parser("update", help = "Update a task")
updateTaskParser.add_argument("id", type=int, help = "Task id to be updated")
updateTaskParser.add_argument("description", nargs="?", default = None, help="Optional task description")
updateTaskParser.set_defaults(func=update_task)


deleteTaskParser = subparsers.add_parser("delete", help= "Delete a task")
deleteTaskParser.add_argument("id",type=int, help = "Task id to be deleted")
deleteTaskParser.set_defaults(func=delete_task)

args = parser.parse_args()

if hasattr(args,"func"):
    args.func(args)
else:
    parser.print_help()













