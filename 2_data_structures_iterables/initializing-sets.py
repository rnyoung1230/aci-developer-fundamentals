# Starter Code for Managing Unique Pet Breeds

# Step 1: Create a set of unique pet breeds available at the store.
# Breeds: "Golden Retriever", "Persian Cat", "Parrot", "Siamese Cat", "Golden Retriever"
pet_breeds = {"Golden Retriever", "Persian Cat", "Parrot", "Siamese Cat", "Golden Retriever"}

# Step 2: Print the set to verify that duplicate values are removed.
print("Unique pet breeds:", pet_breeds)
print("-------------------------------")

# Step 3: Convert a list of new pet breeds into a set and print the result.
# New breeds: ["Cockatoo", "Maine Coon", "Golden Retriever"]
pet_breed_list = ["Cockatoo", "Maine Coon", "Golden Retriever", "Cockatoo"]
print(pet_breed_list)

pet_breed_set = set(pet_breed_list)
print(pet_breed_set)
print("-------------------------------")

# Step 4: Create an empty set to store exotic breeds and print it.
exotic_breeds_set = set()
print(exotic_breeds_set)
print("-------------------------------")