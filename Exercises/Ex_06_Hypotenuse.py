import math
# Hypotenuse of a right triangle
# c = sqrt(a^2 + b^2)

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
# Also can use `c = math.hypot(a, b)`

print(f"The length of the hypotenuse is {round(c, 2)}cm.")