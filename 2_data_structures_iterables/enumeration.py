# Starter Code for Enumerating Pet Names

# Step 1: Create a list of pet names.
# Pet names: "Buddy", "Max", "Bella", "Charlie", "Luna"
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use the enumerate() function to loop through the list.
# Print a numbered list of pet names starting with 0 for the index.
# Example output: "0: Buddy"
for i, name in enumerate(pet_names):
    print(f"{i}: {name}")

print("----------------------------")

# Step 3: Adjust the numbering manually so it starts from 1 instead of 0.
# Example output: "1: Buddy"
#for i, name in enumerate(pet_names):
for i, name in enumerate(pet_names):
    print(f"{i + 1}: {name}")

print("----------------------------")