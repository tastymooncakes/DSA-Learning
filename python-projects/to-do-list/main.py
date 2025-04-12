import argparse

def add(task_list, task):
    task_list.append(task)
    print(f"Added task: {task}")
    show(task_list)

def remove(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Removed task: {task}")
        show(task_list)
    else:
        print(f"Task not found: {task}")

def show(task_list):
    if task_list:
        print("Tasks:")
        for t in task_list:
            print(f"- {t}")
    else:
        print("No tasks found.")

def main():
    
    parser = argparse.ArgumentParser(description="To-Do")
    subparser = parser.add_subparsers(dest="operation", required=True)

    add_parser = subparser.add_parser("add", help="Add a task")
    add_parser.add_argument("task", type=str, help="task to add")

    remove_parser = subparser.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("task", type=str, help="task to remove")

    show_parser = subparser.add_parser("show", help="Show all tasks")

    args = parser.parse_args()
    task_list = []

    if args.operation == "add":
        add(task_list, args.task)
    elif args.operation == "remove":
        remove(task_list, args.task)
    elif args.operation == "show":
        show(task_list)
    
    return

if __name__ == "__main__":
    main()