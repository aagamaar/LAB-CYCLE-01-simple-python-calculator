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
        print("5. Modulo ")
        print("6. Exit")

        choice = input("Enter any one of your choice (1-6): ")

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Kindly enter a number between 1 and 6")
            continue

        if choice == '6':
            print("Exiting the calculator.")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = None
        match choice:
            case '1':
                result = num1 + num2
                operation = " + "
            case '2':
                result = num1 - num2
                operation = " - "
            case '3':
                result = num1 * num2
                operation = " * "
            case '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = " / "
            case '5':
                if num2==0:
                    print("Zero Division Error")
                    continue
                result= num1 % num2
                operation= " % "

        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    simple_calculator()