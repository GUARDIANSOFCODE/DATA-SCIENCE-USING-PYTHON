import seaborn as sns
import numpy as np

# Example data
data = np.random.normal(0, 1, size=1000)

# KDE plot
sns.kdeplot(data, kernel="gau")
