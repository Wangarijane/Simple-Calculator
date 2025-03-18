def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter operation (+, -, *, /): ")
    
    try:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"{num1} {op} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

calc()