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

# TASK 1
def greet(name):
    print(f"Hello {name}!")

# Test
entered_name = input("What's your name?\n>")
greet(entered_name)
print("---------------------------------------------")

# TASK 2
def sort(*students):
    pass

# Test
# students = ["David", "Bob", "Susan", "Carrie", "Amy"]
# print(f"Before sort: {students}")
# sorted_students = sort(students)
# print(f"After sort: {sorted_students}")
# print("---------------------------------------------")

# TASK 3
def create_dict(keyes, values):
    if len(keyes) == len(values):
        new_dict = {
            keyes[x] : values[x] for x in range(len(keyes)) # Dictionary comprehension
        }
    else:
        new_dict = {}

    return new_dict

# Test
list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]
dict = create_dict(list_1, list_2)
print(dict)
print("---------------------------------------------")

# TASK 4
def something():
    pass

# Test
print("---------------------------------------------")

# TASK 5
def something_else():
    pass

# Test