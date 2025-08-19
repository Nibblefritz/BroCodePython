# Typecasting is the process of converting one data type to another.
# str(), int(), float(), and bool() are the most common typecasting functions in Python.

name = "Kyle Fifield"
age = 33
gpa = 3.6
is_student = True

# Printing the types of the variables
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Typecasting
print(int(gpa))
print(float(age))
print(str(is_student))

print(f"{str(age)} is of type {type(str(age))}.")
print(f"{int(gpa)} is of type {type(int(gpa))}.")
print(f"{float(is_student)} is of type {type(float(is_student))}.")
print(f"{str(is_student)} is of type {type(str(is_student))}.")

# Concatenation
print("Hello, " + name + "! You are " + str(age) + " years old and your GPA is " + str(gpa) + ".")
print(float(age) + gpa)