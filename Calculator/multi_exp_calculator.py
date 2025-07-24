#!python3
#Mlti_exp_calculator,py - Evaluates multiple expressions

def calculator():
    print('Python CLI Calculator')
    print("Type exit to quit.\n")

    while True:
        expr = input("Enter the expression:\n")

        if expr.lower() == 'exit':
            print('Goodbye')
            break

        try:
            result = eval(expr) # Evaluates the math expression
            print(f"Result :{result}")

        except ZeroDivisionError:
            print("Cannot divide by zero!\n")

        except Exception as e:
            print("Invalid expression: {e}\n")

if __name__ == "__main__":
    calculator()
