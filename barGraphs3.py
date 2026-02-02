import matplotlib.pyplot as plt

data = ["January","March","May","July","October","December"]

data2 = [6,9,18,6,9,10]
data3 = [9,1,20,17,13,19]

plt.bar(data,data3,color="red",edgecolor="black",linewidth=2,width=0.65)
plt.bar(data,data2,color="green",edgecolor="black",linewidth=2,width=0.65)
plt.title("rainOverTheMonths")
plt.xlabel("months")
plt.ylabel("rain")

plt.show()
