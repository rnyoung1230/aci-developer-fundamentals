''' 
Develop a quiz or flashcard type of game where user will get a question based on the number 
they enter, and then the user will have 3 attempts to guess the answer to that question.'''

q_and_a = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal?": "Blue Whale",
    "What is the name of Harry Potter's owl?":"Hedwig",
    "How many sides does a hexagon have?" : "6",
    "In which country was the game of chess invented?" : "India"
}

#user must enter a number between 1 and 6, included.
'''
user = 2
'''
#print(q_and_a[2]) will not work
#q = {1 : " question1", 2: "q2", 3: "q3"}

q = {}
a = {}

for index, question in enumerate(q_and_a):
#    print(index, question)
    q[index+1] = question
    a[index+1] = q_and_a[question]
    
print(q)
print(a)

print("Welcome to the Flash Dance!")
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}, Welcome to the game! Let's get started.")

user_choice = int(input("Please enter a number between 1 and 6, inclusive: "))
print("Great! Good luck! Here is your question: ", end = "  >>>>>>>>>>  ")
print(q[user_choice])

number_of_attempts = 0
allowed_attempts = 3

while number_of_attempts < allowed_attempts:
    #prompt user to enter their answer
    answer = input("Please enter your answer to the above question:")
    #increment attempts
    number_of_attempts = number_of_attempts + 1
    
    #check if user's answer is the same as the answer from the dictionary a
    if answer.lower() == a[user_choice].lower():
        print("Congratulations, great job! You got the right answer!")
        break
    else:
        print(f"Incorrect answer. You have {allowed_attempts-number_of_attempts} attempts left.\n")
    if number_of_attempts == allowed_attempts:
        print("Game over!")