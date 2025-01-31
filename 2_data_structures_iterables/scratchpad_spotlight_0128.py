# coding examples from 1/28 spotlight session
# built-in functions for Lists
import random

numbers = []
for n in range(20):
    #print(n)
    numbers.append(random.randint(10, 99))

print(numbers)
numbers_set = set(numbers) # removes any duplicates
sorted_numbers = sorted(numbers_set)
print(sorted_numbers)

