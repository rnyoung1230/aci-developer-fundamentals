# TASK 3A: LOOPS
'''
Identify which loop would work best for this situation: 
You are learning how to play basketball and practicing free-throw shots. 
You make three unsuccessful attempts, and on the fourth attempt you make the shot. 
Once you have identified the loop, write a program that will print a statement every time 
your free throw attempt fails and when the attempt was successful.
'''
for number in range(1,5):
    if number < 4:
        print(f"Sorry, attempt {number} was unsuccessful. Please try again.")
    else:
        print(f"Congrats! You made it on attempt {number}.")


# TASK 3B: LOOPS
'''
Using a for loop, print the numbers starting from 1 to 10.
'''
for number in range(1,11):
    if number <= 10:
        print(f"Number: {number}")
    else:
        break

# TASK 3C: LOOPS
'''
Using a while loop, print numbers from 10 to 1.
'''
number = 10
while number > 0:
    print(f"Number: {number}")
    number -= 1

# TASK 3D: LOOPS
'''
You are creating a cryptic name generator, and the first step in this process is to interleave 
the user’s first name with a number after every character. Here are the steps to create this:
- Ask user for their first name
- Create a cryptic_name variable with an empty string
- Use a for loop to iterate through the user’s name
- In each iteration of the loop, ask the user to input a number. 
- This number should be appended after the character of the user’s first name and appended into the new cryptic_name variable.
'''
first_name = input("Please provide your first name.\n>")
print(f"First Name: {first_name}")

cryptic_name = ""
cryptic_name2 = ""
for letter in first_name:
    number = input("Please enter a number.\n>")
    letter_number = letter + number
    cryptic_name += number
    cryptic_name2 += letter_number
print(f"Your cryptic name is {cryptic_name}.")
print(f"Your other cryptic name is {cryptic_name2}.")