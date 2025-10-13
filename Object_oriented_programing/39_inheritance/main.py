# Inheritance = when a class (child class) inherits the attributes and methods from another class (parent class)
#               = helps to reuse code, makes it easier to create and maintain an application
#               = also used to make relationships between classes
#               = Ex. Animal (parent class) -> Dog (child class)
#               = Ex. Animal (parent class) -> Cat (child class)
#               = Ex. Animal (parent class) -> Mouse (child class)
#               = these are also known as sub and super classes

from animal import Dog, Cat, Mouse # import the Dog, Cat, and Mouse classes from our animal.py file

dog = Dog("Scooby Doo")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.name)
print(mouse.name)

print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
cat.speak()
mouse.speak()