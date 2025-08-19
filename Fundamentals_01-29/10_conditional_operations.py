# Conditional Expressions = a one line shortcut for if-else statements (ternary operator)
# Syntax: value_if_true if condition else value_if_false

num = 5

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(f"{"Positive" if num > 0 else "Negative"} number")
result = "Even" if num % 2 == 0 else "Odd"
print(result)

print(max_num)
print(min_num)