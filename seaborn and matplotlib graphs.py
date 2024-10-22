import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.histplot(data["sepal_length"],bins=20)
sns.kdeplot(data["sepal_length"],shade=True)
sns.rugplot(data["sepal_length"])
sns.boxplot(x=data["sepal_length"])
sns.violinplot(x=data["species"],y=data["sepal_length"])
sns.ecdfplot(data["sepal_length"])
plt.show()
