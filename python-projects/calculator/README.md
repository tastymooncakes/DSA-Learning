# Calculator Program

This is a command-line calculator program written in Python. It performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Supports the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x`)
  - Division (`/`)
- Handles edge cases like division by zero with an appropriate error message.

## Usage

Run the script with the following arguments:
1. `operation`: The operation to perform (`+`, `-`, `x`, `/`).
2. `num1`: The first number (float).
3. `num2`: The second number (float).

### Example

```bash
python main.py + 5 3
```

Output:
```
Result: 8.0
```

### Division by Zero Example

```bash
python main.py / 5 0
```

Output:
```
Error: Division by zero
```

## Requirements

- Python 3.x

## How It Works

The program uses the `argparse` module to parse command-line arguments and performs the specified operation based on the input.

```python
# ...existing code...
if args.operation == "+":
    result = args.num1 + args.num2
elif args.operation == "-":
    result = args.num1 - args.num2
# ...existing code...
```

This program is a simple demonstration of Python's argument parsing and basic arithmetic operations.