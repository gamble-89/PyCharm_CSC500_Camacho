import random

# Function to simulate one adjustment process (uses while loop)
def simulate_adjustment():
    current_efficiency = 0.0
    adjustment_angle = 1.0
    iteration_count = 0
    efficiencies = []  # List to store efficiency at each step
    angles = []  # List to store angle at each step
    while current_efficiency < 98.0:
        adjustment_angle += 1.0  # Adjust angle first
        efficiency_increase = random.uniform(5, 15)
        current_efficiency = min(98.0, current_efficiency + efficiency_increase)
        efficiencies.append(current_efficiency)
        angles.append(adjustment_angle)
        iteration_count += 1
    return efficiencies, angles, iteration_count

# Run one simulation and use for loop to print a summary table
efficiencies, angles, total_iterations = simulate_adjustment()
print("Starting satellite solar array adjustment...")
print("Initial efficiency: 0.00%")
print("-" * 40)
print("Iteration | Angle (degrees) | Efficiency (%)")
for i in range(len(efficiencies)):
    print(f"{i+1:<9} | {angles[i]:<15.1f} | {efficiencies[i]:.2f}")
print("-" * 40)
print(f"Optimal alignment achieved after {total_iterations} iterations.")
print(f"Final efficiency: {efficiencies[-1]:.2f}%")
print(f"Final adjustment angle: {angles[-1]:.1f} degrees.")

# Use for loop to run multiple simulations and calculate average iterations
num_simulations = 5
iteration_counts = []
for _ in range(num_simulations):
    _, _, count = simulate_adjustment()
    iteration_counts.append(count)
average_iterations = sum(iteration_counts) / num_simulations
print(f"\nAverage iterations over {num_simulations} simulations: {average_iterations:.2f}")
