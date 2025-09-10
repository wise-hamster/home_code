class Car():
    def __init__(self, model,year,coast):
        self.model = model
        self.year = year
        self.coast = coast
        self.wheels = 4

    def description (self):
        print(f'Model: {self.model}, Year: {self.year}, Coast: {self.coast}, Wheels: {self.wheels}')

class Truck(Car):
    def __init__(self, model, year, coast):
        super().__init__(model, year, coast)
        self.wheels = 8

volvo = Truck ('s929','2001', '100000')

volvo.description()