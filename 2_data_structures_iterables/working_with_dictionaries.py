# e-learning code - working with Dictionaries
#
# inventory = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2,
#     "dates": 10
# }
#
# inv_keys = inventory.keys()
# inv_values = inventory.values()
# print(inv_keys) # before new key-value is added
# print(inv_values) # before new key-value is added
#
# inventory["elderberries"] = 2
# print(inv_keys)  # after new key-value is added
# print(inv_values) # after new key-value is added
#
# kv_pairs = inventory.items()
# print(kv_pairs)

# inventory = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2,
#     "dates": 10,
# }
#
# inv_keys = inventory.keys()
# new_store_inv = inventory.fromkeys(inv_keys, 0)
# print("The new_store_inv holds these key-value pairs:", new_store_inv)

inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10,
    "avocado": 2,
    "tomatoes": 11
}

key = "apples"
removed_item = inventory.pop(key)
print (f"The item that was removed with pop() was ({key}, {removed_item})")
print("The remaining dictionary items are", inventory)

last_item = inventory.popitem()
print ("The item that was removed with popitem() was", last_item)

print ("The remaining dictionary items are", inventory)