# Starter Code for Managing Pet Store Inventory

# Step 1: Create a dictionary to store the inventory of the pet store.
# Items: "dog_food": 10, "cat_toy": 5, "bird_seed": 8
pet_store_inventory = {
    "dog_food" : 10,
    "cat_toy" : 5,
    "bird_seed": 8
}

# Step 2: Print the dictionary to confirm its contents.
print("Pet store inventory:", pet_store_inventory)

# Step 3: Access and print the number of "cat_toy" items in stock.
print("Number of cat toys:", pet_store_inventory["cat_toy"])

# Step 4: Add a new item to the inventory: "hamster_wheel": 3.
pet_store_inventory["hamster_wheel"] = 3

# Step 5: Print the updated dictionary to confirm the new item was added.
print("Updated pet store inventory:", pet_store_inventory)