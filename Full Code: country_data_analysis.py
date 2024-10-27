import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Random Data and Save as CSV

data = {
    'Country': np.random.choice(['Country_A', 'Country_B', 'Country_C', 'Country_D'], 1000),
    'City': np.random.choice(['City_X', 'City_Y', 'City_Z', 'City_W'], 1000),
    'Age': np.random.randint(18, 65, 1000),
    'Population_Density': np.random.randint(50, 300, 1000),
    'Wages': np.random.randint(20000, 100000, 1000),
    'Medicare_Eligibility': np.random.choice([True, False], 1000),
    'Employees': np.random.randint(100, 1000, 1000)
}

df = pd.DataFrame(data)
df.to_csv('country_data.csv', index=False)

print("CSV file 'country_data.csv' generated successfully!")

# Step 2: Load Data from CSV File

df = pd.read_csv('country_data.csv')
print("\nSample Data:")
print(df.head())

# Step 3: Data Analysis and Visualization

# Line Chart: Average Wage by Age Group
df['Age_Group'] = pd.cut(df['Age'], bins=[18, 30, 40, 50, 60, 65], labels=['18-30', '30-40', '40-50', '50-60', '60-65'])
avg_wage_by_age = df.groupby('Age_Group')['Wages'].mean()

plt.figure()
avg_wage_by_age.plot(kind='line', marker='o', color='blue')
plt.title("Average Wage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Wages")
plt.grid(True)
plt.show()

# Bar Chart: Number of Employees by City
employee_by_city = df.groupby('City')['Employees'].sum()

plt.figure()
employee_by_city.plot(kind='bar', color='skyblue')
plt.title("Number of Employees by City")
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.grid(axis='y')
plt.show()

# Scatter Plot: Wages vs. Population Density
plt.figure()
plt.scatter(df['Population_Density'], df['Wages'], alpha=0.5, color='purple')
plt.title("Wages vs. Population Density")
plt.xlabel("Population Density")
plt.ylabel("Wages")
plt.grid(True)
plt.show()

# Pie Chart: Medicare Eligibility Distribution
medicare_count = df['Medicare_Eligibility'].value_counts()

plt.figure()
medicare_count.plot(kind='pie', labels=['Eligible', 'Not Eligible'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
plt.title("Medicare Eligibility Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
plt.show()

# Histogram: Population Density Distribution
plt.figure()
plt.hist(df['Population_Density'], bins=30, edgecolor='black', color='orange')
plt.title("Population Density Distribution")
plt.xlabel("Population Density")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

# Stackplot: Distribution of Employees Across Cities Over Time
x = range(5)
city1 = np.random.randint(100, 1000, 5)
city2 = np.random.randint(100, 1000, 5)
city3 = np.random.randint(100, 1000, 5)
city4 = np.random.randint(100, 1000, 5)

plt.figure()
plt.stackplot(x, city1, city2, city3, city4, labels=['City_X', 'City_Y', 'City_Z', 'City_W'], colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.xlabel("Time Period")
plt.ylabel("Number of Employees")
plt.legend(loc='upper left')
plt.title("Employees Distribution Across Cities Over Time")
plt.grid(True)
plt.show()

# Boxplot: Wages Distribution by City
plt.figure()
df.boxplot(column='Wages', by='City')
plt.title('Wages Distribution by City')
plt.suptitle("")  # Suppress the automatic title
plt.xlabel("City")
plt.ylabel("Wages")
plt.grid(axis='y')
plt.show()

# Hexbin: Wages vs. Age
plt.figure()
plt.hexbin(df['Age'], df['Wages'], gridsize=30, cmap='Blues', bins='log')
plt.colorbar(label='log10(N)')
plt.xlabel('Age')
plt.ylabel('Wages')
plt.title('Hexbin Plot: Wages vs Age')
plt.grid(True)
plt.show()

print("Data Analysis and Visualization Completed!")
