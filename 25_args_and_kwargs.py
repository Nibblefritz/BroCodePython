# *args = allows you to pass multiple non-keyword arguments
# **kwargs = allows you to pass multiple keyword arguments (k = keyword)
# *    unpacking operator

# When you pack all the arguments for args you use a tuple
# When you pack all the arguments for kwargs you use a dictionary
# then you use * to unpack the tuple and ** to unpack the dictionary

def add(*args): # 'args' is just a convention, you can name it anything
    total = 0
    for arg in args:
        total += arg   
    return total

print(add(1, 2, 3, 4))
print(add(10, 20, 30, 40, 50))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
        
display_name("Reginald", "Denny", "John", "Doe", "III")
             
# Kwargs example
def print_address(**kwargs):  # 'kwargs' is just a convention, you can name it anything
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for value in kwargs.values():
        print(value, end=" ")
    print()  # New line after printing all values
        
print()

print_address(Street="123 Main St", City="Anytown", State="CA", Zip="12345")