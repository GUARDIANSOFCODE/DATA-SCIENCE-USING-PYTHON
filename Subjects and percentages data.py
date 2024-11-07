import matplotlib.pyplot as plt
# Subjects and percentages data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
percentages = [25, 30, 20, 15, 10]

# Creating the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=subjects, autopct='%1.1f%%', startangle=140)
plt.title("Student Preferences for Different Subjects")
plt.show()
