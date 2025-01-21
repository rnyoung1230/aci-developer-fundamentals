# Starter Code for Practicing Python List Methods

# Step 1: Create a list of numbers and a list of fruits.
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

'''
Task 1: Add elements to a list, as follows:
Use the append() method to add 60 to the numbers list.
Use the insert() method to add "mango" to the beginning of the fruits list.
Print the updated numbers and fruits lists.
'''
print("--------- TASK 1 ---------")

numbers.append(60)
fruits.insert(0, "mango")

print(numbers)
print(fruits)
print("")

'''
Task 2: Remove elements from a list, as follows:
Use the pop() method to remove the last element from the numbers list.
Use the remove() method to delete "banana" from the fruits list.
Print the updated numbers and fruits lists.
'''
print("--------- TASK 2 ---------")

numbers.pop(-1)
fruits.remove("banana")

print(numbers)
print(fruits)
print("")

'''
Task 3: Extend and sort a list, as follows:
Use the extend() method to combine the fruits list with a new list: ["peach", "pear"].
Sort the extended list alphabetically using the sort() method.
Print the updated fruits list.
'''
print("--------- TASK 3 ---------")

new_fruits = ["peach", "pear"]
fruits.extend(new_fruits)
fruits.sort()

print(fruits)
print("")

'''
Task 4: Combine list methods, as follows:
Use the copy() method to create a copy of the numbers list.
Add 100 to the copied list using append().
Reverse the copied list using the reverse() method.
Print both the original numbers list and the modified copied list.
'''
print("--------- TASK 4 ---------")

numbers_copy = numbers.copy()
numbers_copy.append(100)
numbers_copy.reverse()

print(numbers)
print(numbers_copy)
print("")

'''
Task 5: Complete some complex manipulation, as follows:
Create a grocery list with items ["milk", "bread", "eggs", "butter", "cheese"].
Use the following methods in sequence:
Use append() to add "yogurt" to the list.
Use remove() to remove "butter".
Use index() to find the position of "eggs", and then insert "juice" just before "eggs".
Use sort() to sort the list alphabetically.
Print the final sorted grocery list.
'''
print("--------- TASK 5 ---------")

grocery_list = ["milk", "bread", "eggs", "butter", "cheese"]
grocery_list.append("yogurt")
grocery_list.remove("butter")

egg_position = grocery_list.index("eggs")
print(f"Grocery list before insert: {grocery_list}")
grocery_list.insert(egg_position, "juice")
print(f"Grocery list after insert: {grocery_list}")

grocery_list.sort()
print(f"Grocery list after sort: {grocery_list}")