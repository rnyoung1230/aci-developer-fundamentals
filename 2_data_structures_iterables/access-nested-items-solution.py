# Step 1: Create a list of dictionaries to store employee details.
employees = [
    {"name": "Emily", "age": 29, "position": "Cashier", "department": "Front Desk"},
    {"name": "Mike", "age": 34, "position": "Veterinarian", "department": "Clinic"},
    {"name": "Sophia", "age": 27, "position": "Trainer", "department": "Pet Training"}
]

# Step 2: Use a loop to print each employee's name and department.
print("Employee details:")
for emp in employees:
    print(f'{emp["name"]} is in the {emp["department"]} department.')

# Step 3: Modify the loop to also print each employee's position.
print("\nDetailed employee information:")
for emp in employees:
    print(f'{emp["name"]} is in the {emp["department"]} department and works as a {emp["position"]}.')