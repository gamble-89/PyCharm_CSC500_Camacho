# Program to calculate the average rainfall over a period of years

# Prompt the user for the number of years they would like to analyze
total_years = int(input("Enter the number of years you would like to analyze: "))

# Initialize list for per/month data collection
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Initialize counters for total rainfall and total months
total_rainfall = 0
total_months = 0

# Outer loop to iterate once for each year
for year in range(total_years):
    # Inner loop to iterate once for each month (12 months per year)
    for month in range(12):
        # Initialize rainfall data collection for each month using month name for clarity
        rainfall = float(input(f"Enter rainfall (in inches) for year {year + 1}, {months[month]}: "))
        total_rainfall += rainfall
        total_months += 1

# Initialize and calculate average rainfall per month
average_rainfall = total_rainfall / total_months

# Display # of months, total inches of rainfall, average rainfall per month (entire period)
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# End of rainfall calculator program
