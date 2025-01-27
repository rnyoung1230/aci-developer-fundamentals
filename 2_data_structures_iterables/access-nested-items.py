# Starter Code for Accessing Nested Items in Employee Records

# Step 1: Create a list of dictionaries to store employee details.
# Each dictionary should have keys: "name", "age", "position", "department"
employees = [
    {"name": "Sally", "age": 25, "position": "Engineer", "department": "Sales"},
    {"name": "John", "age": 53, "position": "Manager", "department": "IT"},
    {"name": "Beth", "age": 37, "position": "Talent Recruiter", "department": "HR"}
]

# Step 2: Use a loop to print each employee's name and department.
# Example output: "John is in the Sales department."
for employee in employees:
    print(f"{employee["name"]} is in the {employee["department"]} department.")

# Step 3: Modify the loop to also print each employee's position.
# Example output: "John is in the Sales department and works as a Manager."
for employee in employees:
    print(f"{employee["name"]} is in the {employee["department"]} department and works as a {employee["position"]}.")