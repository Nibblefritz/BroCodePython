# Collection = single "variable" that can hold multiple values
# Examples of collections in Python include:
# 1. Lists = [] ordered and unchangeable, duplicates ok
# 2. Tuples = () ordered and unchangeable, duplicates ok, FASTER than lists
# 3. Sets = {} unordered and immutable, no duplicates, add/remove okay
# 4. Dictionaries (We will cover these in later lessons)

fruit = ["apple", "banana", "cherry", "date", "elderberry"]
# Lists are ordered, changeable, and allow duplicate values.
print(fruit)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruit[0])  # Output: apple
print(fruit[1:3])  # Output: ['banana', 'cherry']
fruit[1] = "blueberry"  # Change value at index 1
print(fruit)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']
print(fruit.index("date"))  # Output: 3 (index of 'date')
fruit.append("fig")  # Add a new item to the end of the list
print(fruit)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']
fruit.remove("cherry")  # Remove an item by value
print(fruit)  # Output: ['apple', 'blueberry', 'date', 'elderberry', 'fig']
fruit.sort()  # Sort the list in ascending order
print(fruit)  # Output: ['apple', 'blueberry', 'date', 'elderberry', 'fig']
fruit.reverse()  # Reverse the order of the list
print(fruit)  # Output: ['fig', 'elderberry', 'date', 'blueberry', 'apple']
# Lists can contain mixed data types
mixed_list = [1, "banana", 3.14, True]

for i in fruit:
    print(i, end=' ')
print()
# print(dir(fruit))  # Show all methods and attributes of the list object
# print(help(fruit))  # Show help documentation for the list object
# print(help(fruit.sort)) # Show help documentation for the sort method

print("apple" in fruit)

print()
print()

# Tuples are ordered, unchangeable, and allow duplicate values.
fruit_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print(fruit_tuple)  # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(fruit_tuple[0])  # Output: apple
print(fruit_tuple[1:3])  # Output: ('banana', 'cherry')
# Tuples cannot be changed, so we cannot modify them like lists
# However, we can convert a tuple to a list, modify it, and convert it back to a tuple
fruit_list = list(fruit_tuple)  # Convert tuple to list
fruit_list[1] = "blueberry"  # Change value at index 1
fruit_tuple = tuple(fruit_list)  # Convert list back to tuple
print(fruit_tuple)  # Output: ('apple', 'blueberry', 'cherry', 'date', 'elderberry')
# Tuples can also contain mixed data types
mixed_tuple = (1, "banana", 3.14, True)

print()
print()

# Sets are unordered, unchangeable, and do not allow duplicate values.
fruit_set = {"apple", "banana", "cherry", "date", "elderberry"}
print(fruit_set)  # Output: {'banana', 'date', 'elderberry', 'apple', 'cherry'}
fruit_set.add("fig")  # Add a new item to the set
print(fruit_set)  # Output: {'banana', 'date', 'elderberry', 'apple', 'cherry', 'fig'}
fruit_set.remove("cherry")  # Remove an item by value
print(fruit_set)  # Output: {'banana', 'date', 'elderberry', 'apple', 'fig'}
# Sets do not support indexing or slicing
# Example of a set with mixed data types
mixed_set = {1, "banana", 3.14, True}