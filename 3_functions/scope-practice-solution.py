# Task 1: Fix the scope error (Solution 1 - Moving print inside function)
def calculate_total():
    subtotal = 50
    tax = 0.1
    total = subtotal + (subtotal * tax)
    print("The total is:", total)

calculate_total()

# Task 2: Create and modify a global variable
score = 0

def update_score():
    global score
    score += 10

def double_score():
    global score
    score *= 2

# Test Task 2
print("Initial score:", score)
update_score()
print("After update:", score)
double_score()
print("After double:", score)

# Task 3: Understanding variable shadowing
name = "Alex"

def change_name():
    name = "Sam"  # This creates a local variable
    print("Inside function:", name)

change_name()
print("Outside function:", name)

# Task 4: Using the global keyword
counter = 0

def increment_counter():
    global counter
    counter += 1

def display_counter():
    print("Counter value:", counter)

# Test Task 4
display_counter()
increment_counter()
display_counter()
