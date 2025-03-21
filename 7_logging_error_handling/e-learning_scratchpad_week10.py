# WEEK 10 - LOGGING AND ERROR HANDLING

# import logging
#
# logging.basicConfig(level=logging.DEBUG) # Default logging level is WARNING
#
# logging.debug("This is a DEBUG message.")
# logging.info("This is a INFO message.")
# logging.warning("This is a WARNING message.")
# logging.error("This is a ERROR message.")
# logging.critical("This is a CRITICAL message.")

# BASIC LOGGING PRACTICE
# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
#
# def add_numbers(x, y):
#     """Adds two numbers and returns the sum"""
#     if type(x) != type(y):
#         logging.warning("Args may not be compatible")
#
#     if type(x) == str and type(y) == str:
#         logging.error("Result is concatenated string")
#
#     if (type(x) != type(y)) and (type(x) in (bool, str) or type(y) in (bool, str)):
#         logging.critical("Result '' cannot be processed")
#         return ""
#
#     logging.debug("x = {}, y = {}".format(x, y))
#     logging.info("Function returns {}".format(x + y))
#     return x + y
#
#
# def main():
#     add_numbers(1, 2)
#
#
#
#
# if __name__ == "__main__":
#     main()

# WRITING LOG FILES PRACTICE
#import logging
#
# logging.basicConfig(filename="example.log", filemode="w", level=logging.DEBUG)
#
# logging.debug("This is a DEBUG message.")
# logging.info("This is a INFO message.")
# logging.warning("This is a WARNING message.")
# logging.error("This is a ERROR message.")
# logging.critical("This is a CRITICAL message.")
#
# import logging
#
# logging.basicConfig(filename="example.log",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     level=logging.DEBUG)
#
# logging.debug("This is a DEBUG message.")
# logging.info("This is a INFO message.")
# logging.warning("This is a WARNING message.")
# logging.error("This is a ERROR message.")
# logging.critical("This is a CRITICAL message.")

# Challenge: Using the logging module
# import logging
#
# logging.basicConfig(filename="messages.log", filemode="w", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
#
# def process_data():
#     logging.info("process_data() is beginning...")
#
#     entered_numbers = input("Please enter a list of numbers...each separated by a comma.\n>")
#     if "," not in entered_numbers:
#         logging.error("User did not enter a comma separated list of values.")
#         return "You did not enter comma separated values. Try again."
#     numbers_list_str = entered_numbers.split(sep=",")
#     logging.info("You entered {} numbers.".format(len(numbers_list_str)))
#
#     numbers_list_int = []
#     for number in numbers_list_str:
#         numbers_list_int.append(int(number))
#     logging.info("List of numbers: {}".format(numbers_list_int))
#     return numbers_list_int
#
# if __name__ == "__main__":
#     result = process_data()
#     print(result)

# Cleaning up code practice --> try/except blocks
# def add_numbers(x, y):
#     """Adds two numbers and returns the sum"""
#     try:
#         return x + y
#     except:
#         return f"Cannot add {type(x)} and {type(y)}"
#
# print(add_numbers("a", 3))

# Planning for exceptions
# def divide_numbers():
#     try:
#         dividend = int(input("Enter the integer to divide: "))
#         divisor = int(input("Enter the integer to divide by: "))
#         return dividend / divisor
#
#     except Exception as e:
#         print(type(e))
#         print(e)
#
# print(divide_numbers())

# Catching specific exceptions
'''
The following example includes three except blocks. The first is meant to catch any ValueError that is raised.
The second catches any instances of a ZeroDivisionError. The third except clause catches any other error-types
and prints the associated exception and message.
'''
# def divide_numbers():
#
#     try:
#         dividend = int(input("Enter the integer to divide: "))
#         divisor = int(input("Enter the integer to divide by: "))
#         return dividend/divisor
#     except ValueError:
#         print ("Enter an integer.")
#     except ZeroDivisionError:
#         print ("Cannot divide by zero.")
#     except Exception as e:
#         print (type(e))
#         print (e)
#
# print(divide_numbers())

# The finally block
try:
    file = open("myfile.txt", "r")
    # Perform some operations on the file
except FileNotFoundError:
    print("The file could not be found.")
except IOError:
    print("An error occurred while reading the file.")
else:
    print("File contents:", file.read())
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")
