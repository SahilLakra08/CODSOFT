#TASK 2
# A simple calculator to perform basic arithmetic operations

print("Welcome to the CodSoft Simple Calculator!")
print("This calculator can perform addition, subtraction, multiplication, and division.")

try:
        # Ask the user for the first number
        num1 = float(input("Enter the first number: "))
        
        # Ask the user for the second number
        num2 = float(input("Enter the second number: "))
        
        # Ask the user to choose an operation
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the number or symbol of the operation (e.g., 1 or +): ")

        # Perform the calculation based on the user's choice
        if operation == '1' or operation == '+':
            result = num1 + num2
            print(f"\nThe result of {num1} + {num2} is: {result}")
        elif operation == '2' or operation == '-':
            result = num1 - num2
            print(f"\nThe result of {num1} - {num2} is: {result}")
        elif operation == '3' or operation == '*':
            result = num1 * num2
            print(f"\nThe result of {num1} * {num2} is: {result}")
        elif operation == '4' or operation == '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nInvalid operation choice. Please try again.")

except ValueError:
        print("\nInvalid input. Please enter numeric values only.")

print("\nThank you for using the CodSoft Simple Calculator!")


