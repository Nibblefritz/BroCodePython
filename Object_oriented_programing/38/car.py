class Car:
    wheels = 4 # class variable (all cars have 4 wheels)

    def __init__(self, model, year, color, for_sale): # constructor
        self.model = model          # instance variable
        self.year = year            # instance variable
        self.color = color          # instance variable
        self.for_sale = for_sale    # instance variable

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {self.for_sale}, Wheels: {Car.wheels}")

    def drive(self):
        print(f"The {self.model} is now driving.")

    def stop(self):
        print(f"The {self.model} has stopped.")