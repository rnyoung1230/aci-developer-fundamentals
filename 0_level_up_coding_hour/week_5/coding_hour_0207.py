# CODING HOUR - 02/07

'''
1. Write a function named greet to print a greeting to a person using their name.
The function receives the name of the person from the main program.
In the main program the value of the name variable must be received using the input method.

2. Write a function that will randomly sort a list of 5 students into Hogwarts houses.

3. Write a function that will take two lists as arguments, create a dictionary and return the dictionary.

4. Write a function to check if a given string has identical letters next to each other.

5. Write a function to check if the given list of numbers has duplicates.
'''
from itertools import count


# import random
#
#
# # TASK 1
# def greet(name):
#     print(f"Hello {name}!")
#
# # Test
# entered_name = input("What's your name?\n>")
# greet(entered_name)
# print("---------------------------------------------")
#
# # TASK 2A
# def assign_houses(students_list):
#     hogwarts_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", None]
#
#     random.shuffle(students_list)
#
#     house_assignments = {
#         students_list[x]: hogwarts_houses[x] for x in range(len(students_list))
#     }
#
#     return house_assignments
#
# # Test
# students = ["David", "Bob", "Susan", "Carrie", "Amy"]
# assignments = assign_houses(students)
# print(assignments)
# print("---------------------------------------------")
#
# # TASK 2B
# def choose_house():
#     hogwarts_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     selected_house = random.choice(hogwarts_houses)
#
#     return selected_house
#
# # Test
# students = ["David", "Bob", "Susan", "Carrie", "Amy"]
#
# for student in students:
#     house = choose_house()
#     print(f"{student} is assigned to {house}.")
#
# print("---------------------------------------------")
#
# # TASK 3
# def create_dict(keyes, values):
#     if len(keyes) == len(values):
#         new_dict = {
#             keyes[x] : values[x] for x in range(len(keyes)) # Dictionary comprehension
#         }
#     else:
#         new_dict = {}
#
#     return new_dict
#
# # Test
# list_1 = [1, 2, 3, 4, 5]
# list_2 = ["a", "b", "c", "d", "e"]
# dict = create_dict(list_1, list_2)
# print(dict)
# print("---------------------------------------------")

# TASK 4A
# def check_for_identical(string):
#
#     char1 = ""
#     for char in string:
#         char2 = char
#         if char1 == char2:
#             return True
#         else:
#             char1 = char2
#
#     return False
#
# string1 = "hello"
# print(check_for_identical(string1))
#
# string2 = "world"
# print(check_for_identical(string2))

# TASK 4B
def check_for_identical(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True

    return False

string1 = "hello"
print(check_for_identical(string1))

string2 = "world"
print(check_for_identical(string2))

# Test
print("---------------------------------------------")

# TASK 5
def check_for_dupes(numbers):
    numbers_set = set(numbers)

    if len(numbers) > len(numbers_set):
        return True
    else:
        return False

# Test
numbers_list1 = [1, 2, 3, 4, 5, 4, 6, 7, 0, 1, 3]
print(check_for_dupes(numbers_list1))

numbers_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(check_for_dupes(numbers_list2))