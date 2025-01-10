print("Hello World!")

# Task 1
first_name = input("What is your first name?\n>")
last_name = input("What is your last name?\n>")
print(f"{first_name} {last_name}")
print(first_name + " " + last_name)
print("--------------------")


# Task 2
tom_age = 7
sarah_age = 11
# Emily is the average of Tom and Sarah
emily_age = int((tom_age + sarah_age) / 2)
print(f"Emily is {emily_age} years old.")
print("-------------------")

# Task 3 - Slicing
sentence = "The brown fox is quick."
print(sentence)
sentence_rearranged = sentence[17:22] + " " + sentence[:16] + sentence[22:]
print(sentence_rearranged)
print("--------------------")

# Task 4 - Other String Manipulations
word = "Jjonathan"
print(word)
new_word = word.replace("Jjonathan", " Jonathan ")
print(new_word)
print(new_word.strip())
print(new_word.upper().strip())
print("--------------------")