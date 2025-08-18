discount_applies = False
while not discount_applies:
    try:
        age = int(input("How old are you? "))
        student = input("Are you a student? (y/n): ").lower() == 'y'
        if student or age > 65:
            discount_applies = True
            print("10% Discount applies, enjoy!")
        else:
            print("No discount, try again!")
    except ValueError:
        print("Please enter a valid age!")
