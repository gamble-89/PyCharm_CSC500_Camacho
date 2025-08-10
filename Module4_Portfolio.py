'''
Program below is an online shopping cart. I built a class called ItemToPurchase with the following specs
name(string), price(float), quantity(int). I also need to use a default constructor with the following specs
initializes the item name = none, the price = 0, and the quantity = 0
'''

class ItemToPurchase:
    def __init__(self):
        # Use of a default constructor to set the initial values as specified
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        # Use of a method called print_item_cost to calculate and output the cost for one item
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

if __name__ == "__main__":
    # Prompt the user for two items and create two objects of the ItemToPurchase class
    # Item 1
    item1 = ItemToPurchase()
    print("Item 1")
    # Minor error handling included in user prompt
    item1.item_name = input("Enter the item name (Letters a-z Only): ")
    item1.item_price = float(input("Enter the item price (0-2 Decimal Format Only E.g. 14.75): "))
    item1.item_quantity = int(input("Enter the item quantity (0 Decimal Format Only E.g. 15): "))

    # Item 2
    item2 = ItemToPurchase()
    print("Item 2")
    # Minor error handling included in user prompt
    item2.item_name = input("Enter the item name (Letters a-z Only): ")
    item2.item_price = float(input("Enter the item price (0-2 Decimal Format Only E.g. 14.75): "))
    item2.item_quantity = int(input("Enter the item quantity (0 Decimal Format Only E.g. 15): "))

    # Add the costs of the two items together and output the total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
    print(f"Total: ${total:.2f}")
