# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.stem import PorterStemmer

# Download the NLTK data for the first time
nltk.download('punkt')

# Sample text data for stemming demonstration
text = ["running", "runner", "ran", "easily", "fairly", "fighting"]

# Initialize the stemmer
stemmer = PorterStemmer()

# Initialize a list to store the stemmed words
stemmed_words = []

# Loop through each word in the text data and apply stemming
for word in text:
    # Skip words that start with 'f' using 'continue'
    if word[0] == 'f':
        continue
    # Stop processing if the word is "ran" using 'break'
    if word == "ran":
        break
    # Apply stemming to the word and add it to the list
    stemmed_words.append(stemmer.stem(word))

# Print the stemmed words
print("Stemmed Words:", stemmed_words)

# Generate some sample data for visualization
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # y is the sine of x

# Initialize a list to store filtered data based on control flow
filtered_x = []
filtered_y = []

# Loop through the data to apply conditions with break and continue
for i in range(len(x)):
    if y[i] < 0:  # Skip negative y values using 'continue'
        continue
    if x[i] > 8:  # Break the loop if x is greater than 8
        break
    
    # Add the valid data points to the filtered lists
    filtered_x.append(x[i])
    filtered_y.append(y[i])

# Data visualization with filtered data
plt.figure(figsize=(10, 6))

# Line plot of the filtered data
plt.plot(filtered_x, filtered_y, label='Filtered Sine Wave', color='b', linewidth=2)

# Title and labels
plt.title('Filtered Sine Wave with Break and Continue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
