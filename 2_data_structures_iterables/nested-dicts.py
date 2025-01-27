# Starter Code: Nested Dictionary of Employees
employees = {
    "001": {
        "name": "John",
        "age": 35,
        "position": "Manager",
        "department": "Sales",
        "location": {
            "street_address": "123 Main Street",
            "city": "Anytown",
            "country": "USA",
        },
    },
    "002": {
        "name": "Ana",
        "age": 28,
        "position": "Engineer",
        "department": "IT",
        "location": {
            "street_address": "456 Any Ave",
            "city": "Anyville",
            "country": "USA",
        },
    },
}

# Task 1: Access employee details, as follows:
'''
Access and print the name of the employee with ID "001".
Access and print the city of the employee with ID "002".
Print the results.
'''
employee_001_name = employees["001"]["name"]
employee_002_city = employees["002"]["location"]["city"]

print("Employee ID 001 name:", employee_001_name)
print("Employee ID 002 city:", employee_002_city)
print("-----------------------------------")

# Task 2: Add a new employee, as follows:
'''
Add a new employee with ID "003" to the employees dictionary. The employee's details are:

Name: "Carlos"
Age: 42
Position: "Director"
Department: "Operations"
Location:
Street Address: "789 New St"
City: "Newtown"
Country: "USA"

Print the updated employees dictionary.
'''
new_employee = {"name": "Carlos", "age": 42, "position": "Director", "department": "Operations",
                "location": {"street_address": "789 New St", "city": "Newtown", "country": "USA"}}

employees.update({"003": new_employee})

print("Updated employees:")

for employee in employees:
    print(employees[employee])

print("-----------------------------------")

# Task 3: Update employee details, as follows:
'''
Update the position of the employee with ID "001" to "Regional Manager".
Print the updated employees dictionary.
'''
employees["001"]["position"] = "Regional Manager"

print("Updated employees:")

for employee in employees:
    print(employees[employee])

print("-----------------------------------")

# Task 4: Access nested values, as follows:
'''
Access and print the street address of the employee with ID "002".
Print the result.
'''
print("Street address of employee ID 002:")

print(employees["002"]["location"]["street_address"])

print("-----------------------------------")

# Task 5: Delete an employee, as follows:
'''
Remove the employee with ID "003" from the employees dictionary.
Print the updated employees dictionary.
'''
#employees.pop("003")
del employees["003"]

print("Updated employees:")

for employee in employees:
    print(employees[employee])