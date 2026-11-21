
import argparse
from Tasks import load_task,save_task, add_task, delete_task, update_task, list_task, mark_task


def main():

    parser = argparse.ArgumentParser(description="Simple Task Tracker")
    subparsers = parser.add_subparsers(dest="command",required=True)

    listalltasks = subparsers.add_parser("list", help = "Lists all the current asks")
    listalltasks.add_argument(
        "status",
        nargs="?",
        choices = ["todo","in-progress","done"],
        default=None,
        help = "Which task status do you want listed"
    )
    listalltasks.set_defaults(func=list_task)

    addtaskparser = subparsers.add_parser("add", help = "Task to be added")
    addtaskparser.add_argument("task", help = "Name of task")
    addtaskparser.set_defaults(func=add_task)

    updatetaskparser = subparsers.add_parser("update", help = "Update a task")
    updatetaskparser.add_argument("id", type=int, help = "Task id to be updated")
    updatetaskparser.add_argument("description", nargs="?", default = None, help="Optional task description")
    updatetaskparser.set_defaults(func=update_task)

    deletetaskparser = subparsers.add_parser("delete", help= "Delete a task")
    deletetaskparser.add_argument("id",type=int, help = "Task id to be deleted")
    deletetaskparser.set_defaults(func=delete_task)

    marktasks = subparsers.add_parser("mark", help = "Mark task as in progress or done")
    marktasks.add_argument("status", choices = ["done","in-progress"])
    marktasks.add_argument("id",type = int, help = "Task id to be marked done or in-progress")
    marktasks.set_defaults(func=mark_task)



    args = parser.parse_args()

    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()














