# PROBLEM 3
'''
Ask the user for a number and print its multiplication table.
'''

# INITIALIZE PROGRAM

# RUN PROGRAM
# Ask user to enter a number
entered_number = int(input("Please enter a number.\n>"))

# Output the number's multiplication table, row by row
for number in range(1, 11):
    product = entered_number * number
    print(f"{entered_number} * {number} = {product}")

# END PROGRAM
# Say good-bye
print("Good-bye!")

