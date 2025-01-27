# e-learning code - working with tuples

# Unpacking tuples
"""
Each transaction record includes:
item name (str)
quantity (int)
date (str)
price (float)
"""
purchase = ("product-1", 2, "6-1-2023", 5.99)

item = purchase[0]
quantity = purchase[1]
print(item)
print(quantity)