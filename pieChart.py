import matplotlib.pyplot as plt

data = ["Transport","electrcity","groceries","gas","school","books","enterainment","essentials","savings","rent"]
data2 = [60,300,200,400,500,180,450,250,450,1200]

#basic pie chart

plt.figure(figsize=(8,6))

plt.pie(data2,labels=data)
plt.title("Household expense")
plt.show()

#colours and persentages

colours = ["#eb5449","#eb9749","#ebd049","#bbeb49","#8deb49","#49eb8d","#49cbeb","#497feb","#4949eb","#9249eb"]
plt.figure(figsize=(8,6))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=90,shadow=True)
plt.title("Household expense with colours and percentages")
plt.show()

#explode

data3 = [0.1,0,0.1,0,0.1,0,0.1,0,0.1,0]
plt.figure(figsize=(4,3))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=140,shadow=True,explode=data3)
plt.title("Household expense with explode")
plt.show()

#Start angle and direction

plt.figure(figsize=(10,10))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=100,counterclock=False)
plt.title("Household expense with direction and start angle")
plt.show()

#anitclockwise

plt.figure(figsize=(8,6))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=0,counterclock=True)
plt.title("Household expense with anitclockwise")
plt.show()

#label distance and percentage placement

plt.figure(figsize=(6,8))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=0,counterclock=False,shadow=True,labeldistance=1.1,pctdistance=0.8)
plt.title("household expence with label distance and percentage placement")    
plt.show()

#finding maximum expense

explode = [0.1 if i == max(data2)else 0 for i in data2]
plt.figure(figsize=(6,8))
plt.pie(data2,labels=data,colors=colours,autopct="%1.1f%%",startangle=0,counterclock=False,shadow=True,explode=explode)
plt.title("Household expence with maxmum expense explode")
plt.show()
