import matplotlib.pyplot as plt
# Test scores for three groups
group_a = [55, 60, 65, 70, 75, 80, 85]
group_b = [50, 55, 60, 65, 70, 75, 80]
group_c = [45, 50, 55, 60, 65, 70, 75]

# Creating the box plot
plt.figure(figsize=(8, 6))
plt.boxplot([group_a, group_b, group_c], labels=['Group A', 'Group B', 'Group C'])
plt.title("Comparison of Test Scores Across Groups")
plt.ylabel("Scores")
plt.show()
