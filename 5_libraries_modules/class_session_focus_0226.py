# FOCUS SESSION - 2/26
# LIBRARIES AND MODULES
# ------------------------

# The Math module
# import math
#
# # Provides brief overview of the math module
# print(math.__doc__)
#
# # Return and print a list of all the functions and variables inside the math module
# for x in dir(math):
#     print(x)

# This signifies the start of your program's execution code
# if __name__ == '__main__':
#     pass

# The Datetime module
from datetime import datetime
from datetime import date
from datetime import timedelta

if __name__ == '__main__':
    today = datetime.now()
    print(today)
