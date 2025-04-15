# To-Do List JSON Program

This is a command-line To-Do List program written in Python that stores tasks persistently in a JSON file. It allows users to manage their tasks by adding, removing, and viewing tasks.

## Features

- **Add a Task**: Add a new task to the to-do list.
- **Remove a Task**: Remove an existing task from the to-do list.
- **Show All Tasks**: Display all tasks in the to-do list.
- Tasks are stored persistently in a `todo.json` file.

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

The program uses the `argparse` module to parse command-line arguments and stores tasks in a JSON file (`todo.json`) for persistence. It supports three operations: `add`, `remove`, and `show`.

### Key Functions

- **`load_task()`**: Loads tasks from the `todo.json` file.
- **`save_task(task_list)`**: Saves the current task list to the `todo.json` file.
- **`add(task)`**: Adds a new task to the list and saves it.
- **`remove(task)`**: Removes a task from the list if it exists and saves the updated list.
- **`show()`**: Displays all tasks in the list.

This project demonstrates Python's file handling, JSON manipulation, and command-line argument parsing capabilities.
