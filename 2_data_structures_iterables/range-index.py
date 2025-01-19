# Starter Code for Numbering Pet Names

# Step 1: Create a list of pet names.
# Pet names: "Buddy", "Max", "Bella", "Charlie", "Luna"
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use a for loop with range() and len() to iterate through the list by index.
# Print a numbered list of pet names starting with 1.
# Example output: "1. Buddy"
for i in range(len(pet_names)):
    print(f"{i + 1}. {pet_names[i]}")