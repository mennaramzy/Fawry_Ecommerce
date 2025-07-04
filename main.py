
class Item:
    def __init__(self, title, cost, stock, perishable=False, shippable=False, mass=0, expired=False):
        self.title = title
        self.cost = cost
        self.stock = stock
        self.perishable = perishable
        self.shippable = shippable
        self.mass = mass
        self.expired = expired

    def is_available(self, amount):
        return amount <= self.stock and (not self.perishable or not self.expired)


class User:
    def __init__(self, username, wallet):
        self.username = username
        self.wallet = wallet


class ShoppingCart:
    def __init__(self):
        self.contents = {}

    def add_item(self, item, quantity):
        if item.is_available(quantity):
            self.contents[item] = self.contents.get(item, 0) + quantity
        else:
            print(f"❌ Cannot add {item.title}, not enough stock or expired.")

    def is_empty(self):
        return not self.contents


class DeliveryService:
    @staticmethod
    def prepare(items):
        print("\n== Shipping Details ==")
        total_mass = 0
        for item, qty in items.items():
            if item.shippable:
                print(f"{qty} x {item.title} - {item.mass * qty}g")
                total_mass += item.mass * qty
        print(f"Total shipment weight: {total_mass / 1000:.2f} kg\n")
        return 30 if total_mass > 0 else 0


def process_checkout(user, shopping_cart):
    if shopping_cart.is_empty():
        print("❌ Your cart is empty!")
        return

    subtotal = 0
    for item, qty in shopping_cart.contents.items():
        if not item.is_available(qty):
            print(f"❌ {item.title} is out of stock or expired.")
            return
        subtotal += item.cost * qty

    shipping_fee = DeliveryService.prepare(shopping_cart.contents)
    total_due = subtotal + shipping_fee

    if user.wallet < total_due:
        print("❌ Not enough balance!")
        return

    user.wallet -= total_due

    print("== Receipt ==")
    for item, qty in shopping_cart.contents.items():
        print(f"{qty} x {item.title}: {item.cost * qty}")
        item.stock -= qty

    print("-------------------------")
    print(f"Subtotal:       {subtotal}")
    print(f"Shipping Fee:   {shipping_fee}")
    print(f"Total:          {total_due}")
    print(f"Remaining Wallet: {user.wallet}")


# Products
item1 = Item("Cheese", 100, 5, perishable=True, shippable=True, mass=200)
item2 = Item("Biscuits", 150, 3, perishable=True, shippable=True, mass=700)
item3 = Item("TV", 3000, 2, perishable=False, shippable=True, mass=8000)
item4 = Item("Scratch Card", 50, 10, shippable=False)

# Customer
main_user = User("Ali", 5000)

# Valid cart
main_cart = ShoppingCart()
main_cart.add_item(item1, 2)
main_cart.add_item(item2, 1)
main_cart.add_item(item3, 1)
main_cart.add_item(item4, 1)
process_checkout(main_user, main_cart)

# Test Case 1: Empty Cart
print("\n-- Test 1: Empty Cart --")
empty_cart = ShoppingCart()
process_checkout(main_user, empty_cart)

# Test Case 2: Insufficient Balance
print("\n-- Test 2: Low Balance --")
low_user = User("Omar", 100)
small_cart = ShoppingCart()
small_cart.add_item(item3, 1)
process_checkout(low_user, small_cart)

# Test Case 3: Expired Product
print("\n-- Test 3: Expired Product --")
expired_item = Item("Expired Cheese", 90, 2, perishable=True, shippable=True, mass=300, expired=True)
cart2 = ShoppingCart()
cart2.add_item(expired_item, 1)
process_checkout(main_user, cart2)

# Test Case 4: Out of Stock
print("\n-- Test 4: Out of Stock --")
limited_item = Item("Few Biscuits", 50, 1)
cart3 = ShoppingCart()
cart3.add_item(limited_item, 2)
process_checkout(main_user, cart3)
