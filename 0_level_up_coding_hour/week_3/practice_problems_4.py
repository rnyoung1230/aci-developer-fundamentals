# PROBLEM 4
"""
Write a program that will use enumerate on the given dictionary to add the keys of the dictionary
into the elements of the given list. The list is initialized to contain all null values.
    game_scores = {'John': 10, 'Alice': 20, 'Bob': 30, 'Eve': 40}
    users = [None, None, None, None] # will give an error if not initialized with values
"""
game_scores = {'John': 10, 'Alice': 20, 'Bob': 30, 'Eve': 40}
print(f"Game scores: {game_scores}")

users = [None, None, None, None]
print(f"Users initialized: {users}")

# Replace None with keys from the game_scores dict
for i, name in enumerate(game_scores):
    print(i, name)
    users[i] = name

print(f"Users populated: {users}")



