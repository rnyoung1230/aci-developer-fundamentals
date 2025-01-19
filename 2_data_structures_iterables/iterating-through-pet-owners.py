# Starter Code for Iterating Through Pet Owner Names

# Step 1: Create a list of pet owner names with one duplicate.
# Names: "alex", "beatriz", "carla", "derek", "alex"
owner_names = ["alex", "beatriz", "carla", "derek", "alex"]
print(owner_names)

# Step 2: Loop through the list to print a personalized thank-you message for each owner.
# Example output: "Thank you, Alex, for taking care of your pet!"
for owner in owner_names:
    print(f"Thank you, {owner.title()}, for taking care of your pet!")

# Step 3: Convert the list of owner names to a set to remove duplicates, and loop through it.
owner_names_set = set(owner_names)
for owner in owner_names_set:
    print(owner.title())

# Step 4: Print a note after looping through the set, mentioning that duplicates were removed.
print("\nNote: Duplicates were removed when converting the list to a set.")