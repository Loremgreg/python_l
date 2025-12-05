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
            if item == item_name:
                self.items.remove(item)
                break

    # Calculate and return the total quantity of items in the shopping cart
    def calculate_total(self):
        total = 0
        for item in self.items:
            if qty:
                total += 1
        return total

# Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
add = cart.add_item("Apple", 2)
print(cart.items)


# Display the current items in the cart and calculate the total quantity




# Remove an item from the cart, display the updated items, and recalculate the total quantity
