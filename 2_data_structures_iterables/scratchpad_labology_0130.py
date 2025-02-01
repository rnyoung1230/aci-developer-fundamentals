# LABOLOGY SESSION - 1/30
# --------------------
#
# # Krishna's Game
# countries = {
#     "USA": ["New York", "Los Angeles", "Chicago"],
#     "UK": ["London", "Manchester", "Birmingham"],
#     "France": ["Paris", "Nice"]
# }
#
# countries_copy = {}
# countries_copy.update(countries)
# print(countries_copy)
# print("---------------------------------")
#
# # two ways of adding a new element to the list
# countries["USA"].append("Boston")
# print(countries)
#
# countries["USA"] += ["San Francisco"]
# print(countries)
# print("---------------------------------")
#
# # count of cities in the UK
# print(len(countries["UK"]))
# print("---------------------------------")
#
# # replace LA with Dallas
# countries["USA"][1] = "Dallas"
# print(countries["USA"])
# print("---------------------------------")
#
# # two ways to add a new country - Germany with cities of Munich, Berlin, and Hamburg
# countries["Germany"] = ["Munich", "Berlin", "Hamburg"]
# print(countries)
#
# countries.update({"Germany": ["Munich", "Berlin", "Hamburg"]})
# print(countries)
#
# recipes = {
#     "Pasta": {
#         "ingredients": ["spaghetti", "tomato sauce", "mushrooms", "garlic", "olive oil"],
#         "instructions": ["Boil pasta", "Heat sauce", "Mix together"],
#         "prep time": 15,
#         "cook time": 20
#     },
#     "Pancakes": {
#         "ingredients": ["flour", "milk", "eggs", "butter"],
#         "instructions": ["Mix batter", "Heat pan", "Cook pancakes"],
#         "prep time": 10,
#         "cook time": 15
#     }
# }
#
# # print each recipe and its ingredients using a loop
# for each_recipe in recipes:
#     print(each_recipe, recipes[each_recipe]["ingredients"])

# Jason's Game
# Construct and print a sudoku puzzle grid
'''
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
------+------+------
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
------+------+------
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
9 1 5 | 3 4 2 | 6 7 8
------+------+------
'''
import random

set_divider = "|"
row_divider = "---------+---------+---------"

counter = 0
while counter < 9:
    row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(row)
    for i in range(len(row)):
        if i == 3 or i == 6:
            print(set_divider, end="")
            print(f" {row[i]} ", end="")
        else:
            print(f" {row[i]} ", end="")

    print("")
    counter += 1
    if counter == 3 or counter == 6:
        print(row_divider)

