import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["+", "-", "x", "/"], help="calculator operation to perform")
    parser.add_argument("num1", type=float, help="first number")
    parser.add_argument("num2", type=float, help="second number")

    args = parser.parse_args()
    if args.operation == "+":
        result = args.num1 + args.num2
    elif args.operation == "-":
        result = args.num1 - args.num2
    elif args.operation == "x":
        result = args.num1 * args.num2
    elif args.operation == "/":
        if args.num2 == 0:
            print("Error: Division by zero")
            return
        result = args.num1 / args.num2
    else:
        print("Invalid Operation")
        return
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()