# LABOLOGY SESSION - 1/23
# --------------------

# TASK 1: Find the average of a given list
nums = [12, 34, 56, 78, 93, 123, 234, 45, 67, 89, 15, 11, 22, 73, 54, 65, 46, 17, 28, 39]
sum = 0

for number in nums:
    sum += number

average = sum / len(nums)
print(f"Average: {average}")

# TASK 2: You are given the following lists. Combine them into a dictionary with fruits as the keys
#and quantity as the values.
fruits = ["apples", "bananas", "oranges"]
quantities = [10, 8, 20]

fruit_quantities = {}
for i in range(len(fruits)):
    fruit_quantities[fruits[i]] = quantities[i]

print(fruit_quantities)

# TASK 3: Twins - check if identical numbers are beside each other in a list
# THIS IS A COMMON INTERVIEW QUESTION
numbers = [0, 11, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]
# previous_number = None
#
# for number in numbers:
#     if number == previous_number:
#         print(f"Identical numbers found next to each other: {number}")
#         previous_number = number
#     else:
#         previous_number = number

for i in range(len(numbers)-1): # -1 to avoid getting an index out of range exception
    if numbers[i] == numbers[i + 1]: # compare current number with next one in list
        print(f"Identical numbers found next to each other: {numbers[i]}")
    else:
        continue



