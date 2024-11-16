import csv

# Open the file in read mode
with open("data.csv", mode='r') as file:
    csv_reader = csv.reader(file)  # Create a CSV reader object
    for row in csv_reader:         # Iterate over the rows in the CSV file
        print(row)                 # Print each row
