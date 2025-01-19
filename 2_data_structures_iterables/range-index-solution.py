# Step 1: Create a list of pet names.
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use a for loop with range() and len() to iterate through the list by index.
print("Numbered list of pet names:")
for i in range(len(pet_names)):
    # Add 1 to the index to start numbering at 1.
    print(f"{i + 1}. {pet_names[i]}")