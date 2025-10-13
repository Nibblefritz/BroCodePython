class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is asleep.")
        
class Dog(Animal): #Dog is a child class of Animal
    def speak(self):
        print("Woof!")

class Cat(Animal): #Cat is a child class of Animal
    def speak(self):
        print("Meow!")

class Mouse(Animal): #Mouse is a child class of Animal
    def speak(self):
        print("Squeak!")