import math
import argparse
from Tasks import tasks

"""
areaCircle = input("Enter the radius of the circle")
parser = argparse.ArgumentParser(description="Calculates area of a circle")
parser.add_argument("-r", "--radius", type=int, metavar="", help = "Area of a circle")
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
args = parser.parse_args([--name])
def circle_area(radius):
    area = (math.pi) * (radius ** 2)
    return area
if __name__ == "__main__":
    Area = (circle_area(args.radius))
    if args.quiet:
        print (Area)
    elif args.verbose:
        print ("Volume of a circle with radius %s is %s" % (args.radius,Area))
    else:
        print ("Volume of circle = %s" % (Area))
"""

def add_task(title, done= False):
    new_task = {
        "description": title,
        "done": done
    }
    tasks.append(new_task)

def


parser = argparse.ArgumentParser(description="Simple Task Tracker")
subparsers = parser.add_subparsers(dest="command",required=True)

addTaskParser = subparsers.add_parser("add", help = "Task to be added")
addTaskParser.add_argument("task", help = "Name of task")
addTaskParser.set_defaults(func=add_task)

updateTaskParser = subparsers.add_parser("Update", help = "Update a task")
updateTaskParser.add_argument("update", help = "Task id to be updated")

deleteTaskParser = subparsers.add_parser("Delete", help= "Delete a task")
deleteTaskParser.add_argument("delete",help = "Task id to be deleted")










