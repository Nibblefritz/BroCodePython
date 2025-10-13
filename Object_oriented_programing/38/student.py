class Student:
    num_students = 0  # class variable to keep track of number of students
    graduation_year = 2024  # class variable for graduation year
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
