import math

# A = pi * r^2
radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle with radius {radius} is {round(area, 2)}cm^2.")