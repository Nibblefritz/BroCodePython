# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book, car
#          you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
from car import Car # import the Car class from our car.py file
        
car1 = Car("Toyota Camry", 2020, "Blue", for_sale=True)
car2 = Car("Honda Accord", 2019, "Red", for_sale=False)
car3 = Car("Ford Mustang", 2021, "Black", for_sale=True)
car4 = Car("Chevrolet Camaro", 2025, "White", for_sale=False)

#print(car1.model)
#print(car1.year)
#print(car1.color)
#print(car1.for_sale)

car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()

car1.drive()
car2.drive()
car3.drive()
car4.drive()

car1.stop()
car2.stop()
car3.stop()
car4.stop()