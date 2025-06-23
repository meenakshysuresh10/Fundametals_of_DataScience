import pandas as pd

# Step 1: Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['Chennai', 'Bangalore', 'Delhi']
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Export data to CSV file
df.to_csv('people.csv', index=False)
print("Data exported to people.csv")

# Step 4: Import data from the CSV file
df_imported = pd.read_csv('people.csv')
print("Imported Data:")
print(df_imported)
