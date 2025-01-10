print('He told me, "You should learn Python!"')

first_name = "Terry"
last_name = "Whitlock"
print(first_name + " " + last_name)

name = 'Rob'
age = 53
location = "Madison, WI"
print(f'Hello, my name is {name}. I am {age} and live in {location}.')

# .format() function as alternative to f-string
print("Hello, my name is {}. I am {} and live in {}.".format(name, age, location))


# Indexing
language = "python"
print(language[1])
print(language[4])

# Slicing
my_string = "Hello, World!"
print(my_string[2:5])

my_string = "Hello, World!"
print(my_string[:5])

my_string = "Hello, World!"
print(my_string[2:])

my_string = "Python is awesome!"
# Extract the word "awesome" using slicing
print(my_string[10:17])

# Extract the phrase "Python is"
print(my_string[:9])

# Extract everything from the word "is" to the end of the string
print(my_string[7:])

# (Bonus): Reverse the entire string using slicing
print(my_string[10:17] + " " + my_string[7:9] + " " + my_string[:6] + my_string[17])

# Task 4 (Bonus): Reverse the entire string
# Use slicing with a step of -1 to reverse the string

reversed_string = my_string[::-1]
print(reversed_string)  # Expected output: !emosewa si nohtyP

# Comments for learners:
# - Slicing syntax: string[start:end] extracts characters from start index to end index (end not included).
# - Omitting start: string[:end] slices from the start to end-1.
# - Omitting end: string[start:] slices from start to the end of the string.
# - Adding a step: string[start:end:step] specifies how many characters to skip (e.g., -1 reverses the string).

# Modifying strings
my_string = "Hello, World!"
print(my_string.upper())
print(my_string.lower())

my_string = " Hello, World! "
print(my_string)
print(my_string.strip()) # removes white space from beginning and end of string

my_string = "Hello, World!"
print(my_string.replace("Hello", "Hi"))

my_string = " Jjonathan Smith"
print(my_string)
new_string = my_string.strip()
print(new_string)
newer_string = new_string.replace("Jjonathan", "Jonathan")
print(newer_string)

# Concatenating strings
string1 = 'Hello'
string2 = 'World'
newstring = string1 + ', ' + string2 + '! '
print(newstring)

# Formatting strings
zipcode = 98121
userinfo = "My name is Terry, and my zip code is {}."
print(userinfo.format(zipcode))

name = 'Rob'
age = 53
zipcode = 53593
city = "Verona"
userinfo = 'My name is {}. I’m {} years old. My zip code is {}. My city is {}.'
print(userinfo.format(name, age, zipcode, city))

# Escape characters
string= "He said, \"Hello\"."
print(string)

print("Name:\tTerry\nAge:\t28\nJob:\tCloud application developer")