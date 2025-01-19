# Step 1: Create a dictionary to store the inventory of the pet store.
# Each item is a key, and its quantity is the value.
pet_store_inventory = {
    "dog_food": 10,
    "cat_toy": 5,
    "bird_seed": 8
}

# Step 2: Print the dictionary to confirm its contents.
print("Pet store inventory:", pet_store_inventory)

# Step 3: Access and print the number of "cat_toy" items in stock.
cat_toy_stock = pet_store_inventory["cat_toy"]
print("Number of cat toys in stock:", cat_toy_stock)

# Step 4: Add a new item to the inventory: "hamster_wheel": 3.
pet_store_inventory["hamster_wheel"] = 3

# Step 5: Print the updated dictionary to confirm the new item was added.
print("Updated pet store inventory:", pet_store_inventory)