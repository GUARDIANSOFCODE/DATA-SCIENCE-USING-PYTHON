import matplotlib.pyplot as plt

Months=["January","February","March","April","May"]
Sales=[300,350,200,400,450]

plt.bar(Months,Sales,color="green",label="MonthlySales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()    
