import matplotlib.pyplot as plt

labels = ["Oxygen","Carbon","Hydrogen","Nitrogen","Calcium","Phosphorus","Others"]
data = [65,18,10,3,1.5,1,1.2]

plt.figure(figsize=(10,10))
colours = ["#eb5449","#eb9749","#ebd049","#8deb49","#497feb","#4949eb","#9249eb"]
plt.pie(data,labels=labels,autopct="%1.1f%%",startangle=180,shadow=True,colors=colours,labeldistance=1.2,pctdistance=0.8)
plt.title("What the human body is made of")
plt.show()