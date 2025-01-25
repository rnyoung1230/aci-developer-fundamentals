# PROBLEM 2
"""
Write a program to find the second largest number in a list of numbers.
Start here: Try to break down how you would logically find the second
largest number in the list [12, 45, 33, 89] without having to write a program for it.
"""
numbers = [1, -99, 0, 34, 22, 600, 101, 345, 120, 102, 346, -45, 6]

# Print the initial list of numbers
print(numbers)

# Sort the numbers in descending order
numbers.sort(reverse = True) # The sort is done in place on the list
print(numbers)

# Print the second largest number
print(f"The second largest number is: {numbers[1]}")