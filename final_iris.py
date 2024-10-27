import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read CSV File
df = pd.read_csv('/mnt/data/iris.csv')
print(df.head())

# Step 2: Create DataFrame and Extract Species Unique Values
species_list = df['Species'].unique()
print(species_list)

# Calculate Average Sepal Length for Each Species
avg_sepal_length = []
for species in species_list:
    avg = df['SepalLengthCm'][df['Species'] == species].mean()
    avg_sepal_length.append(avg)

# Setting Font for Titles
font = {'fontname': 'Arial', 'color': 'Blue', 'size': 15}

# Line Plot
plt.subplot(2, 3, 1).set_title("Line Plot", fontdict=font)
plt.plot(species_list, avg_sepal_length, marker='o')
for i, avg in zip(species_list, avg_sepal_length):
    plt.annotate(f"({round(avg, 2)})", xy=(i, avg))

# Bar Plot
plt.subplot(2, 3, 2).set_title("Bar Plot", fontdict=font)
plt.bar(species_list, avg_sepal_length, color='skyblue')

# Scatter Plot
plt.subplot(2, 3, 3).set_title("Scatter Plot", fontdict=font)
plt.scatter(species_list, avg_sepal_length, color='purple')

# Horizontal Bar Plot for Average Sepal Width
avg_sepal_width = []
for species in species_list:
    avg = df['SepalWidthCm'][df['Species'] == species].mean()
    avg_sepal_width.append(avg)

plt.subplot(2, 3, 4).set_title("Horizontal Bar Plot", fontdict=font)
plt.barh(species_list, avg_sepal_width, color='orange', height=0.3)

# Histogram using Sepal Length Data
plt.subplot(2, 3, 5).set_title("Histogram", fontdict=font)
plt.hist(df['SepalLengthCm'], bins=10, color='green', edgecolor='black')

# Pie Chart with Average Sepal Width
plt.subplot(2, 3, 6).set_title("Pie Chart", fontdict=font)
plt.pie(avg_sepal_width, labels=species_list, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])

# Show All Plots
plt.tight_layout()
plt.show()
