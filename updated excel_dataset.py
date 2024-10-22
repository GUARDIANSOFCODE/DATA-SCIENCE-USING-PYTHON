import pandas as pd

# Load the employee dataset
file_path = 'C:/Users/Sankalp Sharma/Documents/dsai 6- 10 practicals/large_employee_data.xlsx'  # Update the file path
data = pd.read_excel(file_path)

# Display original data
print("Original Data:")
print(data)

# Summary statistics for employees older than 30
filtered_data = data[data['Age'] > 30]
summary_stats = filtered_data[['Salary']].describe()  # Removed Bonus
print("\nSummary Statistics for Employees Older Than 30:")
print(summary_stats)

# Sorting by Salary
sorted_by_salary = filtered_data.sort_values(by='Salary', ascending=False)

# Display sorted data
print("\nEmployees Older Than 30 Sorted by Salary:")
print(sorted_by_salary[['Name', 'Age', 'Country', 'Occupation', 'Salary']].head())  # Display top 5

# Save filtered and sorted data to a new Excel file
output_path = 'C:/Users/Sankalp Sharma/Documents/dsai 6- 10 practicals/sorted_employees.xlsx'
sorted_by_salary.to_excel(output_path, index=False)

print(f"\nFiltered and sorted data saved to: {output_path}")
