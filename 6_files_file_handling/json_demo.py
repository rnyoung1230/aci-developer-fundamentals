import json

order_dictionary = {
  "orders": [
    {
      "orderId": "ABC123",
      "customerInfo": {
        "name": "John Doe",
        "email": "john.doe@example.com"
      },
      "orderDetails": [
        {
          "productId": "PROD001",
          "name": "Product A",
          "quantity": 2,
          "price": 19.99
        },
        {
          "productId": "PROD002",
          "name": "Product B",
          "quantity": 1,
          "price": 29.99
        }
      ],
      "totalAmount": 69.97,
      "paymentMethod": "Credit Card",
      "shippingAddress": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
      }
    }    
  ]
}

# write dictionary to python string

json_string = json.dumps(order_dictionary, indent=4)
print(json_string)

# write dictionary to file using string

# with open('order_data.json', 'w') as json_file:
#   json_file.write(json_string)


# write dictionary directly to file using json library

with open('order_data2.json', 'w') as json_file:
  json.dump(order_dictionary, json_file, indent=2)
