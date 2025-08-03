# This is a program to calculate what time it will be on a 24-hour alarm clock when it goes off
# The program will prompt the user for the current time and how many hours they would like to wait
# The program will then display the result

# Prompt the user for the time now and how long they want to wait (in hours 0-23)
time_now = int(input("Enter the current time (in hours, 0-23): "))
hours_to_wait = int(input("Enter the number of hours to wait for the alarm (in hours, 0-23): "))

# Define total hours and calculate the future time after waiting
total_hours = (time_now + hours_to_wait) % 24

# Output the result on a 24-hour clock
print(f"\nThe time when the alarm goes off will be: {total_hours}00")

