# Step 1: Create a list of pet names.
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use the enumerate() function to loop through the list.
print("Numbered list of pet names (starting at 0):")
for i, name in enumerate(pet_names):
    print(f"{i}: {name}")

# Step 3: Adjust the numbering manually so it starts from 1 instead of 0.
print("\nNumbered list of pet names (starting at 1):")
for i, name in enumerate(pet_names):
    print(f"{i + 1}: {name}")