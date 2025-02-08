def isEven(number):
    # Return True if number is even
    # Return False if number is odd
    return number % 2 == 0

def isOdd(number):
    # Return True if number is odd
    # Return False if number is even
    return number % 2 != 0

# Task 3: Test your functions by creating a loop
# Write your loop here
for i in range(10):
    print(f"Number {i} is even: {isEven(i)} and odd: {isOdd(i)}")