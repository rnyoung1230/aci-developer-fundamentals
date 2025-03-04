# WEEK 8 - LIBRARIES AND MODULES
# from my_module import add_numbers
#
# result = add_numbers(100, 3, 4, 5)
# print(result)
#
# # The following code imports the math module and prints the directory
# # of functions and attributes available in the math module.
#
# import math
#
# for x in dir(math):
#     print(x)
#
# # The __doc__ attribute contains a documentation string, or docstring, that provides an overview of the module.
# print(math.__doc__)

# Challenge 1: calculating surface area
# from math import pi
#
# def calculate_surface_area(radius):
#     surface_area = 4 * (pi * (radius ** 2)) # Surface Area = 4πr2
#     return round(surface_area, 4)
#
# #################### TEST CODE ####################
# print(calculate_surface_area(1))
# print(calculate_surface_area(2))
# print(calculate_surface_area(3))
#
# # Creating date objects
# import datetime
#
# today = datetime.date.today()
#
# print ("This is a date object:", today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday()) # weekday returns the day of week as a number
#                        # Monday  is 0, Tuesday is 1, and so on.
#
# # Creating datetime objects
# import datetime
#
# now = datetime.datetime.now()
#
# print ("This is a datetime object:", now)  # This is the datetime object
# print (now.year) # prints only the year from the object
# print (now.month) # prints only the month from the object
# print (now.day) # prints only the day, as a number, from the object
# print (now.hour) # prints only the hour (in UTC time)
# print (now.minute) # prints only the minute
# print (now.second) # prints only the second
#
# # Find the delta between two datetime objects
# import datetime
#
# past_date = datetime.datetime(2015, 3, 14, 9, 26)
# #print (past_date)
#
# current_date = datetime.datetime.now()
#
# delta = current_date - past_date
#
# print (f"The difference between {current_date} and {past_date} is {delta}.")
#
# # Formatting dates and time
# # Python Date Format Codes located here https://www.w3schools.com/python/gloss_python_date_format_codes.asp
# from datetime import datetime
#
# #date_string = "03/04/2025"
# #date_format = "%m/%d/%Y"
# date_string = "12 May, 2222"
# date_format = "%d %B, %Y"
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)
#
#
# date_string = "Mar 10 2020 08:27"
# date_format = "%b %d %Y %H:%M"
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)

# Challenge 2: next Friday
import datetime

def get_next_friday(year, month, day):
    start_date = datetime.date(year, month, day)
    start_day_of_week = start_date.weekday()
    # days_to_next_friday = 6
    #
    # if start_day_of_week == 6:
    #     days_to_next_friday = days_to_next_friday - 1
    # elif start_day_of_week <= 4:
    #     days_to_next_friday = 4 - start_day_of_week
    #
    # return days_to_next_friday
    if start_day_of_week <= 4:
        days_to_friday = 4 - start_day_of_week
    else:
        days_to_friday = 11 - start_day_of_week

    return days_to_friday


################## TEST CODE ##################
result_1 = get_next_friday(2023, 7, 28)
print(result_1)

result_2 = get_next_friday(2023, 7, 29)
print(result_2)

result_3 = get_next_friday(2023, 8, 2)
print(result_3)