# Iterables = an object/collection that can return its members one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5] # a list is an iterable
for number in numbers:
    print(number, end=" ")  # Printseach number in the list on the same line
    
print()

nums = (10, 20, 30, 40, 50)  # a tuple is also an iterable
for item in reversed(nums):  # reversed() returns an iterator that accesses the given iterable in the reverse order
    print(item, end=" ")  # Prints each number in reverse order on the same line

print()

fruits = {"apple", "banana", "cherry"}  # a set is an iterable, but not reversible
for fruit in fruits:
    print(fruit, end=" ")  # Prints each fruit in the set on the same line
    
print()
name = "John Doe"  # a string is also an iterable
for char in name:
    print(char, end=" ")  # Prints each character in the string on the same line
    
print()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}  # a dictionary is an iterable
for value in my_dict.values():  # values() returns a view object that displays
    print(value, end=" ")  # Prints each value in the dictionary on the same line
print()
for key, value in my_dict.items():  # items() returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(f"{key}: {value}", end=" ")  # Prints each key-value pair in the dictionary on the same line