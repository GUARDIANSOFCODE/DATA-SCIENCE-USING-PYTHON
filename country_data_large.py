import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data from CSV File
df = pd.read_csv('country_data_large.csv')

print("\nSample Data:")
print(df.head())

# Step 2: Data Analysis and Visualization

# Line Chart: Average Wage by Age Group
df['Age_Group'] = pd.cut(df['Age'], bins=[25, 35, 45, 55, 60], labels=['25-35', '35-45', '45-55', '55-60'])
avg_wage_by_age = df.groupby('Age_Group')['Wages'].mean()

plt.figure(figsize=(10, 6))
avg_wage_by_age.plot(kind='line', marker='o', color='blue')
plt.title("Average Wage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Wages")
plt.grid(True)
plt.show()

# Bar Chart: Number of Employees by City
employee_by_city = df.groupby('City')['Employees'].sum()

plt.figure(figsize=(10, 6))
employee_by_city.plot(kind='bar', color='skyblue')
plt.title("Number of Employees by City")
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)  # Rotate city names for better visibility
plt.grid(axis='y')
plt.show()

# Scatter Plot: Wages vs. Population Density
plt.figure(figsize=(10, 6))
plt.scatter(df['Population_Density'], df['Wages'], alpha=0.5, color='purple')
plt.title("Wages vs. Population Density")
plt.xlabel("Population Density")
plt.ylabel("Wages")
plt.grid(True)
plt.show()

# Pie Chart: Medicare Eligibility Distribution
medicare_count = df['Medicare_Eligibility'].value_counts()

plt.figure(figsize=(8, 8))
medicare_count.plot(kind='pie', labels=['Eligible', 'Not Eligible'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
plt.title("Medicare Eligibility Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
plt.show()

# Histogram: Population Density Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Population_Density'], bins=30, edgecolor='black', color='orange')
plt.title("Population Density Distribution")
plt.xlabel("Population Density")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()
