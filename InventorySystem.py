class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def update_quantity(self, amount):
        self.quantity += amount

    def get_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_inventory_value(self):
        total_value = sum(product.get_value() for product in self.products)
        return total_value


def main():
    inventory = Inventory()

    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Phone", 500, 20)

    inventory.add_product(product1)
    inventory.add_product(product2)

    product1.update_quantity(-2)
    product2.update_quantity(5)

    for product in inventory.products:
        print(product.display_product_info())

    print(f"Total Inventory Value: {inventory.total_inventory_value()}")

main()
