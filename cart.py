from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_price(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_cart(self):
        print("Cart contents:")
        for item in self.cart_items:
            item.display_info()
