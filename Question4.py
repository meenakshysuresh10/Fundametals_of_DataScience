import numpy as np

# Quarterly sales data: [Q1, Q2, Q3, Q4]
sales_data = np.array([15000, 18000, 21000, 25000])

# Total sales for the year
total_sales = np.sum(sales_data)

# Percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# Output the results
print(f"Total Sales for the Year: ${total_sales}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")

