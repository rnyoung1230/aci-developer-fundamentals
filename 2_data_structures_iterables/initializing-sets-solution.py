# Step 1: Create a set of unique pet breeds available at the store.
# Note that "Golden Retriever" is duplicated, but the set will only keep one instance.
pet_breeds = {"Golden Retriever", "Persian Cat", "Parrot", "Siamese Cat", "Golden Retriever"}

# Step 2: Print the set to verify that duplicate values are removed.
print("Unique pet breeds:", pet_breeds)

# Step 3: Convert a list of new pet breeds into a set and print the result.
new_breeds_list = ["Cockatoo", "Maine Coon", "Golden Retriever"]
new_breeds_set = set(new_breeds_list)
print("New unique breeds from list:", new_breeds_set)

# Step 4: Create an empty set to store exotic breeds and print it.
exotic_breeds = set()
print("Empty set for exotic breeds:", exotic_breeds)