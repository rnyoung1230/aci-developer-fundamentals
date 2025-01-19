# Step 1: Create a dictionary to store weekly sales data for a pet store.
sales_wk1 = {
    "Monday": 8,
    "Tuesday": 12,
    "Wednesday": 5,
    "Thursday": 7,
    "Friday": 15,
    "Saturday": 20,
    "Sunday": 10
}

# Step 2: Loop through the dictionary and print only the keys (days of the week).
print("Days of the week:")
for day in sales_wk1:
    print(day)

# Step 3: Loop through the dictionary and print only the values (number of sales).
print("\nNumber of sales each day:")
for sales in sales_wk1.values():
    print(sales)

# Step 4: Loop through the dictionary to print both keys and values.
print("\nSales data (day and number of sales):")
for day, sales in sales_wk1.items():
    print(f"{day}: {sales}")

# Step 5: Calculate the total sales for the week by accessing values directly.
total_sales = 0
for day in sales_wk1:
    total_sales += sales_wk1[day]

print(f"\nTotal sales for the week: {total_sales}")