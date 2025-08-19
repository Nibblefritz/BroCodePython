class Car:
    # attributes (variables)
    # __init__ is a constructor method (needed to construct objects)
    def __init__(self, model, year, color, for_sale): # self means "this object" or in this case "this car"
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # methods (functions)
    def display_info(self):
        print(f"Car: {self.year} {self.model}: {self.color}, For sale? {self.for_sale}")

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")