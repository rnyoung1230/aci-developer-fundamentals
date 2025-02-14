# LABOLOGY SESSION - 2/13
# ------------------------

# Exercise 1: Create a superhero class
'''
Task 1: Create an __init__ method that takes name, power, and costume_color as parameters,
and sets energy attribute to 100 and is_disguised attribute to True
'''
class Superhero:
    # class variables and methods


    # instance variables and methods
    def __init__(self, name, power, costume_color):
        self.name = name
        self.power = power
        self.costume_color = costume_color
        self.energy_level = 100
        self.is_disguised = True

    def print_info(self):
        print(f"Name: {self.name}\n"
              f"Power: {self.power}\n"
              f"Costume color: {self.costume_color}\n"
              f"Energy level: {self.energy_level}\n"
              f"Disguised: {self.is_disguised}")

    def use_power(self):
        if self.energy_level > 0:
            self.energy_level -= 10
            print(f"{self.name}'s remaining energy is {self.energy_level}.")
        else:
            print(f"{self.name}'s energy is depleted. He needs to rest!")

    def rest(self, minutes_of_rest):
        for each_minute in range(0, minutes_of_rest):
                if self.energy_level < 100:
                    self.energy_level += 1
                else:
                    continue

        print(f"{self.name}'s energy level is now {self.energy_level}.")

    def change_costume(self):
        if self.is_disguised == True:
            self.is_disguised = False
            print(f"{self.name} changed into their superhero outfit!")
        else:
            self.is_disguised = True
            print(f"{self.name} is back in their civilian clothes.")

################################# CREATING INSTANCES ############################################

superman = Superhero("Superman", "flying", "red and blue")
superman.print_info()
print("---------------------------------------------------------")

superman.use_power()
superman.rest(7)
superman.change_costume()
superman.change_costume()

print("---------------------------------------------------------")

hulk = Superhero("Hulk", "strength", "green")
hulk.print_info()
