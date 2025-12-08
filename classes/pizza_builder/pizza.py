class Pizza: 
# 1. Define a Pizza class that stores:
# - size, crust type, and a list of toppings
    def __init__(self, size, crust, toppings=None):
        self.size = size
        self.crust = crust
        self.toppings = toppings if toppings else []


# 2. Add a method to add a new topping
    def add_topping(self, topping):
        self.toppings.append(topping)

# 3. Add a method to remove a topping if it exists
    def remove_topping(self, topping):
        self.toppings.remove(topping)

    def pizza_details(self):
        print("\n🍕 ===== Your Pizza =====")
        print(f"Size: {self.size.title()}")
        print(f"Crust type: {self.crust.title()}")
        if self.toppings:
            for topping in self.toppings:
                print(f"   - {topping}")
        else:
            print("No topping added")
            

# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)

# 5. Create a pizza object, customize it, and print the summary
my_pizza = Pizza("large", "thin")
my_pizza.add_topping("pepperoni")
my_pizza.add_topping("mushrooms")
my_pizza.add_topping("onions")
my_pizza.remove_topping("onions")
my_pizza.pizza_details()

# second pizza
friend_pizza = Pizza("medium", "deep dish", ["bacon", "extra cheese"])
friend_pizza.add_topping("olives")
friend_pizza.pizza_details()
