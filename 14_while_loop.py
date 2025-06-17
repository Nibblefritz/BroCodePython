# While loops execute a block of code as long as a specified condition is true.

name = input("Enter your name: ")

while name.strip() == "":
    print("Name cannot be empty. Please enter a valid name.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Please enter a valid age between 0 and 120.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

food = input("Enter your favorite food (type 'exit' to stop): ")
while not food.lower() == "exit":
    print(f"Your favorite food is: {food}")
    food = input("Enter another favorite food (type 'exit' to stop): ")
    
print("Bye!")

num = int(input("enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("Number must be between 1 and 10. Please try again.")
    num = int(input("enter a number between 1 and 10: "))
print(f"You entered a valid number: {num}")