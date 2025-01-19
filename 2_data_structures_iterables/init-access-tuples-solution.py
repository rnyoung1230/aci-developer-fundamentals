# Step 1: Create a tuple to store details of a pet adoption.
adoption_details = ("Golden Retriever", "John Doe", 1, "01-01-2025", 300.00)

# Step 2: Print the entire tuple to confirm its contents.
print("Adoption details:", adoption_details)

# Step 3: Access and print the pet's breed and the adoption fee using positive indexing.
pet_breed = adoption_details[0]
adoption_fee = adoption_details[4]
print(f"Pet breed: {pet_breed}")
print(f"Adoption fee: {adoption_fee}")

# Step 4: Access and print the adopter's name using negative indexing.
adopter_name = adoption_details[-4]
print(f"Adopter's name: {adopter_name}")

# Step 5: Create a tuple using the tuple constructor to store adoption status options.
adoption_status = tuple(["Pending", "Approved", "Rejected"])

# Step 6: Print the tuple of adoption status options.
print("Adoption status options:", adoption_status)