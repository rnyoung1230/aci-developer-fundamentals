import json

# open jsonfile
with open('order_data.json', 'r') as json_file:
  # convert jsonfile to dictionary  
  order = json.load(json_file)
# interact with dictionary
print(type(order))
print(order)