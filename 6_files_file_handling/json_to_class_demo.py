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