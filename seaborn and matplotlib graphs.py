import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Histogram of Sepal Length
sns.histplot(data["sepal_length"], bins=20)

# KDE Plot with Shaded Area
sns.kdeplot(data["sepal_length"], shade=True)

# Rug Plot
sns.rugplot(data["sepal_length"])

# Box Plot of Sepal Length
sns.boxplot(x=data["sepal_length"])

# Violin Plot of Sepal Length by Species
sns.violinplot(x=data["species"], y=data["sepal_length"])

# ECDF Plot
sns.ecdfplot(data["sepal_length"])

# Show all plots
plt.show()
