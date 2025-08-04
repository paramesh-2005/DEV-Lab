import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic employee data
employee_id = range(1, 101)
age = np.random.randint(22, 60, size=100)
gender = np.random.choice(['Male', 'Female'], size=100)
department = np.random.choice(['HR', 'Sales', 'IT', 'Marketing'], size=100)
years_of_experience = np.random.randint(1, 15, size=100)
performance_rating = np.random.randint(1, 6, size=100)
salary = np.random.randint(40000, 120000, size=100)

# Create DataFrame
employee_data = pd.DataFrame({
    'EmployeeID': employee_id,
    'Age': age,
    'Gender': gender,
    'Department': department,
    'YearsOfExperience': years_of_experience,
    'PerformanceRating': performance_rating,
    'Salary': salary
})

# Save to CSV
employee_data.to_csv('employee_data.csv', index=False)

# Read from CSV
employee_data = pd.read_csv('employee_data.csv')

# Data overview
print("\n--- Dataset Info ---")
print(employee_data.info())

print("\n--- Descriptive Statistics ---")
print(employee_data.describe())

print("\n--- Missing Values ---")
print(employee_data.isnull().sum())

# Distribution of Departments
print("\n--- Department Distribution ---")
print(employee_data['Department'].value_counts())

# Plot: Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(employee_data['Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot: Performance rating by department
plt.figure(figsize=(8, 5))
sns.boxplot(x='Department', y='PerformanceRating', data=employee_data, hue='Department', palette='Set3', legend=False)
plt.title('Performance Ratings by Department')
plt.xlabel('Department')
plt.ylabel('Performance Rating')
plt.tight_layout()
plt.show()
