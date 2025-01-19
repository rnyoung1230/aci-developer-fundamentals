# Starter Code for Weekly Sales Data

# Step 1: Create a dictionary to store weekly sales data for a pet store.
# Data: "Monday": 8, "Tuesday": 12, "Wednesday": 5, "Thursday": 7, "Friday": 15, "Saturday": 20, "Sunday": 10
sales_wk1 = {"Monday": 8, "Tuesday": 12, "Wednesday": 5, "Thursday": 7, "Friday": 15, "Saturday": 20, "Sunday": 10}

# Step 2: Loop through the dictionary and print only the keys (days of the week).
# Example output: "Monday"
for day in sales_wk1:
    print(day)

print("------------------------------")

# Step 3: Loop through the dictionary and print only the values (number of sales).
# Example output: "8"
for sales in sales_wk1.values():
    print(sales)

print("------------------------------")

# Step 4: Loop through the dictionary to print both keys and values.
# Example output: "Monday: 8"
for days, sales in sales_wk1.items():
    print(f"{day}: {sales}")

print("------------------------------")

# Step 5: Calculate the total sales for the week by accessing values directly.
# Print the total sales.
# total_sales = 0
#
# for sales in sales_wk1.values():
#     total_sales += sales
#
# print(f"Total sales: {total_sales}")
# print("------------------------------")
total_sales = 0

for day in sales_wk1:
    total_sales += sales_wk1[day]

print(f"Total sales: {total_sales}")
print("------------------------------")