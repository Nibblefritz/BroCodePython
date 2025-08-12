# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local > Enclosing > Global > Built-in

# Variables declared within a function are in the local scope
# functions can't see inside other functions but they can see in their own functions
# This is why we pass arguments into other functions so they can see those items

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)
    
func1()  # prints 1
func2()  # prints 2

# Enclosing variables
def func3():
    x = 1
    
    def func4():
        # x = 2 >> Order of operations, if this is here then the print will be 2 not the 1 from outside
        print(x) # uses the enclosing x = 1
    func4()
    
func3()  # prints 1

# Setting a global variable for x it will be used anywhere ther eis no Enclosed or local variables of x
x = 3

def func5():
    print(x)
def func6():
    print(x)
func5()  # prints 3
func6()  # prints 3

# Built-in variable
from math import e

def func7():
    print(e)  # prints 2.718281828459045, the built-in e from the math module   
    
# e = 3 >> This would overwrite the built-in 'e' that we imported, because global takes precedence over built-in
func7()