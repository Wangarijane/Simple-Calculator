# Basic Calculator Program

# Importing necessary libraries
def calculator():
    # Prompt user to input two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Prompt user to input a mathematical operation
    operation = input("Enter the operation ((+),(-),(*),(/)): ")

    # Convert inputs to integers
    num1 = int(num1)
    num2 = int(num2)

    # Perform operation based on user's input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check if division by zero will not occur
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is undefined.")
    else:
        print("Error: Invalid operation.")

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Running the calculator function
calculator()