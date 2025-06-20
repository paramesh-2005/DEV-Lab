import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Users\PARAMESHWARAN\Downloads\Lab\DEV\weekly_temperatures.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month name
df['Month'] = df['Date'].dt.strftime('%B')

# Group by City and Month, then sum temperatures
monthly_sum = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()

# Pivot to reshape: City as rows, Months as columns
pivot_table = monthly_sum.pivot(index='City', columns='Month', values='Temperature').fillna(0)

print("Month-wise total temperature per city:\n")
print(pivot_table)

# Define summer months
summer_months = ['June', 'July', 'August']

# Add summer total column
pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)

# Find city with highest summer temperature
hottest_city = pivot_table['Summer_Total'].idxmax()
max_temp = pivot_table['Summer_Total'].max()

print(f"\nCity with highest total temperature in summer months: {hottest_city} ({max_temp:.1f}°C)")
