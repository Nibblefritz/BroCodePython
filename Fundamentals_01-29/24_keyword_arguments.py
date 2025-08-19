# Keyword arguments = an argument preceded by an identifier and an equal sign
#   Helps with readability
#   Order of arguments doesn't matter

def hello(greeting, title, first_name, last_name):
    print(f"{greeting},{title} {first_name} {last_name}")
    
hello(greeting="Hello", title="Mr.", first_name="John", last_name="Doe") # Keyword arguments
hello("Hi", "Ms.", "Jane", "Smith")  # Positional arguments
# Mixing positional and keyword arguments
hello("Greetings", "Dr.", last_name="Brown", first_name="Alice")

for x in range(1, 11):
    print(x, end=" ")  # End is a keyword argument that specifies what to print at the end of each print call
    
print("1", "2", "3", sep=", ")  # Sep is a keyword argument that specifies what to print between each argument

def get_phone(country, area, first, last):
    return f"+{country}-({area})-{first}-{last}"

phone_num = get_phone(country=1, area=415, first=555, last=1234)
print(phone_num)  # Output: +1-(415)-5551234