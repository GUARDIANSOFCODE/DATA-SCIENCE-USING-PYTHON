import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data from CSV File
try:
    # Load the CSV file, handling bad lines
    df = pd.read_csv('country_data_large_150.csv', 
                     header=0,  # Ensure the header is read correctly
                     on_bad_lines='skip')  # Skip bad lines to avoid warnings
    print("\nSample Data:")
    print(df.head())
except Exception as e:
    print(f"Error loading CSV: {e}")

# Proceed with your data analysis and visualization if df is successfully loaded
if 'df' in locals():
    # Check if required columns exist in the DataFrame
    required_columns = ['Age', 'Wages', 'City', 'Employees', 'Population_Density', 'Medicare_Eligibility']
    
    if all(col in df.columns for col in required_columns):
        # Step 2: Data Analysis and Visualization

        # Create an Age Group column
        df['Age_Group'] = pd.cut(df['Age'], bins=[30, 35, 40], labels=['30-35', '35-40'])

        # Line Chart: Average Wage by Age Group
        avg_wage_by_age = df.groupby('Age_Group')['Wages'].mean()

        plt.figure(figsize=(10, 5))
        avg_wage_by_age.plot(kind='line', marker='o', color='blue')
        plt.title("Average Wage by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Average Wages")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Bar Chart: Number of Employees by City
        employee_by_city = df.groupby('City')['Employees'].sum().sort_values(ascending=False).head(10)  # Show top 10 cities

        plt.figure(figsize=(10, 5))
        employee_by_city.plot(kind='bar', color='skyblue')
        plt.title("Top 10 Cities by Number of Employees")
        plt.xlabel("City")
        plt.ylabel("Number of Employees")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

        # Scatter Plot: Wages vs. Population Density
        plt.figure(figsize=(10, 5))
        plt.scatter(df['Population_Density'], df['Wages'], alpha=0.5, color='purple')
        plt.title("Wages vs. Population Density")
        plt.xlabel("Population Density")
        plt.ylabel("Wages")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Pie Chart: Medicare Eligibility Distribution
        medicare_count = df['Medicare_Eligibility'].value_counts()

        plt.figure(figsize=(8, 8))
        medicare_count.plot(kind='pie', labels=['Eligible', 'Not Eligible'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
        plt.title("Medicare Eligibility Distribution")
        plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
        plt.tight_layout()
        plt.show()

        # Histogram: Population Density Distribution
        plt.figure(figsize=(10, 5))
        plt.hist(df['Population_Density'], bins=30, edgecolor='black', color='orange')
        plt.title("Population Density Distribution")
        plt.xlabel("Population Density")
        plt.ylabel("Frequency")
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    else:
        print("One or more required columns are missing in the DataFrame.")
