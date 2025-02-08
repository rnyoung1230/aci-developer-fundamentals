# WEEK 5 - FUNCTIONS

# What are functions?
# def my_function():
#
#     """Print a welcome message for users visiting the website."""
#
#     print("Welcome to our website!")
#
# my_function()

# Math functions
# numbers = [2, 5, 9, 8, 3, 20]
#
# min_val = min(numbers)
# max_val = max(numbers)
#
# print("Minimum value is:", min_val)
# print("Maximum value is:", max_val)

# Variable scope
# def my_function():
#     """
#     Assign a value of 5 to a local
#     variable 'x' and print its value.
#     """
#     x = 5
#     print('Local', x)
#
# my_function() # output: Local 5
#
# # try to access variable outside of function
# print(x) # output: error
#

"""
 Assign value of 5 to global variable 'x'
"""
x = 5

def my_function():
  """
  Define a local variable 'x' with a value of 5,
  then print it.
  """
  y = 10

  print('Local', y)

my_function() # output: Local 5

# try to access variable outside of function
print('Global', x) #output: Global 5