# Import Pandas library
import pandas as pd

# Modifying my mod 3 discussion post to implement panda dataframes in place of arrays
team_stats = [
    [17, 12, 5, 30],   # Player 1
    [29, 10, 10, 25],  # Player 2
    [44, 15, 3, 40],   # Player 3
    [12, 7, 8, 20],    # Player 4
    [81, 10, 6, 35],   # Player 5
]

# Create a Pandas DataFrame from the list of lists
stats_df = pd.DataFrame(team_stats, columns=['Jersey', 'Goals', 'Assists', 'Shots on Goal'])

# Print the DataFrame
print(stats_df)

# Calculate the total team goals
total_goals = stats_df['Goals'].sum()
print(f"Total team goals: {total_goals}")

# Filter and display players with more than 10 goals
high_scorers_10 = stats_df[stats_df['Goals'] > 10]
print("\nCS Tigers High scorers > 10 goals:")
print(high_scorers_10)
