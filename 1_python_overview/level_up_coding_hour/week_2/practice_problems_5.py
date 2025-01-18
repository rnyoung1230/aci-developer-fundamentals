# PROBLEM 5
'''
Using a while loop, print all even numbers within the range 20 to 80, inclusive of both these numbers.
'''

# INITIALIZE PROGRAM
range_start = 20
range_stop = 81
number = range_start

# RUN PROGRAM
# Print only the even numbers in a given range using a WHILE loop
while number in range(range_start, range_stop):
        print(number)
        number += 2 # Increment number by 2 so it skips ODD numbers and remains EVEN

# END PROGRAM
# Say good-bye
print("Good-bye!")

