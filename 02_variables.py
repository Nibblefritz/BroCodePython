# Variable = A container for a value

first_name = "Kyle"
last_name = "Fifield"
food = "Pizza"
email = "Kyle.F@fake.com"

# Using an f-string to format the output
print(f"Hello, {first_name} {last_name}!")
print(f"You like {food}.")
print(f"Your email is {email}.")

# Integers
age = 30
slices = 3

print(f"You are {age} years old.")
print(f"You have {slices} slices of {food}.")

# Floats
price = 10.99
gpa = 3.6
distance = 5.5

# The :.f formats the float to 2 decimal places
print(f"The price of {food} is ${price:.2f}.")
print(f"Your GPA is {gpa:.1f}.")
print(f"You have traveled {distance:.1f} miles.")

# Booleans
is_student = True
for_sale = True
print(f"Are you a student? {is_student}.")

if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
    
if for_sale:
    print(f"{food} is for sale.")
else:
    print(f"{food} is not for sale.")

