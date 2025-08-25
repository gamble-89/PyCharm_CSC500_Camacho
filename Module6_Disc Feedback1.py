shopping_list = []
while True:
    item = input("Enter item (or type 'done' to finish): ").lower()  # Convert to lowercase for error handling
    if item == "done":  # Check for lowercase 'done'
        break
    shopping_list.append(item)
    print("Current Shopping List:", shopping_list)
print("Final Shopping List:", shopping_list)
