# PROBLEM 2
'''
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''

# INITIALIZE PROGRAM
sum_even_numbers = 0
sum_odd_numbers = 0

# RUN PROGRAM
for number in range(0, 101):
    #Is number even or odd?
    if number % 2 == 0: # number is even
        sum_even_numbers += number
    else: # number is odd
        sum_odd_numbers += number

# END PROGRAM
# Print the sum of all evens and sum of all odds
print(f"Sum of even numbers: {sum_even_numbers}\nSum of odd numbers: {sum_odd_numbers}")

# Say good-bye
print("Good-bye!")

