
# Create Dictionary
team_info = {"team": "Denver Broncos"}

# Insert via assignment
team_info["division"] = "AFC West"
print("After assignment:", team_info)

# Update method for multiple inserts
team_info.update({"stadium": "Empower Field at Mile High", "super_bowls": 2})
print("After update:", team_info)  # Output: {'team': 'Denver Broncos', 'division': 'AFC West', 'stadium': 'Empower Field at Mile High', 'super_bowls': 2}

# Updating Elements to correct Super Bowl Wins
team_info["super_bowls"] = 3  # Update the number of Super Bowls
print("After updating super_bowls:", team_info)  # Output: {'team': 'Denver Broncos', 'division': 'AFC West', 'stadium': 'Empower Field at Mile High', 'super_bowls': 3}

# Updating Multiple Elements
team_info.update({"team": "Tampa Bay Buccaneers", "division": "NFC South"})  # Update team and division as an example
print("After updating multiple:", team_info)  # Output: {'team': 'Tampa Bay Buccaneers', 'division': 'NFC South', 'stadium': 'Empower Field at Mile High', 'super_bowls': 3}

# Removing Elements
# Del: Delete the stadium key-value pair
del team_info["stadium"]
print("After del:", team_info)  # Output: {'team': 'Tampa Bay Buccaneers', 'division': 'NFC South', 'super_bowls': 3}