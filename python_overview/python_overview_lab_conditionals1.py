# TASK 2A: CONDITIONALS PRACTICE
if 's' in 'String':
    print("Found!")

if 's' not in "String":
    print("Sorry!")
    
statement = "The Cat in the Hat is a children's book."
letter = input("Enter which letter you are searching for:\n>")

scrubbed_statement = statement.strip().lower()
if letter in scrubbed_statement:
    print(f"Found the letter \"{letter}\"!")
# Add a condition based on using the not in operator.
elif letter not in scrubbed_statement:
    print(f"Could not find the letter \"{letter}\"!")
    
# TASK 2B: CONDITIONALS PRACTICE
'''
Ask the user to input any number. 
Use conditions to determine if the user-entered number is even or odd.
Print if the number is even or if the number is odd.

Hint: a number is even if it is completely divisible by 2. In other words, 
when you divide a number by 2, if the remainder is 0, it is an even number. If not, it is an odd number.
'''

number = int(input("Please enter a whole number.\n>"))

if number % 2 == 0:
    print(f"You entered {number}, which is even." )
else:
    print(f"You entered {number}, which is odd." )
    