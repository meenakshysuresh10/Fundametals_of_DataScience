import matplotlib.pyplot as plt

# Monthly data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [150, 200, 250, 300, 280, 350, 400, 420, 390, 450, 470, 500]

# 1. Line Plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('1. Monthly Sales (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(months, sales, color='green')
plt.title('2. Monthly Sales (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# 3. Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='orange')
plt.title('3. Monthly Sales (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
