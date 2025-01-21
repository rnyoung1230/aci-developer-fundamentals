# Create a list of numbers and a list of fruits.
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

# Problem 1: Adding Elements to a List
numbers.append(60)
fruits.insert(0, "mango")
print("Problem 1 - Numbers:", numbers)  # Output: [10, 20, 30, 40, 50, 60]
print("Problem 1 - Fruits:", fruits)   # Output: ['mango', 'apple', 'banana', 'cherry']

# Problem 2: Removing Elements from a List
fruits.remove("banana")
numbers.pop()  # Removes the last element
print("Problem 2 - Numbers:", numbers)  # Output: [10, 20, 30, 40]
print("Problem 2 - Fruits:", fruits)    # Output: ['mango', 'apple', 'cherry']

# Problem 3: Extending and Sorting a List
fruits.extend(["peach", "pear"])
fruits.sort()
print("Problem 3 - Fruits:", fruits)  # Output: ['apple', 'cherry', 'mango', 'peach', 'pear']

# Problem 4: Combining List Methods
copied_numbers = numbers.copy()
copied_numbers.append(100)
copied_numbers.reverse()
print("Problem 4 - Original Numbers:", numbers)  # Output: [10, 20, 30, 40]
print("Problem 4 - Copied Numbers:", copied_numbers)  # Output: [100, 40, 30, 20, 10]

# Problem 5: Complex Manipulation
grocery_list = ["milk", "bread", "eggs", "butter", "cheese"]
grocery_list.append("yogurt")
grocery_list.remove("butter")
egg_index = grocery_list.index("eggs")
grocery_list.insert(egg_index, "juice")
grocery_list.sort()
print("Problem 5 - Grocery List:", grocery_list)  # Output: ['bread', 'cheese', 'eggs', 'juice', 'milk', 'yogurt']