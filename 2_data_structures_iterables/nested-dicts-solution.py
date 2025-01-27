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

# Problem 1: Access Employee Details
name_001 = employees["001"]["name"]
city_002 = employees["002"]["location"]["city"]
print("Problem 1 - Name of Employee 001:", name_001)  # Output: John
print("Problem 1 - City of Employee 002:", city_002)  # Output: Anyville

# Problem 2: Add a New Employee
employees["003"] = {
    "name": "Carlos",
    "age": 42,
    "position": "Director",
    "department": "Operations",
    "location": {
        "street_address": "789 New St",
        "city": "Newtown",
        "country": "USA",
    },
}
print("Problem 2 - Updated Employees Dictionary:", employees)

# Problem 3: Update Employee Details
employees["001"]["position"] = "Regional Manager"
print("Problem 3 - Updated Employees Dictionary:", employees)

# Problem 4: Access Nested Values
street_address_002 = employees["002"]["location"]["street_address"]
print("Problem 4 - Street Address of Employee 002:", street_address_002)  
# Output: 456 Any Ave

# Problem 5: Delete an Employee
del employees["003"]
print("Problem 5 - Updated Employees Dictionary After Deletion:", employees)