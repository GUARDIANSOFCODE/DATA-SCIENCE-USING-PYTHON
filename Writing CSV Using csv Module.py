import csv

# Data to be written to CSV file
data = [
    ["name", "age", "city"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 22, "Chicago"]
]

# Open the file in write mode ('w')
with open("output_csv.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the data to the file
    writer.writerows(data)

print("Data written successfully using csv module.")
