# Python calculator

operation = input("Enter an operation (add, subtract, multiply, divide): ")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if not num1.isdigit() or not num2.isdigit():
    print("Error: Please enter valid numbers.")
    exit()
elif operation == "add":
    result = float(num1) + float(num2)
elif operation == "subtract":
    result = float(num1) - float(num2)
elif operation == "multiply":
    result = float(num1) * float(num2)
elif operation == "divide":
    operation = "divid"
    if float(num2) == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = float(num1) / float(num2)

else:
    print(f"Error: {operation} is an invalid operation.")
    exit()

print(f"The result of {operation}ing {num1} and {num2} is: {round(result,2)}")