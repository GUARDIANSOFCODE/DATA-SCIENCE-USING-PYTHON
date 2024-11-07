import matplotlib.pyplot as plt 
# Monthly sales data
months = ['January', 'February', 'March', 'April', 'May']
sales = [300, 350, 200, 400, 450]

# Creating the bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='purple')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.show()
