import csv
import pandas as pd

# Data to write using both methods
data = [
    ["name", "age", "city"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 22, "Chicago"]
]
     
# Using csv module
with open("output_csv.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Using pandas 
df = pd.DataFrame({
    "name": ["John", "Alice", "Bob"],
    "age": [25, 30, 22],
    "city": ["New York", "Los Angeles", "Chicago"]
})

df.to_csv("output_pandas.csv", index=False)

print("Data written successfully using both csv and pandas.")
