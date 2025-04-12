# To-Do List Program

This is a command-line To-Do List program written in Python. It allows users to manage their tasks by adding, removing, and viewing tasks.

## Features

- **Add a Task**: Add a new task to the to-do list.
- **Remove a Task**: Remove an existing task from the to-do list.
- **Show All Tasks**: Display all tasks in the to-do list.

## Usage

Run the script using Python with the following commands:

### Add a Task
```bash
python main.py add "Buy groceries"
```
Output:
```
Added task: Buy groceries
Tasks:
- Buy groceries
```

### Remove a Task
```bash
python main.py remove "Buy groceries"
```
Output:
```
Removed task: Buy groceries
No tasks found.
```

### Show All Tasks
```bash
python main.py show
```
Output:
```
Tasks:
- Task 1
- Task 2
```

## Requirements

- Python 3.x

## How It Works

The program uses the `argparse` module to parse command-line arguments. It supports three operations: `add`, `remove`, and `show`. Tasks are stored in a list during the program's runtime.

```python
# ...existing code...
if args.operation == "add":
    add(task_list, args.task)
elif args.operation == "remove":
    remove(task_list, args.task)
elif args.operation == "show":
    show(task_list)
# ...existing code...
```

This project is a simple demonstration of Python's argument parsing and list manipulation capabilities.