########      List Comprehensions example       #####

list1 = [1,2,3,4,5,6]
#we want to create a new list that has squared values from list1
squared = []

#we can create the new list using a for loop or by using a list comprehension

#using a for loop to create the new list
for n in list1:
    squared.append(n**2)

print(squared)

#using a list comprehension to create the new list
square_list = [n**2 for n in list1]

print(square_list)

##### example 2 ######
ages = [ 27, 32, 56, 47, 29]

#we want to create a new list in which each value is 3 times the value of each item in age
three_times = []

#using a loop
for each_age in ages:
    three_times.append(3*each_age)
print(three_times)

#using list comprehension    
triple_ages = [i*3 for i in ages]
print(triple_ages)

########      Dictionary Comprehensions example       #####
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#create empty dictionary
doubles = {}

#using a for loop to create a new dictionary that holds the value and its doubled value
for i in range(len(numbers)):
     doubles[numbers[i]] = numbers[i] * 2

print(doubles)

#using dictionary comprehension
double_values = {num: num*2 for num in numbers}

print(double_values)

# dictionary comprehension using zip
cities = ["Madison", "Chicago", "Los Angeles", "Atlanta", "New York"]
states = ["WI", "IL", "CA", "GA", "NY"]

new_dict = {cities: states for cities, states in zip(cities, states)}

print(new_dict)

