user = {"name": "Alex", "points": 12}
for key in user:
    print(f"{key}: {user[key]}")
    if input(f"Would you like to change the {key}? (y/n): ").lower() == 'y':
        user[key] = input(f"Enter new {key}: ")
print("Updated user:", user)
