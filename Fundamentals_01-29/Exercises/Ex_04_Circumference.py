import math

# Calculate the circumference of a circle
# C = 2 * pi * r

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference of the circle with radius {radius} is {round(circumference, 2)}cm.")