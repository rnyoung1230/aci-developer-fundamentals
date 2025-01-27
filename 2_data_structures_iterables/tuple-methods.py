# Starter Code for Practicing Python Tuple Methods and Operations

# Create initial tuples for practice
numbers = (1, 2, 3, 4, 1, 2, 3, 4)
purchase = ("product-1", 2, "6-1-2023", 5.99)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# TASK 1: Count and index elements in a tuple, as follows:
'''
Use the count() method to find how many times 1 appears in the numbers tuple.
Use the index() method to find the position of the first occurrence of 3 in the numbers tuple.
Print the results.
'''
print("------------ TASK 1 ------------")

item_count = numbers.count(1)
print(f"# of times 1 appears: {item_count}")

first_occurrence = numbers.index(3)
print(f"Position of first occurrence of 3: {first_occurrence}")

print("")

# TASK 2: Unpack a tuple (partial), as follows:
'''
Unpack the first two elements of the purchase tuple into variables named item and quantity.
Print the values of item and quantity.
'''
print("------------ TASK 2 ------------")
item = purchase[0]
quantity = purchase[1]

print(f"Item: {item}\nQuantity: {quantity}")
print("")

# TASK 3: Unpack a tuple (full), as follows:
'''
Unpack all elements of the purchase tuple into variables named item, quantity, date, and price.
Print all unpacked variables.
'''
print("------------ TASK 3 ------------")

item, quantity, date, price = purchase
print(f"Item: {item}\nQuantity: {quantity}\nDate: {date}\nPrice: {price}")

print("")

# TASK 4: Join two tuples, as follows:
'''
Use the + operator to combine tuple1 and tuple2 into a new tuple named combo_tuple.
Print the combined tuple.
'''
print("------------ TASK 4 ------------")

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

combo_tuple = tuple1 + tuple2
print("Combo tuple:", combo_tuple)

print("")

# TASK 5: Repeat a tuple, as follows:
'''
Use the * operator to repeat tuple1 three times, creating a new tuple named repeat_tuple.
Print the repeated tuple.
'''
print("------------ TASK 5 ------------")

print("Tuple1:", tuple1)

repeat_tuple = tuple1 * 3
print("Repeat tuple:", repeat_tuple)

print("")