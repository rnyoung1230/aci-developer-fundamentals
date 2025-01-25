# PROBLEM 5
"""
Write a program to do the following:
    1. Create an empty dictionary, scores = {}
    2. Add 3 names and associated scores into the dictionary
    3. Iterate through the dictionary and print the key-value pairs using string formatting
       to look like this – Jack --------- 90
    4. Get user input for a name and check to see if that name exists in the scores dictionary.
       If it does, you should print the score of that user name.
	5. Get user input for a name and if that name exists in the scores dictionary,
	   decrease the related score value by 10
    6. Print the updated scores.
"""
scores = {}
scores["Jack"] = 90
scores["Sally"] = 88
scores["Jason"] = 95
print(scores)

for name, score in scores.items():
    print(f"{name} --------- {score}")

entered_name = input("Please enter a name.\n>")
#print(f"You entered: {entered_name}")
if scores.keys().__contains__(entered_name):
    score = scores.get(entered_name)
    print(f"{entered_name}'s original score is: {score}")
    scores[entered_name] -= 10
    #print(updated_score)
else:
    print("Name not found.")

print("Updated scores:")
for score in scores.values():
    print(f"{score} ", end='')




