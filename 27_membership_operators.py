# Membership Operators = used to test if a sequence is presented in an object
# Strings, lists, tuples, sets, and dictionaries can be checked for membership using these operators
# 1. in
# 2. not in

word = 'APPLE'
sequence = '123489'

letter = input("Enter a letter to check if it's in the word: ").upper()

if letter in word:
    print(f"The letter '{letter}' is in the word '{word}'.")
else:
    print(f"The letter '{letter}' is not in the word.")
    
number = input("Enter a number to check if it's in the sequence: ")
if number not in sequence:
    print(f"The number '{number}' is not in the sequence '{sequence}'.")
else:
    print(f"The number '{number}' is in the sequence '{sequence}'.")
    
grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}

print()
student = input("Enter a student's name to check if they are in the grades dictionary: ")
if student in grades:
    print(f"{student} is in the grades dictionary with a score of {grades[student]}.")
else:
    print(f"{student} is not in the grades dictionary.")
    
email = 'bro@gmail.com'
if '@' in email and '.' in email:
    print(f"The email '{email}' is valid.")
else:
    print(f"The email '{email}' is not valid.")