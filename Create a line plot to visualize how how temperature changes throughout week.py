import matplotlib.pyplot as plt

day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
temp=[22,21,23,24,22,25,26]

plt.plot(day,temp,label="Day vs Temperature",color="green")
plt.legend(loc="upper right")
plt.show()
