# FOCUS SESSION - 2/19
# ------------------------
# CLASSES AND OBJECTS

################################ Inheritance example #1 #############################################

class Animal:

    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My pet is {self.age} years old and it's name is {self.name}."

    def __repr__(self):
        return f"Object representation: {self.__class__.__name__}(name={self.name!r}, age={self.age})"

    def speak(self):
        pass

class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()} It is a {str(self.breed).lower()}."

    def __repr__(self):
        # [0:-1] strips off last ) so additional attributes can be added
        return f"{super().__repr__()[0:-1]}, breed={self.breed!r})"

class Cat(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()} It is a {str(self.breed).lower()}."

    def __repr__(self):
        return f"{super().__repr__()[0:-1]}, breed={self.breed!r})"

###################################### TEST CODE ##########################################
dog_1 = Dog("Murphy", 10, "Dachshund")
print(dog_1)
print(repr(dog_1))
print("")

dog_2 = Dog("Chipper", 2, "Schnoodle")
print(dog_2)
print(repr(dog_2))
print("")

dog_3 = Dog(name='Sam', age=5, breed='Great Dane')
print(dog_3)
print(repr(dog_3))
print("")

cat_1 = Cat("Luna", 5, "Persian")
print(cat_1)
print(repr(cat_1))
print("")

cat_2 = Cat("Coco", 6, "Persian")
print(cat_2)
print(repr(cat_2))
print("")

animal = Animal("Zeus", 2)
print(repr(animal))


################################ Inheritance example #2 #############################################

class Car:
    def __init__(self, make, model, year, rate, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = rate
        self.mileage = mileage
        self.rented = False
        self.mileage_at_rent = None

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, rate=${self.daily_rate}, mileage={self.mileage})"

    def __str__(self):
        status = "currently rented" if self.rented else "available"
        return f"{self.year} {self.make} {self.model}, ${self.daily_rate}/day, {self.mileage} miles, {status}"

    def rent(self, days):
        if self.rented:
            return f"Sorry, this {self.make} {self.model} is already rented."
        self.rented = True
        self.mileage_at_rent = self.mileage
        total_cost = self.daily_rate * days
        return f"You have rented the {self.make} {self.model} for {days} days. Total cost: ${total_cost}"

    def return_car(self, miles_driven):
        if not self.rented:
            return f"This {self.make} {self.model} is not currently rented."
        self.rented = False
        self.mileage += miles_driven
        miles_driven = self.mileage - self.mileage_at_rent
        self.mileage_at_rent = None
        return f"Thank you for returning the {self.make} {self.model}. You drove {miles_driven} miles."

    def get_rental_info(self):
        if not self.rented:
            return f"This {self.make} {self.model} is available for rent. Current mileage: {self.mileage} miles."
        return f"This {self.make} {self.model} is currently rented. Mileage at rent: {self.mileage_at_rent} miles."


class ElectricCar(Car):
    def __init__(self, make, model, year, rate, mileage, battery):
        super().__init__(make, model, year, rate, mileage)
        # or Car.__init__(self, make, model, year, rate, mileage)
        self.battery = battery

    def __repr__(self):
        return f'Electric{super().__repr__()[0:-1]} battery={self.battery})'


# Example usage
car1 = Car("Toyota", "Corolla", 2022, 50, 15000)
car2 = Car("Ford", "Mustang", 2023, 100, 5000)
car3 = ElectricCar("Tesla", "CyberTruck", 2024, 200, 20000, 84)

print(car1)  # Using __str__
print(repr(car2))  # Using __repr__
print(car3)
print(repr(car3))

print(car1.rent(5))
print(car2.rent(3))
print(car3.rent(7))

print(car1.get_rental_info())
print(car2.get_rental_info())
print(car3.get_rental_info())

print(car1.return_car(500))
print(car1.get_rental_info())

print(car3.return_car(1000))
print(car3.get_rental_info())