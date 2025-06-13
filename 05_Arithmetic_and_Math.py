# Basic Arithmetic and Math Operators

friends = 0
friends += 4  # Incrementing friends by 4
friends -= 1  # Decrementing friends by 1
friends *= 2  # Doubling the number of friends
friends *= 3  # Tripling the number of friends
friends /= 2  # Halving the number of friends
friends %= 2  # Modulus (remainder) operation, friends will be 0 if divisible by 2
# Modulus is fairly common to use to find if a number is even or odd.

print(f"Number of friends: {friends}")

# Math related functions
x = 3.14
y = -4
z = 5

result = round(x)
print(f"Rounded value of {x} is {result}")

result = abs(y)
print(f"Absolute value of {y} is {result}")

result = pow(z, 2)
print(f"{z} raised to the power of 2 is {result}")

result = max(x, y, z)
print(f"Maximum value among {x}, {y}, and {z} is {result}")

result = min(x, y, z)
print(f"Minimum value among {x}, {y}, and {z} is {result}")
