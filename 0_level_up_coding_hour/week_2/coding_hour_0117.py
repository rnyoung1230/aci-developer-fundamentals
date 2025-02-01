'''
#3 The Fitness Challenge Counter

You're participating in a 10-day fitness challenge, and you want to create a program
to help you keep track of your daily exercises. 
Your goal is to do push-ups every day, 
starting with 5 push-ups on day 1 and increasing by 2 push-ups each day.

Write a program that does the following:

1. Use a for loop to print out the number of push-ups you need to do for each day of the 10-day challenge.
2. Also print the total number of push-ups you will have done by the end of the challenge.

Your program should output:
- The daily push-up count for each day (1 to 10)
- The total number of push-ups done over the 10 days

Example output:
```
Day 1: 5 push-ups
Day 2: 7 push-ups
Day 3: 9 push-ups

'''
daily_count = 0
total_count = 0

for day in range(1, 11):
    
    if day == 1:
        daily_count = 5
        print(f"{day}:{daily_count}")
    else:
        daily_count = daily_count + 2
        print(f"{day}:{daily_count}")
    
    total_count = total_count + daily_count
    
print(f"The total number of pushups for 10 days are {total_count}")

'''
#2: User input using while loop
Write a program that prompts user to enter numbers, one at a time until the user wants to quit.
From the numbers entered, find maximum and minimum of all numbers entered by the user.
'''    

max = None #NoneType - [empty container]
min = None
num = None
# print(type(max))

while num != 'quit':
    num = input("Enter a number: ")
    
    if num == 'quit':
        break
    else:
        num = int(num)
        
    if max == None or num > max:
        max = num
    if min == None or num < min:
        min = num

print(f"The largest number entered is {max} and the smallest number entered is {min}.")

'''
#1. For loop
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
'''
total = 0

for i in range(1, 101):
    total = total +  i

print(total)
        
    
        
        
        
    