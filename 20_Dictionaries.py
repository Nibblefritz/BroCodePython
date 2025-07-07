# A Collection that consists of {key:value} pairs
# Ordered and changable, no duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

# Show all attributes and methods
# print(dir(capitals))
# print()
# print(help(capitals))
# print()

print(capitals.items())
keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)
print()
for key in keys: # Iterate over every key
    print(capitals.get(key), end=", ")
print()
print()

for key, value in capitals.items():
    print(f"{key}: {value}")
print()
print()

print(capitals.get("USA"))
print(capitals.get("China"))
print()

capitals.update({"Germany": "Berlin", "Japan": "Tokyo"})
print(capitals)
print()

capitals.update({"USA": "Boston"}) # Updates the value for USA because no duplicates
print(capitals)
print()

capitals.pop("China") # This pops the item for the key provided
print(capitals)
print()

capitals.popitem() # This will pop the latest item in the dictionary (no key)
print(capitals)
print()

capitals.update({"Mexico": "Mexico City", "England": "London"})

country_choice = input("What country do you want to check? ")
if capitals.get(country_choice):
    print(f"That Capital exists and is: {capitals.get(country_choice)}")
else:
    print("That Capital does not exist.")

capitals.clear() # clears the entire dictionary