from product_manager import ProductManager
from product import Product
import random

def main():
    pm = ProductManager()

    # Adaugă produse arbitrare
    pm.add_product(Product("Laptop", 3000, 5))
    pm.add_product(Product("Mouse", 50, 10))
    pm.add_product(Product("Keyboard", 150, 7))
    pm.add_product(Product("Monitor", 800, 4))

    # Afișare produse și total
    pm.display_products()
    print(f"Total inventory value: {pm.total_value()}")

if __name__ == "__main__":
    main()