# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read CSV File
# Make sure the CSV file is in the correct directory or provide the full path
df = pd.read_csv('/mnt/data/iris.csv')
print(df.head())  # Print first few rows to check the data

# Step 2: Extract Unique Species from the Data
species_list = df['Species'].unique()
print("Species:", species_list)

# Step 3: Calculate Average Sepal Length for Each Species
avg_sepal_length = []
for species in species_list:
    avg = df['SepalLengthCm'][df['Species'] == species].mean()
    avg_sepal_length.append(avg)

# Define Font Settings for Plot Titles
font = {'fontname': 'Arial', 'color': 'Blue', 'size': 15}

# Step 4: Create Visualizations

# Line Plot for Average Sepal Length
plt.subplot(2, 3, 1).set_title("Line Plot", fontdict=font)
plt.plot(species_list, avg_sepal_length, marker='o')
for i, avg in zip(species_list, avg_sepal_length):
    plt.annotate(f"({round(avg, 2)})", xy=(i, avg))  # Annotate with average values

# Bar Plot for Average Sepal Length
plt.subplot(2, 3, 2).set_title("Bar Plot", fontdict=font)
plt.bar(species_list, avg_sepal_length, color='skyblue')

# Scatter Plot for Average Sepal Length
plt.subplot(2, 3, 3).set_title("Scatter Plot", fontdict=font)
plt.scatter(species_list, avg_sepal_length, color='purple')

# Step 5: Calculate Average Sepal Width for Each Species
avg_sepal_width = []
for species in species_list:
    avg = df['SepalWidthCm'][df['Species'] == species].mean()
    avg_sepal_width.append(avg)

# Horizontal Bar Plot for Average Sepal Width
plt.subplot(2, 3, 4).set_title("Horizontal Bar Plot", fontdict=font)
plt.barh(species_list, avg_sepal_width, color='orange', height=0.3)

# Histogram of Sepal Length Data
plt.subplot(2, 3, 5).set_title("Histogram", fontdict=font)
plt.hist(df['SepalLengthCm'], bins=10, color='green', edgecolor='black')

# Pie Chart of Average Sepal Width Distribution
plt.subplot(2, 3, 6).set_title("Pie Chart", fontdict=font)
plt.pie(avg_sepal_width, labels=species_list, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])

# Step 6: Adjust Layout and Show All Plots
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
