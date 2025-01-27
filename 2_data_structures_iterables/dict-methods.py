# Starter Code for Practicing Python Dictionary Methods

# Create the inventory dictionary
inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

# TASK 1:  Access keys and values, as follows:
'''
Use the keys() method to get all the keys in the inventory dictionary.
Use the values() method to get all the values in the inventory dictionary.
Print the keys and values.
'''
print("------------ TASK 1 ------------")
keys = inventory.keys()
values = inventory.values()

print("The inventory keys:", keys)
print("The inventory values:", values)

print("")

# TASK 2:  Use get() and add a new item, as follows:
'''
Use the get() method to retrieve the value of "apples".
Use the get() method to attempt to retrieve the value of "grapes" (which does not exist).
Add "grapes" to the dictionary with a value of 6 using the update() method.
Print the retrieved values and the updated dictionary.
'''
print("------------ TASK 2 ------------")

key1 = "apples"
value1 = inventory.get(key1)
print(f"The value of {key1}: {value1}")

key2 = "grapes"
value2 = inventory.get(key2)
print(f"The value of {key2}: {value2}")

inventory.update({key2 : 6})
print(f"Updated inventory: {inventory}")

print("")

# TASK 3:  Copy and create a new dictionary, as follows:
'''
Use the copy() method to create a copy of the inventory dictionary.
Use the fromkeys() method to create a new dictionary with the same keys as inventory, but all values set to 0.
Print the copied dictionary and the new dictionary.
'''
print("------------ TASK 3 ------------")

inventory_copy = inventory.copy()
print("Copied inventory:", inventory_copy)

inv_keys = inventory.keys()
new_inventory = inventory.fromkeys(inv_keys, 0)
print("New inventory:", new_inventory)

print("")

# TASK 4:  Remove items, as follows:
'''
Use the pop() method to remove "coconuts" from the inventory dictionary.
Use the popitem() method to remove the last item added to the dictionary.
Print the removed items and the updated dictionary after each operation.
'''
print("------------ TASK 4 ------------")

remove_item_key = "coconuts"
inventory.pop(remove_item_key)
print("Inventory after pop():", inventory)

inventory.popitem()
print("Inventory after popitem():", inventory)

print("")

# TASK 5:  Clear a dictionary, as follows:
'''
Use the clear() method to remove all items from the inventory dictionary.
Print the cleared dictionary.
'''
print("------------ TASK 5 ------------")

inventory.clear()
print("Inventory after clear():", inventory)

print("")