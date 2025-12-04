import sys

class Shopping_cart:
    def __init__(self):
        self.item = []

    def __str__(self):
        return f"List of items: {self.item}"

    def adding_item(self):
        while True:
            try:
                user_item = input("Add item: ")
                self.item.append(user_item)
            except EOFError:
                print("\nItems added to your cart.")
                choice = input("Voulez-vous afficher votre liste d’items ? (yes/no): ").strip().lower()
                if choice == "yes":
                    print(self)
                    choice = input("Voulez-vous supprimer des items? yes/no): ").strip().lower()
                    if choice == "yes":
                        self.removing_item()
                    else:
                        break
                elif choice == "no":
                    choice = input("Voulez-vous supprimer des items? yes/no): ").strip().lower()
                    if choice == "yes":
                        self.removing_item()
                    else:
                        break


    def removing_item(self):
        input_remove = input("Remove: ")
        if input_remove:
            self.item.remove(input_remove)
            print(f"{input_remove} removed from cart") 
        



    def total_price():
        ... 

cart_1 = Shopping_cart()
cart_1.adding_item() # This will now run in an infinite loop
print(cart_1.item)


# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.