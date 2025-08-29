def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

scores = [75, 40, 98]
print(f"Average score: {calculate_average(scores)}")
