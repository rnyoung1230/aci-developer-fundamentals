# FOCUS SESSION - 1/29
# --------------------

# Nested data structures
# Example 1: Create a data structure that stores the following info
# name, allergic, invited, favorite food
#
# friend = {"name": "John", "allergic": "Y", "invited": "Y", "fav_food": "Pizza"}
# print(friend)
#
# fav_foods = ["pizza", "spaghetti", "ice cream"]
#
# friend["fav_food"] = fav_foods
# print(friend)
#
# print(friend["fav_food"][1])
#
# friend_one = {"name": "Nancy", "allergic": "Y", "invited": "N", "fav_food": ["Pizza", "Fries", "Ice cream", "Soup"]}
# friend_two = {"name": "Mark", "allergic": "N", "invited": "Y", "fav_food": ["Chicken", "Pizza", "Mac and Cheese", "Spaghetti"]}
# friends_list = [friend_one, friend_two]
# print(friends_list)
#
# names = []
# #print(len(friends_list))
# for i in range(len(friends_list)):
#     names.append(friends_list[i]["name"])
#
# print(names)
# print("---------------------------------")

# fav_foods = []
#for i in range(len(friends_list)):
#    fav_foods += friends_list[i]["fav_food"]

# same result using iterable method
# for each_friend in friends_list:
#     fav_foods += each_friend["fav_food"]
#
# print(fav_foods)
#
# fav_foods_deduped = set(fav_foods)
# print(fav_foods_deduped)

# Nest list practice
# nested_list = [
#     [1, 2],
#     [3, 4]
# ]
# print(nested_list)
# print(nested_list[0][0])

employees = {
    "John": {"id": 1234, "tenure": 5, "dept": "Sales"},
    "Jack": {"id": 5678, "tenure": 10, "dept": "IT"}
}
print(employees)

for employee in employees:
    print(f"{employee} works in the {employees[employee]["dept"]} department.")

