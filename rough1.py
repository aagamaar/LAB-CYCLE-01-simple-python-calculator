def simple_calculator():
    """
    Implements a simple desktop calculator using Python.
    """

    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your 1  choice (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == '5':
            print("Exiting the calculator.")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = None
        match choice:
            case '1':
                result = num1 + num2
                operation = "addition"
            case '2':
                result = num1 - num2
                operation = "subtraction"
            case '3':
                result = num1 * num2
                operation = "multiplication"
            case '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = "division"

        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    simple_calculator()