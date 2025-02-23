# LABOLOGY SESSION - 2/20
# ------------------------

# Associations and Inheritance

class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles_traveled = 0

    def move_forward(self, miles):
        pass

    def read_miles(self):
        pass

    def info(self):
        pass

    def fill_gas(self):
        pass

class ElectricCar:

    def __init__(self, car, battery):
        self.car = car
        self.battery = battery


################################## TESTING CODE #########################################

car_1 = Car("Toyota", "4-Runner", 2024, "Black")
electric_car_1 = ElectricCar(car_1, 120)  #kilowatt hours (120 kWh)
