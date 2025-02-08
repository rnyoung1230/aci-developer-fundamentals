# Global variables for tracking game statistics
high_score = 0
current_score = 0
player_stats = {}

# Task 1: Create a function that calculates player's round score
def calculate_round_score():
    # Parameters: base_points, multiplier=1, *bonus_points
    # Use pow() for multiplier and add sum of bonus points
    # Return the total round score
    pass

# Task 2: Update the high score if necessary
def update_high_score():
    # Use global keyword for high_score and current_score
    # Use max() to compare current_score with high_score
    # Update high_score if current_score is higher
    pass

# Task 3: Track player statistics
def record_player_stats():
    # Parameters: player_name, **stats
    # Stats should include: rounds_played, wins, losses
    # Use abs() to ensure all stats are positive numbers
    # Store in player_stats dictionary
    pass

# Task 4: Generate player report
def generate_report():
    # Parameter: player_name
    # Return None if player not found
    # Calculate win percentage (wins / rounds_played)
    # Return formatted string with player stats
    pass
