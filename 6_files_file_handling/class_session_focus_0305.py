# SPOTLIGHT SESSION - 3/5
# FILES AND FILE HANDLING CONT.
# ------------------------

import requests, json

#API url
url = f"https://official-joke-api.appspot.com/random_joke"

#send the HTTP request
response = requests.get(url)

# figure out what we are working with
print(type(response))
# get a list of attributes and methods we might be able to use
print(dir(response))

# view response
print(type(response.text))
print(response.text)


# the response.text is a <string> format,
# convert from a json formatted string to a python dictionary


# interact with dictionary


import json

class PlayerCharacter:
    def __init__(self, name, level, occupation, stats):
        self.name = name
        self.level = level
        self.occupation = occupation
        self.stats = stats

def pc_from_json(json_string):
    data = json.loads(json_string)
    return PlayerCharacter(**data)

# Usage
json_string = '{"name": "Cronk", "level": 30, "occupation": "Bodyguard", "stats": [18,12,10,13,16,14]}'
pc = pc_from_json(json_string)

print(f'{pc.name}: {pc.occupation}({pc.level})')
print(pc.stats)