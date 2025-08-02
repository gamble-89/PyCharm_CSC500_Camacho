# Below is a program that calculates the total amount of a meal purchased at a restaurant
# The program must perform the below three items:
# Ask the user to input total food charge
# Calculate the tip and tax based on pre-defined rates
# Calculate these totals and display all values


# float input needed to ask user for total net charges
total_food_charge = float(input("Enter the charge for the food: $"))

# declaring variables for tip/tax
tip_rate = 0.18
sales_tax = 0.07

tip_total = total_food_charge * tip_rate
sales_tax_total = total_food_charge * sales_tax

# calculating total gross charges
total_price = total_food_charge + sales_tax_total + tip_total

# Display each of these amounts and total price
print(f"\nFood Charge: ${total_food_charge:.2f}")
print(f"18% Tip: ${tip_total:.2f}")
print(f"7% Sales Tax: ${sales_tax_total:.2f}")
print(f"Total Price: ${total_price:.2f}")

