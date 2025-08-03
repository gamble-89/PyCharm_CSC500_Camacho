# Module 3 discussion Array Scenario:
# Real life example of storing jersey number, goals, assists, and shots on goal for my kids 12U hockey team
# Create a list of lists to store stats for 5 players
# Each sublist contains [jersey_number, goals, assists, shots_on_goal]

team_stats = [
    [17, 12, 5, 30],   # Player 1: Jersey #17 12 goals, 5 assists, 30 shots
    [29, 8, 10, 25],   # Player 2: Jersey #29   ""
    [96, 15, 3, 40],   # Player 3: Jersey #96   ""
    [92, 7, 8, 20],    # Player 4: Jersey #92   ""
    [8, 10, 6, 35]     # Player 5: Jersey #8    ""
]

# Print the current team stats in a user/fan friendly format
print("Colorado Springs Tigers 12UA Team Stats:")
for player in team_stats:
    print(f"#{player[0]} {player[1]} goals, {player[2]} assists, {player[3]} shots on goal")

# Example of updating #29's goals (index 1) by adding 2 more shots & goals
team_stats[1][1] = team_stats[1][1] + 2  # Increase goals scored from 8 to 10
team_stats[1][3] = team_stats[1][3] + 2  # Increase shots on goal from 25 to 27
print("\nUpdated team stats after #29 scores 2 more goals:")
for player in team_stats:
    print(f"#{player[0]} {player[1]} goals, {player[2]} assists, {player[3]} shots on goal")

# Calculate & display total team goals
total_goals = sum(player[1] for player in team_stats)
print("\nTotal team goals as of today:", total_goals)
