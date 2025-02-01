'''
1. Concatenate First and Last Name
Write a Python program that takes a first name 
and a last name as input from the user, and then
concatenates them into a single string with a space in between.
'''

# first_name = input("Please enter your first name: ")

# last_name = input("Please enter your last name: ")

# name = first_name + " " + last_name
# print(name)

# print(f"Hi! My name is {name}.")

'''
Tom and Sarah are siblings, and their cousin Emily is visiting.
Use the following clues to determine Emily's age:
•	Sarah is 4 years older than Tom.
•	Tom is 7 years old.
•	Emily's age is the average of Sarah and Tom's ages.
Can you figure out how old Emily is?
'''

# tom = 7
# sarah = tom + 4

# emily = (tom + sarah)/2 #this will result in a float
# #another way
# emily = int(emily) #type casting emily to be an integer

#one way of forcing result to be an integer
#emily = (tom + sarah) // 2 #integer division

# print(type(emily))

# print(f"Emily is {emily} years old.")

# statement = "Emily is " + str(emily) + " years old."
# print(statement)

''' Word Scrambler:
Create a Python program that takes a sentence as input, 
and then scrambles the order of the words to make the 
first word appear after the last word in the sentence 
using string concatenation. For example, if the input is 
"The quick brown fox", the output could be " quick brown fox The".
'''

str1 = "The quick brown fox"

# print(len(str1))
#example of slicing
#print(str1[5:8]) #[start: end : step]

first_word = str1[0:3]
#print(first_word)

rest_of_the_string = str1[4:]
# print(rest_of_the_string)

new_string = rest_of_the_string +" " + first_word
# print(new_string)

#string methods
string1 = " itsy bitsy spider went up the water spout "
print(string1)

# Remove leading and trailing whitespaces
string2 = string1.strip() #string.methodname()
print(string2)

# Convert to titlecase
string3 = string1.title()
print(string3)

# Replace "the" with an empty string (case-insensitive)
string4 = string1.replace("The", "")
print(string4)

string5 = string1.replace("the", "")
print(string5)

