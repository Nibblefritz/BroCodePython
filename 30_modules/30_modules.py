# module = a file containing Python code that can be imported and used in other Python programs
# use 'import' to include a module in your code (built in or your own)
# useful to break up a large program into smaller, manageable pieces

# print(help("modules")) # This will print a list of all available modules
# print(help("math")) # This will print information about the math module

# import math # Include the math module
# import math as m # Include the math module with an alias
# from math import pi # Import the pi constant from the math module
"""
from math import e  # Example of why using from to import parts isn't always the best for example e here is overwritten by our own e variable
a, b, c, d, e = 1, 2, 3, 4, 5
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)
"""

import example

result1 = example.pi
result2 = example.square(3)
result3 = example.cube(3)
result4 = example.circumference(3)
result5 = example.area_of_circle(3)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
