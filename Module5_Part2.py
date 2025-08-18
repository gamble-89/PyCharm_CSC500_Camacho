# Prompt the user to input the number of books they purchased this month
books_purchased = int(input("Enter the number of books you purchased this month: "))

# Determine points based on the number of books the student purchased
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0  # Any pos/neg number not explicitly specified in instructions

# Display the number of points awarded for the Bookstore Purchase Program
print(f"Number of points awarded: {points}")

# End of CSU Global Bookstore Point Calculator Program
