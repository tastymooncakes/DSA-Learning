import argparse

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def mulitply(a, b):

    return a * b

def divide(a, b):
    if b == 0:
        print("Error : Division by zero")
        return None
    
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["+", "-", "*", "/"], help="calculator operation to perform")
    parser.add_argument("num1", type=float, help="first number")
    parser.add_argument("num2", type=float, help="second number")

    args = parser.parse_args()
    
    operations = {
        "+": add,
        "-": subtract,
        "*": mulitply,
        "/": divide
    }

    result = operations.get(args.operation)(args.num1, args.num2)
    
    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()