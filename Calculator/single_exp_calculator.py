#!python 3
# Calculator.py - Basic calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error"
    return x/y

def calculator():
    print("Simple Calculator")
    print("Available operations : +,-,*/")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter the calculation")

        if user_input.lower() == 'exit':
            print('Goodbye')
            break

        try:
            # Split input into parts
            parts = user_input.split()
            if len(parts) !=3:
                raise ValueError("Invalid Input Format")

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = add(num1 + num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operator"

            print(f"Result: {result}\n")

        except ValueError as ve:
            print(f" Error: {ve}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

if __name__ == "__main__":  # The reason why this part is required is if calculator is imported as a module for its functions only
    calculator()            # then in order to not execute the program this is required
                            # The above code will run only if this file is run directly
