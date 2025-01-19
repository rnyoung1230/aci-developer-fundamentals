# Starter Code for Accessing and Slicing Pet Store Inventory

# Step 1: Create a list of pet products available in the store.
# Products: "Dog Food", "Cat Toy", "Bird Seed", "Hamster Wheel", "Fish Tank"
pet_products = ["Dog Food", "Cat Toy", "Bird Seed", "Hamster Wheel", "Fish Tank"]

# Step 2: Print the entire list to verify its contents.
print("All products:", pet_products)

# Step 3: Access and print the first product in the list using a positive index.
print("First product:", pet_products[0])

# Step 4: Access and print the last product in the list using a negative index.
print("Last product:", pet_products[-1])

# Step 5: Slice and print the middle three products from the list.
print("Middle 3 products:", pet_products[1:4])

# Step 6: Slice and print the first two products.
print("First 2 products:", pet_products[:2])

# Step 7: Slice and print all products except the first one.
print("All products except first one:", pet_products[1:])