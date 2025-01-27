# FOCUS SESSION - 1/23
# --------------------

# Basic list example
# house_pets = ["dog", "cat", "hamster", "bird"]
#
# for pet in house_pets:
#     print(pet)

# # Slicing examples
# my_list = ["first", "second", "third", "fourth"]
#
# # print single element using the positive index
# print(my_list[1])
#
# # print single element using the negative index
# print(my_list[-1])
#
# # print range of values using the slice operator
# print(my_list[1:3])

# Dictionary examples
# inventory = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2
# }
#
# print (inventory)
#
# inv_with_dups = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2,
#     "apples": 1
# }
#
# print (inv_with_dups)

# Accessing items in a Dictionary
# inventory = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2,
#     "dates": 10
# }
#
# num_dates = inventory["dates"]
#
# num_apples = inventory["apples"]
#
# print (f"There are {num_dates} dates and {num_apples} apples in the inventory.")

# Tuples
# new_tuple = ("zero", "one", "two", "three", "four")
#
# print(new_tuple[0])
# print(new_tuple[-1])
#
# names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]
#
# for i in range(len(names)):
#     print (f"{names[i]} is at position {i}")
#
# sales_wk1 = {
#     "Monday": 10,
#     "Tuesday": 10,
#     "Wednesday": 5,
#     "Thursday": 5,
#     "Friday": 15,
#     "Saturday": 20,
#     "Sunday": 15
# }
#
# total_sales = 0
#
# for k in sales_wk1:
#     total_sales += sales_wk1[k]
#
# print (total_sales)
#
# # initializes colors list
# colors = ["orange", "yellow", "green", "blue"]
#
# # adds purple to the end of the colors list
# colors.append("purple")
#
# # inserts new colors at the specified position in the colors list
# colors.insert(2, "red")
# colors.insert(4, "black")
#
# print(colors)
#
# # extend the list even further
# more_colors = ["silver", "muave"]
# colors += more_colors
# print(colors)
#
# pets = ["dog", "cat", "hamster", "iguana", "goldfish"]
#
# # pop last element
# lost_pet = pets.pop()
#
# print ("pets after pop() is:", pets)
# print ("lost_pet is:", lost_pet)
#
# # pop specific element
# lost_pet = pets.pop(0)
#
# print ("pets after pop(0) is:", pets)
# print ("lost_pet is:", lost_pet)
#
# pets = ["dog", "cat", "hamster", "iguana", "goldfish"]
# print(pets)
#
# # remove
# pets.remove("hamster")
#
# print ("pets after remove('hamster') is", pets)
#
# pets.remove(pets[0])
#
# print ("pets after remove(pets[0]) is", pets)
#
# # clear
# pets.clear()
#
# print("pets after clear() is", pets)

# sort alphanumeric string
# my_list = ["car", "boat", "Truck", "1", "Car", "-1", "ZZ_Top", "b00m", "T3p"]
# my_list.sort()
# print("Mixed case alphanumeric sort:", my_list)
#
# # sort with optional reverse argument
# my_list.sort(reverse=True)
# print("Sort with optional reverse argument:", my_list)
#
# # sort using reverse method
# groceries = ["apples", "berries", "cabbage"]
# groceries.reverse()
# print("groceries after reverse()", groceries)

# Tripe quotes used within a variable assignment allow you to break lines
# ''' = doc string
# message = '''
# This is a multi line string.
# It is cool to use and avoid having to
# scroll across the screen to read everything.
# '''
# print(message)
# temp = list(message.split())
# print(temp)

# Dictionary practice
# dict = {} # empty curly braces ALWAYS equate to a Dictionary (not a Set)
# names_ages = {"Tim" : 20, "Sally": 34, "Mike": 55} # names and ages
# print(names_ages)
# names_ages["Tim"] += 5
# print(names_ages)
#
# # del keyword is ONE way to remove a key-value pair from a dict
# del names_ages["Tim"]
# print(names_ages)

# Create a dictionary with fruit names as keys and color as their values
# fruits = {
#     "Banana": "Yellow",
#     "Apple": "Red",
#     "Pear": "Green",
#     "Lime": "Green",
#     "Lemon": "Yellow",
#     "Blueberry": "Blue",
#     "Orange": "Orange"
# }
# print(fruits)
#
# # Create a dictionary with 3 countries and their capitals
# countries_cap = {
#     "USA": "Washington D.C.",
#     "France": "Paris",
#     "Mexico": "Mexico City"
# }
# print(countries_cap)

# Looping through iterables
#Lists
# fruits = ["apples", "pears", "bananas", "blueberries", "limes"]
# for fruit in fruits:
#     print(fruit)
#
# print("------------------------")
#
# for i, v in enumerate(fruits): # enumerate provides easy way of getting the index and value from a list
#     print(i, v)
#
# for index in range(len(fruits)):
#     print(index + 1, fruits[index])

# numbers = [1, 2, 3, 4, 2, 3, 6, 7, 3, 1, 9]
# print(len(numbers))
# print(numbers)
#
# numbers_set = set(numbers) # casting a list to a set automatically removes any duplicates
# print(len(numbers_set))
# print(numbers_set)

# Create a dictionary with fruit names as keys and quantity as their values
# fruits = {
#     "Banana": 5,
#     "Apple": 13,
#     "Pear": 4,
#     "Lime": 2,
#     "Lemon": 2,
#     "Blueberry": 50,
#     "Orange": 6
# }
# #print(fruits)
#
# for i, v in enumerate(fruits): # gives you the index for each key
#     print(i, v)
#
# print("------------------------")
#
# for k in fruits:
#     print(k, fruits[k]) # gives you each key and its value
#
# print("------------------------")
#
# for k, v in fruits.items(): # gives you each key and its value using iterable method
#     print(k, v)

# List methods
pets = ["dog", "cat", "hamster", "iguana", "goldfish"]

# remove
pets.remove("hamster")

print ("pets after remove('hamster') is", pets)

pets.remove(pets[0])

print ("pets after remove(pets[0]) is", pets)

# clear
pets.clear()

print("pets after clear() is", pets)