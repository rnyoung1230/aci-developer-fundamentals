# Task 1: Working with min() and max()
numbers = [15, 8, 42, 23, 16]
smallest = min(numbers)
largest = max(numbers)
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")

# Task 2: Working with pow()
base = 4
exponent = 3
result = pow(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

# Task 3: Working with abs()
negative_num = -42
positive_result = abs(negative_num)
print(f"The absolute value of {negative_num} is: {positive_result}")

# Task 4: Combining functions
numbers_2 = [-5, 10, -15, 20, -25]
absolute_numbers = []  # Create an empty list to store absolute values
for num in numbers_2:
    absolute_numbers.append(abs(num))
largest_absolute = max(absolute_numbers)
print(f"The largest absolute value is: {largest_absolute}")
