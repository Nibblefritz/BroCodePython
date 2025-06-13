# if   = Do some code only IF some condition is true
# else = do something else

age = int(input("Enter your age: "))

if age >= 18 and age < 100:
    print("You are an adult. You can sign up for a credit card.")
elif age < 0:
    print("Age cannot be negative. Please enter a valid age.")
elif age >= 100:
    print("You are too old to sign up for a credit card.")    
else:
    print("You are a minor. You cannot sign up for a credit card.")

response = input("Do you want some food? (y/n): ").lower()
if response == "y":
    print("Great! What would you like to eat?")
elif response == "n":
    print("Okay, maybe next time!")
else:
    print("Invalid response. Please enter 'y' or 'n'.")
    
name = input("What is your name? ")
if name == "":
    print("You didn't enter a name.")
else:
    print(f"Hello, {name}!")
    
# Booleans with if statments
for_sale = True
if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")
    
online = False
if online:
    print("The user is available online.")
else:
    print("The user is not available online.")