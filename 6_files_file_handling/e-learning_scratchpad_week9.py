# WEEK 9 - FILES AND FILE HANDLING

# Create a file and write a welcome message to it.
f = open("welcome.txt", "w")
f.write("Hello! Welcome to the Python 1 module. This file is for testing purposes. "
        "Hope you are enjoying this module so far. ")
f.close()
print("File created.")

# # Open the file and print its contents.
f = open("welcome.txt", "r")
print(f.read())
f.close()

# Challenge: Add data to an existing file
f = open("welcome.txt", "a")
f.write("Thank you.")
f.close()

# Challenge: Experiment with adding a size argument to the read() method. Re-run your code and observe the results.
f = open("welcome.txt", "r")
print(f.read(5))
f.close()

# Deleting files
import os

if os.path.exists("welcome.txt"):
        os.remove("welcome.txt")
        print("File deleted.")
else:
        print("The file doesn't exist.")

# Working with JSON

# Import the JSON module
import json

# Define a JSON-formatted string.
x =  '{ "name":"John", "lastname":"Stiles", "city":"Seattle"}'
print(type(x))

# Convert the JSON string into a Python object.
y = json.loads(x)
print(type(y))

# Print the value of 'city'.
print(y["city"])

# Converting from JSON to Python
import json

# Open the JSON file.
f = open('my_data.json', 'r')

# Convert the JSON data into Python.
my_data = json.load(f)
print(type(my_data))

# Close file.
f.close()

# The variable now contains a Python object representing the JSON file data.
print(my_data)

# Converting from Python to JSON
import json

# Define a dictionary with three key-value pairs.
x = {
  "dog": "Jack",
  "breed": "Golden Retriever",
  "city": "Albuquerque"
}
print(type(x))

# Convert dictionary into a JSON string using json.dumps().
#y = json.dumps(x, indent=4) # Use the indent parameter to make the output more readable
y = json.dumps(x, indent=4, separators=(" |", " = ")) # Use the separator parameter to change to the default separator used between the keys and values

# Print output.
print(type(y))
print(y)

# Challenge: Convert Python to JSON
print("\nChallenge: Convert Python to JSON")
'''
Define a Python class called Book with the attributes title and author. 
Create an instance of the class with the title and author of your favorite book. 
Use json.dumps() to convert the attributes of the Book instance to a JSON string. 
Format the string with four spaces of indentation and a colon followed by a space as the 
separator between keys and values. Instead of passing the entire Book object to json.dumps(), 
convert the attributes of the Book instance to a dictionary first because json.dumps() does not 
natively support serializing custom objects. This ensures that the JSON conversion process handles 
the data correctly without requiring additional serialization logic.
'''
class Book:

        def __init__(self, title, author):
                self.title = title
                self.author = author

my_book = Book("The Catcher in the Rye", "J.D. Salinger")

# my_book_dict = {"title": my_book.title, "author": my_book.author}

# # Convert python object to JSON
my_book_json = json.dumps(vars(my_book), indent=4, separators=(", ", ": "))
print(type(my_book_json))
print(my_book_json)

# Looping over dictionaries and JSON
# Import the JSON module
import json

# Define JSON string
x = '{"name": "John", "lastname": "Stiles", "city": "Seattle"}'

# Parse JSON data into a Python dictionary
py_dict = json.loads(x)

# Loop through the Python dictionary
for key, value in py_dict.items():
    print(key, ":", value)

# Challenge: Looping over dictionaries
print("\nChallenge: Looping over dictionaries")
'''
Create a JSON file containing your name, age, and hobbies information. 
Write a Python script that reads the file and prints out each key-value pair in the dictionary. 
Make sure that the script prints each hobby in the hobbies list on a separate line. 
'''
import json

# Open the JSON file.
f = open('my_info.json', 'r')

# Convert the JSON data into Python.
my_info = json.load(f)
print(my_info)

# Display contents of Python dictionary
for k, v in my_info.items():
        if k != "hobbies":
                print(f"{k} : {v}")
        else:
                print("hobbies:")
                for hobby in v:
                        print(f"\t\t{hobby}")
# Close file.
f.close()

# Using input validation
print("\nUsing input validation with jsonschema")
#import json
import jsonschema

# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname" : {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["firstname", "lastname", "age"]
}
# Validate a JSON document against the schema.
document = {
    "firstname": "John",
    "lastname": "Stiles",
    "age": "28"
}
try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)



