# Default arguments in Python functions
# A default argument is a value that is used if no argument is provided for that parameter when the function is called.
# They make you functions more flexible and easier to use.

""" def happy_birthday_to(name="Friend", age=18):
    print("Happy Birthday to you, " + name + "!")
    print("You are " + str(age) + " years old!")
    print("Happy Birthday to you, " + name + "!")
    print()

happy_birthday_to()  # Call the function without arguments
happy_birthday_to("Alice", 25)  # Call the function with custom arguments
"""

def net_price(list_price, discount=0.0, tax=0.065):
    return list_price * (1.0 - discount) * (1.0 + tax)

print(f"Normal Price: {net_price(500)}")
print(f"Discounted Price: {net_price(500, 0.1)}")
print(f"Discounted Price without Tax: {net_price(500, 0.1, 0.0)}")