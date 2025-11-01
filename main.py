from product_manager import ProductManager
from product import Product
import random

def main():
    pm = ProductManager()

    # Adaugă produse arbitrare
    pm.add_product(Product("PC", 3000, 5))
    pm.add_product(Product("Headset", 50, 10))
    pm.add_product(Product("Keyboard", 150, 7))
    pm.add_product(Product("Display", 800, 4))

if __name__ == "__main__":
    main()