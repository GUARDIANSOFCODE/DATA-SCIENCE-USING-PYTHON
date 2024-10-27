import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
a=pd.read_csv('Iris.csv') 
print(a) 
b=pd.DataFrame(a) 
SLC=[] 
xpoints=b.Species.unique() 
print(xpoints) 
for i in range(3): 
 arr=b["SepalLengthCm"][(b['Species'] == xpoints[i])] 
 arr = arr.to_numpy() 
 c=np.average(arr) 
 SLC.append(c) 
f={'font':'Arial','color':'Blue','size':15} 
# Line PLot 
plt.subplot(2,3,1).set_title("Line Plot", fontdict=f) 
plt.legend(title="Sepal Length") 
for i in zip(xpoints, SLC): 
 plt.annotate(f"({round(i[1],2)})",xy=i) 
plt.plot(xpoints, SLC) 
#Barplot 
plt.subplot(2,3,2).set_title("Bar Plot",fontdict=f) 
plt.legend(title="Sepal Length") 
plt.bar(xpoints, SLC) 
#Scatter Plot 
plt.subplot(2,3,3).set_title("Scatter Plot",fontdict=f) 
plt.legend(title="Sepal Length") 
plt.scatter(xpoints,SLC) 
SLC=[] 
for i in range(3): 
 arr=b["SepalWidthCm"][(b['Species'] == xpoints[i])] 
 arr = arr.to_numpy() 
 c=np.average(arr) 
 SLC.append(c) 
#Horizontal Bar Plot 
p1 = np.array(['A','B','C','D']) 
q1= np.array([78,30,49,23]) 
plt.subplot(2,3,4).set_title("Bar Plot", fontdict=f) 
plt.legend(title="Sepal Width") 
plt.barh(xpoints,SLC,height = 0.1) 
#Histograph 
n1 = np.random.normal(170,10,20) 
plt.subplot(2,3,5).set_title("Histograph",fontdict=f) 
plt.legend(title="Sepal Width") 
plt.hist(n1) 
#Pie Plot 
plt.subplot(2,3,6).set_title("Pie Plot",fontdict=f) 
plt.legend(title="Sepal Width") 
plt.pie(SLC, labels=xpoints) 
plt.show()
