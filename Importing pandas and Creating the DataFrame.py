import pandas as pd
# Create the DataFrame
Sales = pd.DataFrame({
    2014: [100, 150, 200, 30000, 40000],
    2015: [12000, 18000, 28000, 30000, 45000],
    2016: [20000, 50000, 70000, 100000, 125000],
    2017: [50000, 60000, 70000, 80000, 90000]
}, index=['Madhu', 'Kusum', 'Krishan', 'Ankit', 'Shruti'])

# Display row labels
print("Row labels:\n", Sales.index)

# Display column labels
print("\nColumn labels:\n", Sales.columns)

# Display sales for 2017
print("\nSales in 2017:\n", Sales[2017])

# Display dimensions, shape, size and values
print("\nDimensions:", Sales.ndim)
print("Shape:", Sales.shape)
print("Size:", Sales.size)
print("Values:\n", Sales.values)

# Delete data for 2014
Sales = Sales.drop(2014, axis=1)
print("\nDataFrame after deleting 2014 data:\n", Sales)

# Transpose the DataFrame
Sales_transposed = Sales.T
print("\nTransposed DataFrame:\n", Sales_transposed)
