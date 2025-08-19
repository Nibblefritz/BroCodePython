# Validate User Input
# Username is no longer than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username must be no longer than 12 characters.")
# elif not username.find(" ") == -1: # Checks if there is a space in the username
elif " " in username:
    print("Username must not contain spaces.")
# elif not username.isalpha(): # Checks if the username is not alphabetic
elif any(char.isdigit() for char in username): # Checks if any character is a digit with a for loop with each char
    print("Username must not contain digits.")
else:
    print(f"Username '{username}' is valid.")