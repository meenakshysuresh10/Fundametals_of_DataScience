import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'product_name': ['A', 'B', 'A', 'C', 'B', 'D', 'E', 'A', 'C', 'D'],
    'quantity_sold': [5, 3, 2, 7, 1, 4, 6, 3, 2, 5]
})

# Group by product name, sum quantity sold, and get top 5
top_products = sales_data.groupby('product_name')['quantity_sold'].sum().sort_values(ascending=False).head(5)

# Display the result
print("Top 5 products sold the most:")
print(top_products)
