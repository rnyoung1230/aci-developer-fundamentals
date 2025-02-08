# Task 1: Working with required parameters
def create_profile(name, age, city):
    # Add parameters: name, age, city
    # Return them in a formatted string
    message = "{} is {} years old and lives in {}."
    return message.format(name, age, city)

formatted_message = create_profile("Robert", 53, "Madison")
print(formatted_message)

print("-----------------------------------")

# Task 2: Using default parameter values
def calculate_interest(principal, rate=0.05, years=1):
        return (principal * rate * years)

interest = calculate_interest(1000)
print(f"Interest: {interest}")

interest = calculate_interest(1000, 0.07)
print(f"Interest: {interest}")

interest = calculate_interest(1000, 0.07, 2)
print(f"Interest: {interest}")

print("-----------------------------------")

# # Task 3: Mixing positional and keyword arguments
def make_pizza(size, crust_type, *toppings):
    order = "A {} pizza with {} crust topped with {}."
    pizza_toppings = []
    for topping in toppings:
        pizza_toppings.append(topping)

    return order.format(size, crust_type, pizza_toppings)

print(make_pizza("large", "thin", "mushrooms", "pepperoni", "olives"))

print("-----------------------------------")
#
# Task 4: Create a function that accepts any number of key-value pairs
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Bob", age=30, email="bob@email.com", phone="555-1234", address="123 Main St.")