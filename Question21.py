# Case Study 21: Data Cleaning and Transformation
employee_df = pd.read_csv("employee_data.csv")
employee_df['Salary'] = pd.to_numeric(employee_df['Salary'].replace('[\$,]', '', regex=True), errors='coerce')
employee_df = employee_df.dropna(subset=["Department"])
employee_df['First Name'] = employee_df['Full Name'].str.split().str[0]
print(employee_df.head())

# Case Study 22: Time Series Analysis
temp_df = pd.read_csv("temperature_data.csv")
temp_df['Date'] = pd.to_datetime(temp_df['Date'])
temp_df['Month'] = temp_df['Date'].dt.to_period('M')
monthly_avg_temp = temp_df.groupby('Month')['Temperature (Celsius)'].mean().reset_index()
monthly_avg_temp['Month'] = monthly_avg_temp['Month'].dt.to_timestamp()
plt.figure(figsize=(10, 5))
plt.plot(temp_df['Date'], temp_df['Temperature (Celsius)'], label='Daily Temperature')
plt.plot(monthly_avg_temp['Month'], monthly_avg_temp['Temperature (Celsius)'], color='red', label='Monthly Average')
plt.title('Temperature Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (Celsius)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
