"""
This project will add additional functionality to the online shopping cart project by utilizing
new methods and classes to enhance the shopping cart experience for the user.
Enhancements will include a menu for the user to interact with such as:
allowing the user to add, remove, and change items as well as
printing the item descriptions of all items in the cart, and/or printing the entire shopping cart with
name, quantities, and price.
"""

# Start of the Online Shopping Cart Program
# Importing datetime to provide the current date to the customer for the shopping cart
from datetime import datetime

# Creating the ItemToPurchase class needed to model each item in the cart
# In this class, we will store item details such as (name, price, quantity, and description)
class ItemToPurchase:
    def __init__(self):
        # Default constructor needed to initialize the before mentioned item details with default values
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "No description"

    def print_item_cost(self):
        # This is creating a method to calculate and print the item cost based on price and quantity provided
        total_cost = self.item_quantity * self.item_price
        # Ensuring the output formatting matches standard currency displays with 2 decimal places
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# Creating the ShoppingCart class to intake the items from the user/customer
# The ShoppingCart class is needed to handle the customer name/date, and add/remove operations
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Designed a parameterized constructor per requirements to take customer name/date as parameters
        # Creates an empty list to store customer items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # New method to add new items to the cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # New method to by-name remove items from the cart
        # Error handling message included to account for an empty shopping cart query (name must also match)
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        # Creating a method to modify the items description, price, and/or quantity of requested or needed
        # If item found by-name, item can be replaced, otherwise output an error handling message
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                self.cart_items[i] = item
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Creating a method to calculate total number of items in the shopping cart
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # Creating a method to calculate total cost of all items in the shopping cart
        # Perform quantity * price calculations for each item, then perform sum operations
        return sum(item.item_quantity * item.item_price for item in self.cart_items)

    def print_total(self):
        # Creating a method to output a summary of all shopping cart items to the customer
        # Error handling included to account for an empty shopping cart query
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        # Creating a method to output all shopping cart item names and their descriptions to the user
        # Error handling included to account for an empty shopping cart query
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")

# Implementing a print menu function for the user with a menu of options to manipulate the shopping cart
# Each option will be represented/accessed by a single character for clarity
def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

# Creating a function to handle the user provided input letter option
# Ensuring the input is flexible with case-insensitivity (more error handling implementation)
def print_menu_choice():
    return input("Choose an option: ").lower()

# Creating the main execution block of the shopping cart program the user will interact with
# Creates the shopping cart and continues to loop until user quits w/ a "q" selection
if __name__ == "__main__":
    # Sets/ensures output of date is the current date when executed
    current_date = datetime.now().strftime("%B %d, %Y") # Formatting (Month day, year)
    cart = ShoppingCart("Chris Camacho", current_date)

    while True:
        print_menu()
        choice = print_menu_choice()
        if choice == 'q':
            break # Exits the loop and finishes the program if the customer decides to quit w/ a "q" selection
        elif choice == 'a':
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter the name of your item: ")
            new_item.item_price = float(input("Enter the price of your item (e.g 15.99): "))
            new_item.item_quantity = int(input("Enter the item quantity (e.g. 3): "))
            new_item.item_description = input("Enter the item description (e.g. sunglasses): ")
            cart.add_item(new_item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove (must match): ")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter name of item to modify (must match): ")
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_price = float(input("Enter the new price of your item (e.g 15.99): "))
            new_item.item_quantity = int(input("Enter the new quantity of your item (e.g. 3): "))
            new_item.item_description = input("Enter the new description of your item (e.g. sunglasses): ")
            cart.modify_item(new_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please try again.")
# End of the Online Shopping Cart Program