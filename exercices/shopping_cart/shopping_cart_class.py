class ShoppingCart:
    def __init__(self):
        self.items = []

    # Add an item with a name and quantity to the shopping cart
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    # Remove an item with a specific name from the shopping cart
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    # Calculate and return the total quantity of items in the shopping cart
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

# Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Apple", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

tot_qty = cart.calculate_total()
print("Total quantity: ", tot_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
del_ = cart.remove_item("Apple")
print("Updated items in Cart after removing Apple:")
for item in cart.items:
    print(item[0], "-", item[1])

tot_qty = cart.calculate_total()
print("New quantity: ", tot_qty)
