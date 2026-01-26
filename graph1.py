import matplotlib.pyplot as plt

#Line plot

x = [1,2,5,8,11,41]

y = [4,7,8,12,34,65]

plt.plot(x,y)

#title
plt.title("LinePlot")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

#features of graphs

data1 = [1,3,6,9,12,16]

data2 = [4,6,9,12,19,24]

plt.plot(data1,data2,color="blue",marker="v")
plt.plot(data1,data2,color="red",marker=".")
plt.plot(data1,data2,color="yellow",marker="o")

plt.legend()

plt.xlabel("x")
plt.ylabel("y")

#adding a grid

plt.grid()

plt.show()
