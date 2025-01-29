my_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)

setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}

#setB.update(setA)
setA.update(setB)

print(f"Set A: {setA}")
print(f"Set B: {setB}")

insects = {"ant", "bee", "cricket", "dragonfly"}

# discard()
insects.discard("ant")
print('After discard("ant"), the insects sets is:', insects)

# remove()
# remove raises an error if the specified element is not in the set
insects.remove("bee")  #changed ant to bee
print("After remove(), the insects set includes:", insects)
# e-learning code - working with Sets

# my_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
#
# my_set = set(my_list)
#
# print (my_set)

# setA = {"Python", "JavaScript", "PHP"}
# setB = {"Python", "JavaScript", "Java", "C++"}
#
# #setB.update(setA)
# setA.update(setB)
#
# print (f"Set A: {setA}")
# print (f"Set B: {setB}")

# insects = {"ant", "bee", "cricket", "dragonfly"}
#
# # discard()
# insects.discard("ant")
# print ('After discard("ant"), the insects sets is:', insects)
#
# # remove()
# # remove raises an error if the specified element is not in the set
# insects.remove("ant")  #change ant to some other set value and rerun
# print("After remove(), the insects set includes:", insects)

# insects = {"ant", "bee", "cricket", "dragonfly"}
#
# # pop removes a random element and returns that value
# removed_item = insects.pop()
# print ("The removed element is", removed_item)
# print ("The remaining set includes", insects)

sizes_avail = {'S', 'M', 'L', 'XL', 'XXL'}
sizes_needed = {'XS', 'S', 'M', 'L', 'XL', 'XXL'}

print(sizes_needed.issubset(sizes_avail))
print(len(sizes_avail - sizes_needed) >= 0)

