# Global variables for tracking game statistics
high_score = 0
current_score = 0
player_stats = {}

# Task 1: Create a function that calculates player's round score
def calculate_round_score(base_points, multiplier = 1, *bonus_points):
   # print(type(bonus_points)) --> Tuple
    total_score = pow(base_points, multiplier) + sum(bonus_points)
    # Return the total score
    return total_score

# Task 2: Update the high score if necessary
def update_high_score():
    global high_score, current_score

    print(f"Current high_score: {high_score}")
    return max(current_score,high_score)

# Task 3: Track player statistics
def record_player_stats(player_name, **stats):
    cleaned_stats = {}
    for k, v in stats.items():
        cleaned_stats[k] = abs(v)

    player_stats[player_name] = cleaned_stats
    print(player_stats)

# Task 4: Generate player report
def generate_report(player_name):
    if player_stats.get(player_name) is None:
        print("Player doesn't exist.")
    else:
        print(f'Player name: {player_name}')
        for k, v in player_stats[player_name].items():
            print(f'{k}: {v}')

        win_percentage = (player_stats[player_name]["wins"]/player_stats[player_name]["rounds_played"])*100
        print(f'win percentage: {win_percentage}')

# Test calculate_round_score()
print(f"Round score: {calculate_round_score(100)}")
print(f"Round score: {calculate_round_score(100, 2)}")
print(f"Round score: {calculate_round_score(100, 2, 10, 20, 30)}")
print("---------------------------------------------")

# Test update_high_score()
print(f"Updated high score: {update_high_score()}")
print("---------------------------------------------")

# Test record_player_stats
record_player_stats("Susan", rounds_played=10, wins=7, losses=3)
record_player_stats("Bob", rounds_played=-5, wins=-4, losses=-1)
print("---------------------------------------------")

# Test generate_report
generate_report("Susan")
