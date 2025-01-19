# Step 1: Create a list of pet owner names with one duplicate.
owner_names = ["alex", "beatriz", "carla", "derek", "alex"]

# Step 2: Loop through the list to print a personalized thank-you message for each owner.
print("Thank-you messages from the list:")
for name in owner_names:
    print(f"Thank you, {name.title()}, for taking care of your pet!")

# Step 3: Convert the list of owner names to a set to remove duplicates, and loop through it.
owner_names_set = set(owner_names)
print("\nThank-you messages from the set (duplicates removed):")
for name in owner_names_set:
    print(f"Thank you, {name.title()}, for taking care of your pet!")

# Step 4: Print a note after looping through the set, mentioning that duplicates were removed.
print("\nNote: Duplicates were removed when converting the list to a set.")