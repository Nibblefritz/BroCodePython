# function = a block of reusable code
# place () after the function to call (invoke) it

def happy_birthday():
    print("Happy Birthday to you!")
    print("You are old!")
    print("Happy Birthday to you!")
    print()
    
happy_birthday()  # Call the function to execute its code
happy_birthday()  # Call the function again to see it run multiple times
happy_birthday()


# Any data you put in the parenthesis of a function is called an argument
# You can also define functions that take arguments to customize their behavior
# four types of arguments # 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
# Positional Arguments = arguments that are passed in the order they are defined
def happy_birthday_to(name, age):
    print("Happy Birthday to you, " + name + "!")
    print("You are " + str(age) + " years old!")
    print("Happy Birthday to you, " + name + "!")
    print()
    
happy_birthday_to("Alice", 20)  # Call the function with an argument
happy_birthday_to("Bob", 30)    # Call the function with another argument
happy_birthday_to("Charlie", 40)  # Call the function with yet another argument


# Return Statements = statement to end a function and return a result back to the caller
def add_numbers(x, y):
    z = x + y
    return z  # Return the result of the addition

def subtract_numbers(x, y):
    z = x - y
    return z  # Return the result of the subtraction

def multiply_numbers(x, y):
    z = x * y
    return z  # Return the result of the multiplication

def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero!"  # Handle division by zero
    z = x / y
    return z  # Return the result of the division

result = add_numbers(5, 10)  # Call the function and store the result
print(f"The sum of 5 and 10 is {result}.")  # Print the result
result = subtract_numbers(10, 5)  # Call the function and store the result
print(f"The difference between 10 and 5 is {result}.")  # Print the result
result = multiply_numbers(5, 10)  # Call the function and store the result
print(f"The product of 5 and 10 is {result}.")  # Print the result
result = divide_numbers(10, 5)  # Call the function and store the result
print(f"The quotient of 10 and 5 is {result}.")  # Print the result
result = divide_numbers(10, 0)  # Call the function with zero to test error handling
print(result)  # Print the error message for division by zero
    

def create_name(first_name, last_name):
    first = first_name.strip()  # Remove any leading/trailing spaces from the first name
    last = last_name.strip()  # Remove any leading/trailing spaces from the last name

    first = first.capitalize()  # Capitalize the first name
    last = last.capitalize()  # Capitalize the last name

    full_name = first + " " + last  # Concatenate first and last name
    return full_name  # Return the full name
    
print(create_name("john", "doe"))  # Call the function with lowercase names
print(create_name("  jane ", " smith "))  # Call the function with names containing spaces      