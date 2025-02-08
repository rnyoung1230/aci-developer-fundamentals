# Task 1: Working with required parameters
def create_profile(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

# Test Task 1
print(create_profile("Alice", 25, "New York"))

# Task 2: Using default parameter values
def calculate_interest(principal, rate=0.05, years=1):
    return principal * rate * years

# Test Task 2
print(calculate_interest(1000))  # Using defaults
print(calculate_interest(1000, 0.07))  # Custom rate
print(calculate_interest(1000, 0.07, 2))  # All custom values

# Task 3: Mixing positional and keyword arguments
def make_pizza(size, crust_type, *toppings):
    toppings_list = ", ".join(toppings)
    return f"A {size} pizza with {crust_type} crust topped with: {toppings_list}"

# Test Task 3
print(make_pizza("large", "thin", "mushrooms", "pepperoni", "olives"))

# Task 4: Create a function that accepts any number of key-value pairs
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test Task 4
print_user_info(name="Bob", age=30, email="bob@email.com", phone="555-1234")
