# PROBLEM 4 - PARAGRAPH SLICING
'''
The Jedi Name Generator - In the Star Wars universe, Jedi Knights often have unique names.
Your task is to write a program that generates a Jedi name based on user input and also generates
their age based on their favorite number.
    Here's how the program should work:
		□ Prompt the user to enter their first name.
		□ Prompt the user to enter their last name.
		□ Prompt the user to enter their favorite number.
	    □ Using string slicing and string concatenation (using the + operator with strings),
	    combine the first three letters of their first name, the first two letters of their last name,
	    and their favorite number to create their Jedi name.
		□ Next, take their favorite number and concatenate 537 to it to arrive at their age.
		□ Using string formatting, now display their jedi name and age.

	Here’s an example output:
        "Hello! Your Jedi name is KriKa44 and you are 581 years old."
'''
first_name = input("What's your first name?\n>")
last_name = input("What's your last name?\n>")
favorite_number = input("What's your favorite number?\n>")

intro_message = "Hello! Your Jedi name is {} and you are {} years old."

jedi_name = first_name[:3] + last_name[:2] + favorite_number
jedi_age = int(favorite_number) + 537

print(intro_message.format(jedi_name, jedi_age))