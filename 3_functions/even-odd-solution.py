def isEven(number):
    return number % 2 == 0

def isOdd(number):
    return number % 2 == 1

# Test the functions with numbers 0-9
for number in range(10):
    even_result = isEven(number)
    odd_result = isOdd(number)
    print(f"Number {number} is even: {even_result} and odd: {odd_result}")
