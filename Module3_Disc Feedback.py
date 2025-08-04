# Daily fitness metrics: [weekday, steps, miles] for a week
fitness_data_stats = [
        ['Monday', 8423, 4.2], # Miles = steps / 2000 ~approximately
        ['Tuesday', 10325, 5.2],
        ['Wednesday', 7641, 3.8],
        ['Thursday', 9820, 4.9],
        ['Friday', 11045, 5.5],
        ['Saturday', 9378, 4.7],
        ['Sunday', 10567, 5.3]
]

# Calculate average steps and total miles
avg_steps = sum(day[1] for day in fitness_data_stats) / len(fitness_data_stats)
total_miles = sum(day[2] for day in fitness_data_stats)
print(f"Average steps: {avg_steps:.2f}")
print(f"Total miles ran: {total_miles:.2f}")
