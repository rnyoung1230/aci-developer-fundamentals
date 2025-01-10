# TASK 2C: CONDITIONALS PRACTICE   
'''
Write a program to allocate an auditorium seating row for the user based on their favorite number by doing the following... 
- Get a user-inputted value between 1 and 50 and save it in the variable fav_number. 
- Based on this value, using the following seating map, print the row that the user will sit in the auditorium. 
- If the user enters anything that is above 50 or below 0, the program should tell them that it is an invalid input.

Fav_number ---- Row

1 - 10 ----- E

11 - 20 ----- D

21 – 30 ----- C

31 – 40 ------ B

41 - 50 ------ A
'''

seatAvailable = True
rowA = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
rowB = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
rowC = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
rowD = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rowE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while seatAvailable:
    fav_number = int(input("Enter a number between 1 and 50\n>"))
    if 1 < fav_number < 50:
        #print(fav_number)
        if rowA.count(fav_number) > 0:
            print(f"Thank you! You will be in seat {fav_number}, which is in row A.")
        elif rowB.count(fav_number) > 0:
            print(f"Thank you! You will be in seat {fav_number}, which is in row B.")
        elif rowC.count(fav_number) > 0:
            print(f"Thank you! You will be in seat {fav_number}, which is in row C.")
        elif rowD.count(fav_number) > 0:
            print(f"Thank you! You will be in seat {fav_number}, which is in row D.")
        else:
            print(f"Thank you! You will be in seat {fav_number}, which is in row E.")
        seatAvailable = False
    else:
        print("You did not enter a number between 1 and 50. Please try again.")
