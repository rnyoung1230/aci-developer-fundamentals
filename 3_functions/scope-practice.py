# Task 1: Fix the scope error

def calculate_total():
    subtotal = 50
    tax = 0.1
    global total  # Calculate total using subtotal and tax
    total = (subtotal * tax) + subtotal

calculate_total()
print("The total is:", total)  # This line should print the total
print("-----------------------------------------")

# Task 2: Create and modify a global variable
score = 0  # This is your global variable

def update_score():
    # Add 10 points to the score
    global score
    score += 10

def double_score():
    # Double the current score
    global score
    score *= 2

update_score()
print(score)
double_score()
print(score)

print("-----------------------------------------")

# # Task 3: Understanding variable shadowing
name = "Alex"

def change_name():
    name = "Sam"  # This creates a local variable
    print("Inside function:", name)

change_name()
print("Outside function:", name)

print("-----------------------------------------")

# # Task 4: Using the global keyword
counter = 0

def increment_counter():
    # Use the global keyword to modify the counter
    global counter
    # Add 1 to counter
    counter += 1

def display_counter():
    # Print the current value of the counter
    print(f"Counter: {counter}")

display_counter()
increment_counter()
display_counter()
