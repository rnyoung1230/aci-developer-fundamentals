# WEEK 7 - ASSESSMENT

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

p1 = Person("Mary", 44, "US")
print(p1)
print(vars(p1)) # Prints a dictionary object containing the attributes

print(dir(p1))