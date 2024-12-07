def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    operation = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")

    if operation not in {"1", "2", "3", "4"}:
        print("Invalid operation. Please restart the calculator and try again.")
        return

    try:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if operation == "1":
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif operation == "2":
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif operation == "3":
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif operation == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
