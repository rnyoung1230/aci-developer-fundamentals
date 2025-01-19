# Given dictionary
inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

# Step 1: Access and store the values for "dates" and "apples".
num_dates = inventory["dates"]
num_apples = inventory["apples"]

# Step 2: Access and store the values for "bananas" and "coconuts".
num_bananas = inventory["bananas"]
num_coconuts = inventory["coconuts"]

# Step 3: Print the original message.
print(f"There are {num_dates} dates and {num_apples} apples in the inventory.")

# Step 4: Print a new string using the values of "bananas" and "coconuts".
print(f"There are {num_bananas} bananas and {num_coconuts} coconuts in the inventory.")