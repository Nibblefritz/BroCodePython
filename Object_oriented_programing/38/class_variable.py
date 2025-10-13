# Class variables = attributes that are shared by all instances of a class
#                   Class variables are not as frequently used as instance variables
#                   Use class variables when you want to have a variable that is the same for every instance
#                   Ex. car has 4 wheels, 1 steering wheel, and 1 engine

from car import Car # import the Car class from our car.py file     
from student import Student # import the Student class from our student.py file   

car1 = Car("Toyota Camry", 2020, "Blue", for_sale=True)
car2 = Car("Honda Accord", 2019, "Red", for_sale=False)
car3 = Car("Ford Mustang", 2021, "Black", for_sale=True)
car4 = Car("Chevrolet Camaro", 2025, "White", for_sale=False)

car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()

car1.drive()
car4.drive()
car1.stop()
car4.stop()

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 21)

student1.display_info()
student2.display_info()
student3.display_info()

print(f"Total Students: {Student.num_students}")
print(f"Graduation Year: {Student.graduation_year}")
