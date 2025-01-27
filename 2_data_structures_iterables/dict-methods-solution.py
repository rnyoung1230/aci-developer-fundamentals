# Create the inventory dictionary
inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

# Problem 1: Accessing Keys and Values
keys = inventory.keys()
values = inventory.values()
print("Problem 1 - Keys:", keys)  # Output: dict_keys(['apples', 'bananas', 'coconuts', 'dates'])
print("Problem 1 - Values:", values)  # Output: dict_values([5, 4, 2, 10])

# Problem 2: Using `get()` and Adding a New Item
apples_value = inventory.get("apples")
grapes_value = inventory.get("grapes")  # Should return None
inventory.update({"grapes": 6})
print("Problem 2 - Value of apples:", apples_value)  # Output: 5
print("Problem 2 - Value of grapes:", grapes_value)  # Output: None
print("Problem 2 - Updated Inventory:", inventory)
# Output: {'apples': 5, 'bananas': 4, 'coconuts': 2, 'dates': 10, 'grapes': 6}

# Problem 3: Copying and Creating a New Dictionary
copied_inventory = inventory.copy()
new_inventory = inventory.fromkeys(inventory.keys(), 0)
print("Problem 3 - Copied Inventory:", copied_inventory)
# Output: {'apples': 5, 'bananas': 4, 'coconuts': 2, 'dates': 10, 'grapes': 6}
print("Problem 3 - New Inventory with 0 values:", new_inventory)
# Output: {'apples': 0, 'bananas': 0, 'coconuts': 0, 'dates': 0, 'grapes': 0}

# Problem 4: Removing Items
removed_coconuts = inventory.pop("coconuts")
print("Problem 4 - Removed 'coconuts':", removed_coconuts)  # Output: 2
print("Problem 4 - Inventory after removing 'coconuts':", inventory)
# Output: {'apples': 5, 'bananas': 4, 'dates': 10, 'grapes': 6}

removed_last_item = inventory.popitem()
print("Problem 4 - Removed Last Item:", removed_last_item)
print("Problem 4 - Inventory after popitem:", inventory)
# Output: {'apples': 5, 'bananas': 4, 'dates': 10}

# Problem 5: Clearing a Dictionary
inventory.clear()
print("Problem 5 - Cleared Inventory:", inventory)  # Output: {}