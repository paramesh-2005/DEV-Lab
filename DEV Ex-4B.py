import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Users\PARAMESHWARAN\Downloads\Lab\DEV\employee_hours.csv')

# Group by Department and calculate total and average hours
grouped = df.groupby('Department')['Work_Hours'].agg(Total_Hours='sum', Average_Hours='mean').reset_index()

# Create pivot table (optional since grouped is already a summary)
pivot_table = pd.pivot_table(df, index='Department', values='Work_Hours', aggfunc=['sum', 'mean'])
pivot_table.columns = ['Total_Hours', 'Average_Hours']
pivot_table = pivot_table.reset_index()

# Identify the department with highest average hours
max_avg_row = pivot_table.loc[pivot_table['Average_Hours'].idxmax()]
dept_with_max_avg = max_avg_row['Department']
max_avg_hours = max_avg_row['Average_Hours']

# Display report
print("Department-wise Work Hours Summary:\n")
print(pivot_table)

print(f"\n Department with the highest average working hours: {dept_with_max_avg} ({max_avg_hours:.2f} hours)")
