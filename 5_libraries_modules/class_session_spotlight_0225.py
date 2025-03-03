# SPOTLIGHT SESSION - 2/25
# CLASSES AND OBJECTS REVIEW
# ------------------------

class PetShop:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.inventory = []

    def add_customer(self, owner):
        self.customers.append(owner)

    def add_to_inventory(self, pet):
        self.inventory.append(pet)

    def get_pet_names(self):
        return [customer.pet.name for customer in self.customers]

    def get_inventory_species(self):
        return [pet.species for pet in self.inventory]

class Pet:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"My pet is a {self.age}-year old {self.species} named {self.name}."

    def make_sound(self):
        if self.species == "Dog":
            return f"Woof, woof!"
        elif self.species == "Cat":
            return f"Meow, meow!"
        else:
            return f"I don't know what type of animal I am."

class Owner:

    def __init__(self, name, pet_name):
        self.name = name
        self.pet_name = pet_name

    def __str__(self):
        return f"My name is {self.name} and my pet's name is {self.pet_name}."

############################ TEST CODE ############################
fluffy = Pet("Fluffy", "Cat", 3)
buddy = Pet("Buddy", "Dog", 5)
rex = Pet("Rex", "Dog", 2)

john = Owner("John", fluffy)
sarah = Owner("Sarah", buddy)

pet_shop = PetShop("Happy Paws")
pet_shop.add_customer(john)
pet_shop.add_customer(sarah)
pet_shop.add_to_inventory(rex)