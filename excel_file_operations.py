import pandas as pd

# Step 1: Read the Excel file
file_path = 'C:/Users/Sankalp Sharma/Documents/dsai 6- 10 practicals/large_employee_data.xlsx'
data = pd.read_excel(file_path)

# Step 2: Display the first few rows of the data
print("Original Data:")
print(data.head())

# Step 3: Perform some operations
# Example: Calculate average salary
average_salary = data['Salary'].mean()
print(f"\nAverage Salary: {average_salary}")

# Example: Filter employees older than 30
older_employees = data[data['Age'] > 30]
print("\nEmployees older than 30:")
print(older_employees)

# Example: Save the filtered data to a new Excel file
filtered_file_path = 'C:/Users/Sankalp Sharma/Documents/dsai 6- 10 practicals/filtered_employees.xlsx'
older_employees.to_excel(filtered_file_path, index=False)

print(f"\nFiltered data saved to: {filtered_file_path}")
