# PROBLEM 1
"""
Write a program to swap the last two elements in a list.
Try this with a list that has all numbers and a list that has words.
"""
# List with numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)
numbers_len = len(numbers)
last_element_index = numbers_len-1
second_last_element_index = numbers_len-2
#print(numbers_len)
temp_var = numbers[second_last_element_index]
numbers[second_last_element_index] = numbers[last_element_index]
numbers[last_element_index] = temp_var
print(numbers)

# List with words
animals = ["ant", "bee", "alligator", "pig", "elephant", "lion", "mouse", "hamster", "bird", "spider"]
print(animals)
animals_len = len(animals)
last_element_index = animals_len-1
second_last_element_index = animals_len-2
#print(animals_len)
temp_var = animals[second_last_element_index]
animals[second_last_element_index] = animals[last_element_index]
animals[last_element_index] = temp_var
print(animals)