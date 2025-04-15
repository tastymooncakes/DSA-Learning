import argparse
import os
import json

FILE = "todo.json"

def load_task():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)
    
def save_task(task_list):
    with open(FILE, "w") as f:
        json.dump(task_list, f, indent=2)

def add(task):
    task_list = load_task()
    task_list.append(task)
    save_task(task_list)
    show()

def remove(task):
    task_list = load_task()
    if task in task_list:
        task_list.remove(task)
    else:
        print(f"Task not found: {task}")
    save_task(task_list)
    show()

def show():
    task_list = load_task()
    if task_list:
        print("Tasks:")
        for task in task_list:
            print(f"- {task}")
    else:
        print("No tasks found.")

def main():
    parser = argparse.ArgumentParser(description="To-Do List Manager")
    subparser = parser.add_subparsers(dest="operation", required=True)

    add_parser = subparser.add_parser("add", help="Add a tasl")
    add_parser.add_argument("task", type=str, help="Task to add")

    remove_parser = subparser.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("task", type=str, help="Task to remove")

    show_parser= subparser.add_parser("show", help="Show all tasks")

    args = parser.parse_args()

    if args.operation == "add":
        add(args.task)
    elif args.operation == "remove":
        remove(args.task)
    elif args.operation == "show":
        show()

if __name__ == "__main__":
    main()