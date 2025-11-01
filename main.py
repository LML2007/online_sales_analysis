from cart import Cart
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

    # Lucru cu coș
    cart = Cart()

    # Adaugă 3 produse alese aleator din stoc
    selected_products = random.sample(pm.products, 3)
    for prod in selected_products:
        cart.add_product(prod)

    cart.display_cart()
    print(f"Total cart price: {cart.total_price()}")

if __name__ == "__main__":
    main()