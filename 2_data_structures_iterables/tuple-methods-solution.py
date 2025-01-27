# Starter tuples
numbers = (1, 2, 3, 4, 1, 2, 3, 4)
purchase = ("product-1", 2, "6-1-2023", 5.99)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Problem 1: Counting and Indexing Elements in a Tuple
count_of_1 = numbers.count(1)  # Count the number of 1s
index_of_3 = numbers.index(3)  # Find the index of the first 3
print("Problem 1 - Count of 1 in numbers:", count_of_1)  # Output: 2
print("Problem 1 - Index of first 3 in numbers:", index_of_3)  # Output: 2

# Problem 2: Unpacking a Tuple (Partial)
item = purchase[0]
quantity = purchase[1]
print("Problem 2 - Item:", item)  # Output: product-1
print("Problem 2 - Quantity:", quantity)  # Output: 2

# Problem 3: Unpacking a Tuple (Full)
item, quantity, date, price = purchase
print("Problem 3 - Item:", item)  # Output: product-1
print("Problem 3 - Quantity:", quantity)  # Output: 2
print("Problem 3 - Date:", date)  # Output: 6-1-2023
print("Problem 3 - Price:", price)  # Output: 5.99

# Problem 4: Joining Two Tuples
combo_tuple = tuple1 + tuple2
print("Problem 4 - Combined Tuple:", combo_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Problem 5: Repeating a Tuple
repeat_tuple = tuple1 * 3
print("Problem 5 - Repeated Tuple:", repeat_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)