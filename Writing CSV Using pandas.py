import pandas as pd

# Data to be written to CSV file
data = {
    "name": ["John", "Alice", "Bob"],
    "age": [25, 30, 22],
    "city": ["New York", "Los Angeles", "Chicago"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("output_pandas.csv", index=False)

print("Data written successfully using pandas.")
