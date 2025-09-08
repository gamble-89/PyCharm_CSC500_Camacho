"""
This is a culminating project adding additional functionality to the online shopping cart project by utilizing
new methods and classes to enhance the shopping cart experience for the user.
Enhancements will include a new object to prompt for the customers name and current date, replacing
a previous hard-coded function. Final enhancements include modifying the Change Item Quantity Menu Option
to only prompt the user for new quantity, replacing a previous function prompting the user to re-enter all item data.
"""

# Start of the Online Shopping Cart Program

# Creating the ItemToPurchase class needed to model each item in the shopping cart
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
# The ShoppingCart class is needed to handle the customer name/date, and add/remove operations from the menu
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Designed a parameterized constructor per requirements to take customer name/date as parameters
        # Creates an empty list to store customer items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # New method to add new items to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # New method to by-name remove items from the shopping cart
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
                # Update only the provided fields; keep all others as-is
                if item.item_price != 0.0:  # Check if new price provided (non-default)
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:  # Check if new quantity provided
                    cart_item.item_quantity = item.item_quantity
                if item.item_description != "No description":  # Check if new description provided
                    cart_item.item_description = item.item_description
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Creating a method to calculate the total number of items in the shopping cart
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # Creating a method to calculate the total cost of all items in the shopping cart
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
    # Prompt for the customer name and date, then output them both as strings for simplicity
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create ShoppingCart with user inputs
    cart = ShoppingCart(customer_name, current_date)

    while True:
        print_menu()
        choice = print_menu_choice()
        if choice == 'q':
            break # Exits the loop and finishes the program if the customer decides to quit w/ a "q" selection
        elif choice == 'a':
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter the item name:\n")
            new_item.item_description = input("Enter the item description:\n")
            new_item.item_price = float(input("Enter the item price:\n"))
            new_item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(new_item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c': # Creating a new ItemToPurchase class for performance and better handling of change requests
            item_name = input("Enter the item name:\n")
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(new_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please try again.")
# End of the Online Shopping Cart Program