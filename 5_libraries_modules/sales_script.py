# Script file leveraging the Product and Sales classes
from product_sales import Product, Sales
import random

# Simulate how you might receive sales data and unpack the values to create and manipulate objects.
product_data = [("widgetA", 5.99, 100), ("widgetB", 10.99, 100),
                ("widgetC",14.99 , 200), ("widgetD", 16.99, 50),
                ("widgetE",14.99 , 125), ("widgetF", 11.99, 75),
                ("widgetG",4.99 , 200), ("widgetH", 17.99, 200),
                ("widgetI",1.99 , 300), ("widgetJ", 13.99, 50)]

def create_product_objects(data):
    products = []
    for product in product_data:
        name, price, inventory = product
        products.append(Product(name, price, inventory))
    return products

def report_sales(product_list):
    sales = Sales()
    for index, product in enumerate(product_list):
        if index % 2 == 0: # check if index is even
            quantity_sold = random.randint(1, 10)
            sales.add_sale(product, quantity_sold)
    return sales.generate_report()

if __name__ == '__main__':
    batch1 = create_product_objects(product_data)
    print(report_sales(batch1))