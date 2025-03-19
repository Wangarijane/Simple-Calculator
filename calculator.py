def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")
        
        if op == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Please enter valid numbers!")

calculator()
