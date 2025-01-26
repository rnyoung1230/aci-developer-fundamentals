print("Level Up Coding Hour: Week 3")

# Task 1 - Develop a quiz or flashcard game where users will get a question based on the number they enter,
# and then they will have 3 attempts to guess the answer to that question.

question_1 = "What data structure is UNORDERED and only contains UNIQUE elements?" # Set
question_2 = "What data structure is INMUTABLE?" # Tuple
question_3 = "What data structure is comprised of KEY-VALUE PAIRS?" # Dictionary

answer_1 = "Set"
answer_2 = "Tuple"
answer_3 = "Dictionary"

wants_to_play = True

print("********* Data Structures Quiz Game *********\n")

while wants_to_play:
    number = input("Please enter a number from 1-3.\n>")
    # Ask question based on number they entered
    if number == "1":
        answer = input(f"{question_1}\n>")
        if answer == answer_1:
            print(f"Congratulations! {answer} is correct.")
        else:
            print(f"Sorry. {answer} is incorrect.")
    elif number == "2":
        answer = input(f"{question_2}\n>")
        if answer == answer_2:
            print(f"Congratulations! {answer} is correct.")
        else:
            print(f"Sorry. {answer} is incorrect.")
    elif number == "3":
        answer = input(f"{question_3}\n>")
        if answer == answer_3:
            print(f"Congratulations! {answer} is correct.")
        else:
            print(f"Sorry. {answer} is incorrect.")
    else:
        print("You did not enter a valid number. Please try again.")

    wants_to_quit = input("Do you want to quit? Enter Y or N\n>")
    if wants_to_quit == "Y":
        wants_to_play = False
        print("Thanks for playing!")
    else:
        continue