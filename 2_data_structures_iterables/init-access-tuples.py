# Starter Code for Working with Tuples

# Step 1: Create a tuple to store details of a pet adoption.
# Example details: "Golden Retriever", "John Doe", 1, "01-01-2025", 300.00
adoption_details = ("Golden Retriever", "John Doe", 1, "01-01-2025", 300.00)

# Step 2: Print the entire tuple to confirm its contents.
print("Adoption details:", adoption_details)

# Step 3: Access and print the pet's breed and the adoption fee using positive indexing.
print(f"Breed: {adoption_details[0]}\nAdoption Fee: {adoption_details[4]}")

# Step 4: Access and print the adopter's name using negative indexing.
print(f"Adopter's Name: {adoption_details[-4]}")

# Step 5: Create a tuple using the tuple constructor to store adoption status options.
# Example options: "Pending", "Approved", "Rejected"
adoption_status_list = ["Pending", "Approved", "Rejected"]
adoption_status = tuple(adoption_status_list)

# Step 6: Print the tuple of adoption status options.
print("Adoption status options:", adoption_status)