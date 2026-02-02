import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y,marker=".")
plt.title("data")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

x = [0,1,2,3,4,5]
y = [0,5,10,15,20,25]
plt.plot(x,y,color="red")
plt.title("data")
plt.grid()
plt.show()

x = [1,2,3,4,5]
y = [6,5,7,4,9]
plt.plot(x,y)
plt.title("Weather Tempture over 5 days")
plt.xlabel("Day")
plt.ylabel("°C")
plt.show()


food = ["Chips","Chocolate","Cookies","Fruit"]
count = [6,4,7,5]

plt.bar(food,count,color="yellow")
plt.title("foodCount")
plt.show()

thing = ["Adults","Kids","Pets"]
count = [2,2,1]

plt.bar(thing,count,)
plt.title("thingCount")
plt.show()
