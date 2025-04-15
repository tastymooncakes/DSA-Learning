import argparse

def add(task):
    with open("todo.txt", "a") as f:
        f.write("\n" + task)
    print(f"Added task: {task}")
    show()

def remove(task):
    list = open("todo.txt", "r").readlines()
    task_list = [line.strip() for line in list]
    if task in task_list:
        task_list.remove(task)
    else:
        print(f"Task not found: {task}")
    open("todo.txt", "w").write("\n".join(task_list))
    show()

def show():
    list = open("todo.txt", "r").readlines()
    task_list = [line.strip() for line in list]
    if task_list:
        print("Tasks:")
        for t in task_list:
            print(f"{t}")
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

    if args.operation == "add":
        add(args.task)
    elif args.operation == "remove":
        remove(args.task)
    elif args.operation == "show":
        show()
    
    return

if __name__ == "__main__":
    main()