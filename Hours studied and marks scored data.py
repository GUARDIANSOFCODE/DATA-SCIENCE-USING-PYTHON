import matplotlib.pyplot as plt
# Hours studied and marks scored data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [50, 52, 55, 60, 65, 70, 75, 78, 80, 85]

# Creating the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(hours_studied, marks, color='green')
plt.title("Hours Studied vs Marks Scored")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
