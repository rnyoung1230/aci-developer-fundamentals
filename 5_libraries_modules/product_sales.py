"""
This module contains classes for tracking
product and sales data.
"""

class Product:

    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        return f"Product {self.name} is priced at ${self.price} and has a remaining inventory of {self.inventory}."

class Sales:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product, quantity):
        sale = {"product": product, "quantity": quantity}

        self.sales_data.append(sale)

    def generate_report(self):
        total_sale_value = 0
        products_summary = {}
        widget_info = {}

        for sale in self.sales_data:
            product = sale["product"]
            quantity = sale["quantity"]

            # Determine total value (dollars) of all sales
            this_sale_value = product.price * quantity
            total_sale_value += this_sale_value

            if product.name not in products_summary:
                revenue = product.price * quantity
                widget_info["quantity"] = quantity
                widget_info["revenue"] = revenue
                products_summary[product.name] = widget_info
            else:
                quantity1 = products_summary[product.name]["quantity"]
                revenue1 = products_summary[product.name]["revenue"]
                new_quantity = quantity1 + quantity
                new_revenue = revenue1 + this_sale_value
                products_summary[product.name]["quantity"] = new_quantity
                products_summary[product.name]["revenue"] = new_revenue

        print(products_summary)
        print(f"Total Sale Value: ${total_sale_value}")


########################## TEST PRODUCT & SALES CLASS ##########################
product_1 = Product("Widget A", 1.25, 20)
#print("Product 1:", product_1)
# print(repr(product_1))

product_2 = Product("Widget B", 3.50, 10)
#print("Product 2:", product_2)
# print(repr(product_2))

sale_1 = Sales()
sale_1.add_sale(product_1, 5)
sale_1.add_sale(product_2, 8)
sale_1.add_sale(product_2, 2)
sale_1.add_sale(product_1, 13)

sale_1.generate_report()


