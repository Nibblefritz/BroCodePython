name = input("Enter your name: ").lower()

length = len(name)
print(f"Your name has {length} characters.")

print(f"Is the name '{name}' alphabetical? {'Yes' if name.isalpha() else 'No'}") # this will fail with spaces

result = name.find(" ")
print(f"Your name has a space at index {result}." if result != -1 else "Your name does not have a space.") # if result is -1, means that there was nothing in the "result" variable

result = name.rfind("i")
print(f"Your name has an occurrence of \"i\" counting in reverse at index {result}." if result != -1 else "Your name does not have an occurrence of \"i\" counting in reverse.")

name = name.capitalize()
print(f"Your name capitalized is: {name}")
name = name.title()
print(f"Your name in title case is: {name}")
name = name.upper()
print(f"Your name in uppercase is: {name}")
name = name.lower()
print(f"Your name in lowercase is: {name}")
name = name.strip()
print(f"Your name with leading and trailing spaces removed is: {name}")
name = name.replace(" ", "_")
print(f"Your name with spaces replaced by underscores is: {name}")
name = name.split("_")
print(f"Your name split by underscores is: {name}")
name = "_".join(name)
print(f"Your name joined by underscores is: {name}")
name = name.center(50, "-")
print(f"Your name centered in a 50 character wide string is: {name}")
name = name.ljust(50, "-")
print(f"Your name left justified in a 50 character wide string is: {name}")
name = name.rjust(50, "-")
print(f"Your name right justified in a 50 character wide string is: {name}")
name = name.zfill(50)
print(f"Your name zero filled to 50 characters is: {name}")
name = name.title()
name = name.swapcase()
print(f"Your name with swapped case is: {name}")

value = "12345"
print(f"Is the value '{value}' a digit? {'Yes' if value.isdigit() else 'No'}")

phone_number = input("Enter your phone number with dashes: ")
phone_number = phone_number.replace("-", " ")
print(f"Your phone number with dashes replaced by spaces is: {phone_number}")
print(f"Your phone number without spaces is: {phone_number.replace(' ', '')}")
phone_number = phone_number.split(" ")
print(f"Your phone number split by spaces is: {phone_number}")