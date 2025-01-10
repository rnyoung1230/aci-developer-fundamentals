'''
# Example 1
message = input("Write your message here: ")
print(message)

# Example 2
customername = input("What's your name?")
print("Welcome " + customername)

# Example 3
birthyear = input("What year were you born?")

if (int(birthyear) > 2002):
    print("True")
else:
    print("False")'''
    
# Exercise 1
'''
Use the input() function to prompt the user to do the following:
- Enter their name
- Enter their birth year
- Use the int() function to convert the birth year from a string to an integer
- Calculate the user's age based on the current year and print a message with their name and age
'''
user_name = input("What's your name?\n>")
user_birth_year = int(input("What year were you born?\n>"))
current_year = 2025
user_age = current_year - user_birth_year
print(f"Hello {user_name}. You are {user_age} years old.")


# Exercise 2
'''
Use an if statement to check if the user is 18 or older
- If they are 18 or older, print "You are an adult."
- Otherwise, print "You are a minor."
'''
if user_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")