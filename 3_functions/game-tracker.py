# Global variables for tracking game statistics
from email.policy import default

high_score = 0
current_score = 1500
player_stats = {}

# Task 1: Create a function that calculates player's round score
def calculate_round_score(base_points, multiplier = 1, *bonus_points):
   # print(type(bonus_points))
    bonus_points_sum = 0
    for points in bonus_points:
        bonus_points_sum += points

    total_score = base_points * multiplier + bonus_points_sum

    # Return the total score
    return total_score

# Test calculate_round_score()
print(f"Round score: {calculate_round_score(100)}")
print(f"Round score: {calculate_round_score(100, 2)}")
print(f"Round score: {calculate_round_score(100, 2, 10, 20, 30)}")

print("---------------------------------------------")
# Task 2: Update the high score if necessary
def update_high_score():
    global high_score
    global current_score

    print(f"Current high_score: {high_score}")
    return max(current_score,high_score)

# Test update_high_score()
print(f"Updated high score: {update_high_score()}")

print("---------------------------------------------")
# Task 3: Track player statistics
def record_player_stats(player_name, **stats):

    global player_stats

    player_stats[player_name] = stats
    print(player_stats)

# Test record_player_stats
record_player_stats("Susan", rounds_played=10, wins=7, losses=3)
record_player_stats("Bob", rounds_played=5, wins=4, losses=1)

print("---------------------------------------------")
# Task 4: Generate player report
def generate_report(player_name):

    global player_stats

    if player_stats.get(player_name) is None:
        print("Player doesn't exist.")
    else:
        print(f'Player name: {player_name}')
        for k, v in player_stats[player_name].items():
            print(f'{k}: {v}')

        win_percentage = (player_stats[player_name]["wins"]/player_stats[player_name]["rounds_played"])*100
        print(f'win percentage: {win_percentage}')

# Test generate_report
generate_report("Sam")
