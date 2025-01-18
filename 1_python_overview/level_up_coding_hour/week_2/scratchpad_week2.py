print("Level Up Coding Hour: Week 2")

# Task 1 - Use for loop to iterate 0 to 100 and print sum of all numbers
# number_sum = 0
# for number in range(0,101):
#     number_sum += number
#
# print(number_sum)
# print("--------------------")

# Task 2 - Write a program that will prompt users to enter numbers, one at a time until the user wants to quit.
# From the numbers entered, find max and min of all numbers entered by the user.
# wants_to_play = True
# entered_numbers = []
#
# while wants_to_play:
#     entered_number = int(input("Please enter a number\n>"))
#     print(f"You entered {entered_number}.")
#     entered_numbers.append(entered_number)
#     print(entered_numbers)
#
#     wants_to_quit = input("Do you want to quit? Please enter Y or N.\n>")
#
#     if wants_to_quit == "Y":
#         max_number = max(entered_numbers)
#         min_number = min(entered_numbers)
#
#         print(f"The max number you entered was {max_number}")
#         print(f"The min number you entered was {min_number}")
#
#         wants_to_play = False
#     else:
#         continue
#
# print("Thanks for playing.")
# print("--------------------")

# Task 3 - The Fitness Challenge Counter (see OneNote for full description)
message1 = "The daily push-up count for day{} is {}."
message2 = "The total number of push-ups done over {} day(s) is {}."

num_days_to_track = int(input("For how many days do you want to track your number of push-ups?\n>"))
num_pushups_day1 = int(input("How many push-ups do you want to start with?\n>"))
num_pushups_increase = int(input("How many push-ups will you increase by each day?\n>"))
daily_pushup_count = 0
total_pushup_count = 0

for day in range(1, num_days_to_track + 1):
    if day == 1:
        daily_pushup_count = num_pushups_day1
        print(message1.format(day,daily_pushup_count))
    else:
        daily_pushup_count += num_pushups_increase
        print(message1.format(day, daily_pushup_count))

    total_pushup_count += daily_pushup_count

print(message2.format(num_days_to_track, total_pushup_count))

# print("--------------------")


