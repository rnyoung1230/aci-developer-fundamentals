# Global variables for tracking game statistics
high_score = 0
current_score = 0
player_stats = {}

def calculate_round_score(base_points, multiplier=1, *bonus_points):
    score = pow(base_points, multiplier)
    if bonus_points:
        score += sum(bonus_points)
    return score

def update_high_score():
    global high_score, current_score
    high_score = max(high_score, current_score)
    return high_score

def record_player_stats(player_name, **stats):
    cleaned_stats = {
        key: abs(value) for key, value in stats.items()
    }
    player_stats[player_name] = cleaned_stats

def generate_report(player_name):
    if player_name not in player_stats:
        return None
    
    stats = player_stats[player_name]
    wins = stats.get('wins', 0)
    rounds = stats.get('rounds_played', 0)
    losses = stats.get('losses', 0)
    win_percentage = (wins / rounds * 100) if rounds > 0 else 0
    
    return f"""
Player: {player_name}
Rounds Played: {rounds}
Wins: {wins}
Losses: {losses}
Win Percentage: {win_percentage:.1f}%
"""

# Test the functionality
print("Testing round score calculation:")
print(calculate_round_score(100))  # Base points only
print(calculate_round_score(100, 2))  # With multiplier
print(calculate_round_score(100, 2, 10, 20, 30))  # With bonus points

print("\nTesting high score update:")
current_score = 1000
print(f"New high score: {update_high_score()}")

print("\nTesting player stats recording and reporting:")
record_player_stats("Player1", rounds_played=10, wins=7, losses=3)
print(generate_report("Player1"))
