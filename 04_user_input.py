# How to get user input in Python
# User input is obtained using the input() function.
# The input() function returns a string, so you may need to typecast it to the desired data type.

name = input("What is your name? ")
age = int(input("What is your age? "))
gpa = float(input("What is your GPA? "))
is_student = input("Are you a student? (yes/no) ").lower() == "yes"

print(f"Hello, {name}! You are {age} years old and your GPA is {gpa:.1f}.")
if is_student:
    print("You are a student.")