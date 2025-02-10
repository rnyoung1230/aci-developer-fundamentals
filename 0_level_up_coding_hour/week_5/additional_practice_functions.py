# Additional functions practice
'''
1. Write a function named rec_area to calculate the area of a rectangle
using the formula length*width. The length and width values of 97, 32
are sent to the function from the main program. The function should
print the area of the given rectangle, not return the value.

2. Write a function that receives a list of numbers from the main program
and print the length of the list. Hint – treat the list just as a single “thing”
being sent to a function. Once the function receives it, use the length
function on the list to print the length of the list.

3. Write a function that will add any 5 numbers and return the result back
to the main program. You can use *args to receive the 5 numbers in
the function.

4. Write a function that will take two lists as input, create a dictionary and
return the dictionary back to the main program. Use the two lists below
to check your answer:
    fruits = ["apple", "banana", "orange", "grape", "mango"]
    colors = ["red", "yellow", "orange", "purple", "green"]

5. In the main part of your program, prompt user to choose a color from
the given choices: Red, Blue, Green or Purple. Write a function that will
receive as input the user choice of color and will return:
    a. “Sith” if the color choice is Red
    b. “Jedi” if the color is green, blue or purple

In the main part of the program, use the word returned to print a statement
“You may be a ___”
'''

# Exercise 1 - Calculate area of a rectangle
def calculate_area_rec(length, width):
    area = length * width
    print(f"The area of the rectangle is: {area}.")

l = 97
w = 32

calculate_area_rec(l, w)

print("-------------------------------------------------------")

# Exercise 2 - Print the length of received numbers list
def determine_list_length(numbers_list):
    print(f"The length of this list is: {len(numbers_list)}.")

numbers_1 = [1, 2, 4, 5, 6, 7, 8]
determine_list_length(numbers_1)

numbers_2 = [33, 22, 45, 100, 3, 0, 12, 21, 22, -2, 7000]
determine_list_length(numbers_2)

print("-------------------------------------------------------")

# Exercise 3 - Add numbers
def add_numbers(*numbers):
    return sum(numbers)

summed_numbers = add_numbers(1, 3, 7, 10, 25)
print(f"The sum of your numbers is: {summed_numbers}.")

print("-------------------------------------------------------")

# Exercise 4 - Create a dictionary from two lists
def create_dict(keyes, values):
    if len(keyes) == len(values):
        new_dict = {
            keyes[x] : values[x] for x in range(len(keyes)) # Dictionary comprehension
        }
    else:
        new_dict = {}

    return new_dict

# Test
fruits = ["apple", "banana", "orange", "grape", "mango"]
colors = ["red", "yellow", "orange", "purple", "green"]

fruits_colors = create_dict(fruits, colors)
print(fruits_colors)

print("-------------------------------------------------------")

# Exercise 4B - Create a list from a given input of numbers
def create_list(*numbers):
    new_list = [x for x in numbers] # List comprehension
    return new_list

number_list = create_list(1, 3, 7, 10, 25)
print(number_list)

print("-------------------------------------------------------")

# Exercise 5 - Create a list from a given input of numbers
color_list = ["red", "blue", "green", "purple"]

def determine_side_of_the_force(color):
    if color == "red":
        return "Sith"
    else:
        return "Jedi"

color_choice = input(f"Please choose one of these colors: {color_list}\n>")

force_side = determine_side_of_the_force(color_choice)
print(f"You may be a {force_side}.")

