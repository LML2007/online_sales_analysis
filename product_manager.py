from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for p in self.products:
            p.display_info()

    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)

    def remove_product_by_name(self, name):
        for product in self.products[:]:
            if product.name == name:
                self.products.remove(product)