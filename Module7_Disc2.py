def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

scores = [8, 29, 17]
result = sum_list(scores)
print(f"Sum of scores: {result}") 