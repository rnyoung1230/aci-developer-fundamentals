# SPOTLIGHT SESSION - 2/4
# ------------------------

# Additional practice for Nested Data Structures

# Exercise 1 - Movie Database
movies = {
"Action": ["Die Hard", "Mad Max: Fury Road", "The Dark Knight"],
"Comedy": ["Bridesmaids", "The Hangover", "Anchorman"],
"Drama": ["The Godfather", "Schindler's List", "Forrest Gump"]
}

'''
Questions
1. What would movies["Action"][1] print? --> Mad Max: Fury Road
2. What would movies["Comedy"][-1] print? --> Anchorman
3. What would movies["Drama"][3] print? --> Index error
4. How do you add a new movie "Inception" to the Action list? --> movies["Action"].append("Inception")
5. How do you check if "The Godfather" is in the Drama list? --> "The Godfather" in movies["Drama"]
6. Write a for loop to iterate through the movies data structure and print the keys and values.
'''
# print(movies)
# print(movies["Action"][1]) #1
# print(movies["Comedy"][-1]) #2
# #print(movies["Drama"][3]) #3
# movies["Action"].append("Inception") #4
# print(movies["Action"])
# print("The Godfather" in movies["Drama"]) #5
#
# for k, v in movies.items(): #6
#     print(k, v)

# Exercise 2 - School Grades
grades = {
"Math": {"Alice": 85, "Bob": 92, "Charlie": 78},
"Science": {"Alice": 90, "Bob": 88, "David": 95},
"English": {"Bob": 91, "Charlie": 89, "David": 87}
}

'''
Questions
1. What would grades["Math"]["Bob"] print? --> 92
2. What would grades["Science"]["Charlie"] print? --> No key found
3. How do you add a new student "Eve" with a grade of 93 in Math? --> grades["Math"]["Eve"] = 93
4. How do you check if "David" has a grade in English?
5. How do you update Bob's grade in English to 93?
6. How do you add a new subject "History" with grades {"Alice": 88, "Charlie": 92}?
7. How do you remove David's grade from Science?
8. Write a for loop to iterate through the grades data structure and print the keys and values.
'''
# print(grades["Math"]["Bob"]) #1
# # print(grades["Science"]["Charlie"]) #2 --> Key error
#
# print(grades)
# grades["Math"]["Eve"] = 93 #3
# print(grades)
#
# print("David" in grades["English"]) #4
#
# print(grades)
# grades["English"]["Bob"] = 93 #5
# print(grades)
#
# grades["History"] = {"Alice": 88, "Charlie":92} #6
# print(grades)
#
# grades["Science"].pop("David") #7
# print(grades)
#
# for k, v in grades.items(): #8
#     print(k, v)

# Exercise 3 - Recipe Book
recipes = {
"Pasta": {
"ingredients": ["spaghetti", "tomato sauce", "garlic", "olive oil"],
"instructions": ["Boil pasta", "Heat sauce", "Mix together"],
"prep_time": 15,
"cook_time": 20
},
"Pancakes": {
"ingredients": ["flour", "milk", "eggs", "butter"],
"instructions": ["Mix batter", "Heat pan", "Cook pancakes"],
"prep_time": 10,
"cook_time": 15
}
}

'''
Questions
1. What would recipes["Pasta"]["ingredients"][2] print? --> garlic
2. What would recipes["Pancakes"]["cook_time"] print? --> 15
3. How do you add a new ingredient "cheese" to the Pasta recipe?
4. How do you check if "milk" is in the Pancakes ingredients?
5. How do you update the prep_time of Pancakes to 12 minutes?
6. How do you add a new recipe "Salad" with ingredients ["lettuce", "tomato", "cucumber"],
instructions ["Chop vegetables", "Mix in bowl"], prep_time 10, and cook_time 0?
7. Write a for loop to get the following output using f-strings:
    Pasta : ['spaghetti', 'tomato sauce', 'garlic', 'olive oil']
    Pancakes : ['flour', 'milk', 'eggs', 'butter']
'''

print(recipes["Pasta"]["ingredients"][2]) #1
print(recipes["Pancakes"]["cook_time"]) #2

print(recipes)
recipes["Pasta"]["ingredients"].append("cheese") #3
print(recipes)

print("milk" in recipes["Pancakes"]["ingredients"]) #4

print(recipes["Pancakes"]["prep_time"])
recipes["Pancakes"]["prep_time"] = 12 #5
print(recipes["Pancakes"]["prep_time"])

print(recipes) #6
recipes["Salad"] = {
    "ingredients": ["lettuce", "tomato", "cucumber"],
    "instructions": ["Chop vegetables", "Mix in bowl"],
    "prep_time" : 10,
    "cook_time": 0}
print(recipes)

for k, v in recipes.items(): #7
    print(f"{k}: {v["ingredients"]}")




