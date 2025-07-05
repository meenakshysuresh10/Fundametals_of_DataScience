import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1200, 1100, 1500, 1700, 1600]

# Set figure size
plt.figure(figsize=(10, 4))

# 1. Line Plot
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')

# 2. Bar Plot
plt.subplot(1, 2, 2)
plt.bar(months, sales, color='pink')
plt.title('Monthly Sales (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')

# Layout adjustment and display
plt.tight_layout()
plt.show()
