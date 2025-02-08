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
#
# """
#  Assign value of 5 to global variable 'x'
# """
# x = 5
#
# def my_function():
#   """
#   Define a local variable 'x' with a value of 5,
#   then print it.
#   """
#   y = 10
#
#   print('Local', y)
#
# my_function() # output: Local 5
#
# # try to access variable outside of function
# print('Global', x) #output: Global 5

# Arguments and parameters
# def my_function(food = "burgers"):
#   print("My favorite food is " + food)
#
# """
# Print a message about the programmer's favorite food.
# """
# # call function with 'pizza' as an argument.
# my_function("pizza")
#
# # call function with 'tacos' as an argument.
# my_function("tacos")
#
# # call function with no argument.
# my_function()

# Positional arguments
def my_friend(friend_name, friend_city):
  """
  Take in two parameters, `friend_name` and `friend_city`,
  and print a message stating your friend with name `friend_name`
  lives in `friend_city`.
  """
  print(f"My friend {friend_name} lives in {friend_city}.")


my_friend('Jane', 'New York')

# Keyword arguments
def my_friend(friend_name, friend_city):
  print(f"My friend {friend_name} lives in {friend_city}.")

my_friend(friend_city='New York', friend_name='Jane')

# Arbitrary keyword arguments
def user_info(**kwargs):
  """
  Take in keyword arguments as inputs and print
  out the key-value pairs.
  """
  for key, value in kwargs.items():
    print(f"{key}: {value}")


user_info(Name="Jane", Age=33, City="Paris", Language="French")