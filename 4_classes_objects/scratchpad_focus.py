# FOCUS SESSION - 2/12
# ------------------------

# CLASSES AND OBJECTS

################################ DOG EXAMPLE #############################################

class Dog:
    # class variables and methods
    current_year = 2025

    # instance variables and methods
    def __init__(self, name, breed, color, birth_year):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = Dog.current_year - birth_year

    def bark(self):
        print(f"{self.name} says woof, woof!")

    def print_info(self):
        print(f"{self.name} is a {self.color} {self.breed} who is {self.age} years old.")

my_dog = Dog("Murphy", "Dachshund Terrier", "black/tan", 2014)
#print(dir(my_dog))
#print(f"I have a {my_dog.color} {my_dog.breed} named {my_dog.name}. He's {my_dog.age} years old.")
my_dog.print_info()
my_dog.bark()

your_dog = Dog("Chipper", "Schnoodle", "brown", 2022)
your_dog.print_info()
your_dog.bark()

print("----------------------------------------------------------------------------------")
################################ CAR EXAMPLE #############################################

class Car:
    # class variables and methods

    # instance variables and methods
    def __init__(self, year, make, model, trim_level):
        self.year = year
        self.make = make
        self.model = model
        self.trim_level = trim_level
        self.mileage = 0

    def print_info(self):
        print(f"My car is a {self.year} {self.make} {self.model} {self.trim_level} with {self.mileage} miles.")

    def record_trip(self, miles_driven):
        self.mileage += miles_driven

    def honk_horn(self):
        print("Beep beep!")

my_car = Car(2021, "Volkswagen", "Atlas Cross Sport", "3.6L V6 SEL")
my_car.print_info()
my_car.record_trip(150)
my_car.honk_horn()
my_car.print_info()
