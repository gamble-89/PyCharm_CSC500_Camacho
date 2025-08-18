# Point award system modified to include 1, 3, 5, 7 books purchased

# Prompt the user to input the number of books they purchased this month
books_purchased = int(input("Enter the number of books you purchased this month: "))

# Determine points based on the number of books the student purchased
if books_purchased == 0 or books_purchased == 1:
    points = 0
elif books_purchased == 2 or books_purchased == 3:
    points = 5
elif books_purchased == 4 or books_purchased == 5:
    points = 15
elif books_purchased == 6 or books_purchased == 7:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0 # any negative integer

# Display the number of points awarded
print(f"Number of points awarded: {points}")

# End of Program