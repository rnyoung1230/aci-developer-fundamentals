# Starter Code for Practicing Python Set Methods

# Create initial sets for practice.
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}

# TASK 1: Add and remove elements, as follows:
'''
Use the add() method to add "lime" to the fruits set.
Use the remove() method to remove "mango" from the fruits set.
Print the updated fruits set.
'''
# print("------------ TASK 1 ------------")
#
# print(f"Fruits before operations: {fruits}")
#
# fruits.add("lime")
# fruits.remove("mango")
#
# print(f"Fruits after operations: {fruits}")
#
# print("")
# TASK 2: Check membership and clear a set, as follows:
'''
Check if "carrot" is in the vegetables set using the in keyword.
Use the clear() method to empty the vegetables set.
Print the result of the membership check and the cleared vegetables set.
'''
# print("------------ TASK 2 ------------")
#
# vegetable = "carrot"
#
# if vegetable in vegetables:
#     print(f"{vegetable} is in the set.")
# else:
#     print(f"{vegetable} is NOT in the set.")
#
# vegetables.clear()
# print(f"Vegetables set after clear method: {vegetables}.")
#
# print("")
# TASK 3: Copy and create new sets, as follows:
'''
Use the copy() method to create a copy of the fruits set.
Use the update() method to add the following items to the vegetables set: "spinach", "kale".
Print the copied set and the updated vegetables set.
'''
print("------------ TASK 3 ------------")
fruits_copy = fruits.copy()
fruits_copy.add("pear")

print(f"Fruits original: {fruits}")
print(f"Fruits copy: {fruits_copy}.")

veg_to_add = ["spinach", "kale"]
vegetables.update(veg_to_add)

print(vegetables)

print("")
# TASK 4: Remove items with pop(), as follows:
'''
Use the pop() method to randomly remove an item from the fruits set.
Print the item removed and the updated fruits set.
'''
print("------------ TASK 4 ------------")

print(f"Fruits set before operation: {fruits_copy}.")

removed_item = fruits_copy.pop()
print(f"Removed item: {removed_item}")
print(f"Fruits set after operation: {fruits_copy}.")

print("")
# TASK 5: Clear a set, as follows:
'''
Use the clear() method to remove all items from the fruits set.
Print the cleared fruits set.
'''
print("------------ TASK 5 ------------")

print(f"Fruits set before clear: {fruits}")
fruits.clear()
print(f"Fruits set after clear: {fruits}")
