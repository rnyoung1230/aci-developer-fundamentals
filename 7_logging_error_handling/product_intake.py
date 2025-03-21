'''
Write code to import logging and JSON modules. Then, set up a logging configuration that
captures the date and time a log message is written. Capture all messages at the INFO level and higher.
Write logs to a file named prod_validation.log.
'''
import logging
import json

logging.basicConfig(filename="prod_validation.log", filemode="w", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# Now, add a function named parse_products that takes a file_path parameter.
# Write your function so that it meets the following criteria outlined in the # TODO comments in the following code.

def parse_products(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        # Write a "File not found: {file_path}" error to the log
        logging.error("File not found using path {}".format(file_path))
        return []

    products = []

    for product in data:
        if "name" not in product:
            # Write a "Product missing required field: name" error to the log
            logging.error("Product missing required field: name")
            continue
        if "price" not in product:
            # Write a "Product missing required field: price" error to the log
            logging.error("Product missing required field: price")
            continue
        products.append(product)
        # Write an "Added product to inventory: {product['name']}" informational message to the log
        logging.info("Added product to inventory: {}".format(product["name"]))

    return products

# Write validated products list: Create a new function called write_products with two parameters: file_path and product_list,
# where file_path is a string and products is a list. The function should open and write a file to the specified path.
# It should use the dump method from the JSON module to convert the Python object to a JSON object.
def write_products(file_path, products_list):
    with open(file_path, "w") as json_file:
        json.dump(products_list, json_file, indent=4)

# Run the functions: Use the if __name__ == "__main__" pattern to run your two functions, parse_products and write_products.
# Save the result of calling parse_products to a variable, and pass that value to write_products as its second argument.
# You can use any JSON file name for the file_path string for the first argument of write_products, such as "validated_products.json".
if __name__ == "__main__":
    parsed_products = parse_products("prod_sample.json")
    print(parsed_products)
    write_products("validated_products.json", parsed_products)
