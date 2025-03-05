"""
This module contains classes for tracking
product and sales data.
"""
import utilities

class Product:

    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        return f"Product: {self.name}\n" \
               f"Unit Price: {utilities.format_currency(self.price)}\n" \
               f"Inventory {self.inventory}\n"

class Sales:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product, quantity):
        sale = {"product": product, "quantity_sold": quantity}

        self.sales_data.append(sale)

    def generate_report(self):
        aggregated_sales_info = {}
        aggregated_sales_info_display = ""
        total_sales_revenue = 0

        # Unpack the list of sales items and format them into a line-by-line item display
        for sale in self.sales_data:
            product = sale.get("product")
            quantity_sold = sale.get("quantity_sold")
            product_revenue = product.price * quantity_sold

            if product.name in aggregated_sales_info:
                details = aggregated_sales_info.get(product.name)
                details[0] += quantity_sold
                details[2] += product_revenue
                aggregated_sales_info.update({product.name: details})
            else:
                aggregated_sales_info[product.name] = [quantity_sold, product.price, product_revenue]

            total_sales_revenue += product_revenue

        for k, v in aggregated_sales_info.items():

            aggregated_sales_info_display += ''.join(f"Product: {str(k).ljust(12, " ")}"
                                     f"Units Sold: {str(v[0]).ljust(6, " ")}"
                                     f"Unit Price: {str(utilities.format_currency(v[1])).ljust(8, " ")}"
                                     f"Revenue: {str(utilities.format_currency(v[2])).ljust(8, " ")}") + '\n'

        report = f"\nPRODUCT SALES SUMMARY\n" \
               f"Total Sales Revenue: {utilities.format_currency(total_sales_revenue)}\n" \
               f"\nSALE DETAILS\n" \
               f"{aggregated_sales_info_display}\n" \
               f"------------------------------------------"

        return report

########################## TEST CODE ##########################

# Create some product objects
prod1 = Product("WidgetA", 10.99, 100)
prod2 = Product("WidgetB", 19.99, 50)
prod3 = Product("WidgetC", 7.99, 150)
prod4 = Product("WidgetD", 3.99, 500)

# Create a sales object
sales = Sales()
sales.add_sale(prod1, 15)
sales.add_sale(prod2, 30)
sales.add_sale(prod3, 45)
sales.add_sale(prod1, 30)
sales.add_sale(prod4, 100)

print(sales.generate_report())





