# Starter sets for practice
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}

# Problem 1: Adding and Removing Elements
fruits.add("lime")
fruits.remove("mango")
print("Problem 1 - Updated Fruits:", fruits)  
# Output: {'banana', 'orange', 'lime', 'lemon'}

# Problem 2: Checking Membership and Clearing a Set
is_carrot_in_vegetables = "carrot" in vegetables
vegetables.clear()
print("Problem 2 - Is 'carrot' in vegetables?", is_carrot_in_vegetables)  
# Output: True
print("Problem 2 - Cleared Vegetables:", vegetables)  
# Output: set()

# Problem 3: Copying and Creating New Sets
fruits_copy = fruits.copy()
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}  # Reset vegetables
vegetables.update(["spinach", "kale"])
print("Problem 3 - Copied Fruits Set:", fruits_copy)  
# Output: {'banana', 'lime', 'lemon', 'orange'}
print("Problem 3 - Updated Vegetables Set:", vegetables)  
# Output: {'tomato', 'potato', 'cabbage', 'onion', 'carrot', 'spinach', 'kale'}

# Problem 4: Removing Items with `pop()`
removed_item = fruits.pop()
print("Problem 4 - Randomly Removed Item:", removed_item)  
# Output: Random item from fruits
print("Problem 4 - Updated Fruits Set:", fruits)  

# Problem 5: Clearing a Set
fruits.clear()
print("Problem 5 - Cleared Fruits Set:", fruits)  
# Output: set()