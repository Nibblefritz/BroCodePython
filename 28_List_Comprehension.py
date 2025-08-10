# List Comprehension = A concise way to create lists in Python
# compact and easier to read than traditional loops
# Formula  > [expression for value in iterable if condition]

doubled = [n * 2 for n in range(1, 11)]
print(doubled)
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers if n % 2 == 0] # if n modulo 2 equals 0 then square the number
print(squared)

numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry", "date"]]
print(fruits)
fruits = [fruit[0] for fruit in ["apple", "banana", "cherry", "date"]]
print(fruits)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
