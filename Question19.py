# Case Study 19: Sales and Profit Analysis
df = pd.read_csv('sales_data.csv')
df['Total Sales'] = df['Quantity Sold'] * df['Unit Price']
product_sales = df.groupby('Product').agg({'Total Sales': 'sum'}).reset_index()
product_sales['Profit'] = product_sales['Total Sales'] * 0.20
overall_profit = product_sales['Profit'].sum()
top_products = product_sales.nlargest(5, 'Profit')
print("Total Sales per Product:")
print(product_sales.sort_values('Total Sales', ascending=False).to_string(index=False))
print(f"\nOverall Company Profit: ${overall_profit:,.2f}")
print("\nTop 5 Profitable Products:")
print(top_products[['Product', 'Profit']].to_string(index=False))
