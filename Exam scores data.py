import matplotlib.pyplot as plt
# Exam scores data
scores = [55, 60, 45, 70, 65, 80, 85, 60, 55, 50, 90, 75, 65, 55, 85, 70, 95, 85, 75, 60]

# Creating the histogram
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=10, color='orange', edgecolor='black')
plt.title("Distribution of Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()
