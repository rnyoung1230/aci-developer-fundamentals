# PROBLEM 1
'''
Write a program that prompts user to enter numbers, one at a time until the user wants to quit.
When the user is done, find and print the average of the numbers entered by the user.
'''

# INITIALIZE PROGRAM
entry_count = 0
sum_entered_numbers = 0
wants_to_play = True

# RUN PROGRAM
while wants_to_play:
    # Ask user to enter a number, add that number to a running total,
    # and increase the number of entries count by 1
    entered_number = int(input("Please enter a number.\n>"))
    sum_entered_numbers += entered_number
    entry_count += 1

    # Ask user if they'd like to enter another number
    # If they answer N, set the wants_to_play flag to False. Otherwise, continue
    continue_game = input("Enter another number? Y or N\n>")
    if continue_game == "N":
        wants_to_play = False
    else:
        continue

# END PROGRAM
# Compute the average of the entered numbers
avg_entered_numbers = sum_entered_numbers/entry_count

# Print the number of entries, the sum of entered numbers, and their average
print(f"Number of entries: {entry_count}\nSum of entered numbers: {sum_entered_numbers}"
              f"\nAverage of entered numbers: {avg_entered_numbers}")

# Say good-bye
print("Good-bye!")

