# PROBLEM 1 - GREETING MESSAGE
'''
Create a Python program that prompts the user to enter their name,
and then prints a greeting message using string formatting.
For example, if the user enters "Alice", the program should print "Hello, Alice!".
Next continue and ask about the user’s hobby/interest.
Use string formatting to print a statement about their topic or interest.
'''

name = input("What is your name?\n>")
greeting_message = "Hello, {}!"
print(greeting_message.format(name))
print("")

interests_response = input(f"Do you have any hobbies, {name}? Please respond Y or N.\n>")
if interests_response == "Y":
    favorite_hobby = input("Cool! What's your favorite one?\n>")
    topic_statement = "Right on {}! I'd love to hear more about your interest in {}."
    print(topic_statement.format(name, favorite_hobby.lower()))
else:
    print(f"Oh well. Good-bye, {name}.")

print("--------------------")

# PROBLEM 2 - WORD MIXER
'''
Ask user input for two words. Your task is to create a third word using the first half of 
the first word and the second half of the second word. 
Use a combination of any two of the string methods from eLearning on the third word you have created.
'''
first_word = input("Please enter a word...any word will do.\n>")
second_word = input("Please enter another word.\n>")
print(f"You entered {first_word} and {second_word}.")

first_word_length = len(first_word)
second_word_length = len(second_word)
print(f"first_word_length:\t{first_word_length}\nsecond_word_length:\t{second_word_length}")

# Create a mixed word using first half of first word and second half of second word
mixed_word = ""
first_word_length_halved = first_word_length // 2
second_word_length_halved = second_word_length // 2
print(f"first_word_length_halved:\t{first_word_length_halved}\nsecond_word_length_halved:\t{second_word_length_halved}")

mixed_word = first_word[:first_word_length_halved] + second_word[second_word_length_halved:]
print("")
print(f"Thanks. I used your entries to create a new mixed word called \"{mixed_word}\".")

print("--------------------")