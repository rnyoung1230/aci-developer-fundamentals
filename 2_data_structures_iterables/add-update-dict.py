# Starter Code for Adding and Updating Pet Store Inventory

# Step 1: Create a dictionary to store the inventory of the pet store.
# Items: "dog_food": 10, "cat_toy": 5, "bird_seed": 8
pet_store_inventory = {
    "dog_food": 10,
    "cat_toy": 5,
    "bird_seed": 8
}
print(pet_store_inventory)

# Step 2: Add a new item to the inventory: "hamster_wheel": 3.
pet_store_inventory["hamster_wheel"] = 3

# Step 3: Update the stock of "cat_toy" to 10.
pet_store_inventory["cat_toy"] = 10

# Step 4: Increment the stock of "dog_food" by 5 and decrement "bird_seed" by 2.
pet_store_inventory["dog_food"] += 5
pet_store_inventory["bird_seed"] -= 2

# Step 5: Print the updated inventory to confirm changes.
print("Updated pet store inventory:", pet_store_inventory)