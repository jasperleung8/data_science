import matplotlib.pyplot as plt
import numpy as np

data = ["Jan","Feb","Mar","Apr","May","Jun","July","Oug","Sep","Oct","Nov","Dec"]
x = np.arange(len(data))

#orangic, paid, social, referral
orangic = [1500,900,700,1000,1200,400,1400,500,1100,800,1700,1300]
paid = [500,1200,700,1400,800,1200,1100,1200,800,500,1100,1300]
social = [400,100,1000,1200,500,200,900,1900,800,200,1000,1400]
referral = [600,700,300,1000,1500,1800,1200,700,600,100,1100,200]

#Basic stack plot

plt.figure(figsize=(8,6))
plt.stackplot(x,orangic,paid,social,referral,labels=["Orangic","Paid","Social","referral"])
plt.xticks(x,data)
plt.title("Website traffic")
plt.legend(loc="upper left")
plt.show()

#Adding colours

colours = ["#eb5449","#57eb49","#496aeb","#eb49de"]

plt.figure(figsize=(8,6))
plt.stackplot(x,orangic,paid,social,referral,labels=["Orangic","Paid","Social","Referral"],colors=colours,alpha=0.8)
plt.xticks(x,data)
plt.title("Website traffic")
plt.legend(loc="lower left")
plt.show()

#Highlighting

plt.figure(figsize=(10,10))
plt.stackplot(x,orangic,paid,social,referral,labels=["Orangic","Paid","Social","Referral"],colors=colours,alpha=0.8)
plt.plot(x,orangic,color="#732722",linewidth=5)
plt.xticks(x,data)
plt.legend(loc="lower left")
plt.show()

#Grid

plt.figure(figsize=(8,6))
plt.stackplot(x,orangic,paid,social,referral,labels=["Orangic","Paid","Social","Referal"],colors=colours,alpha=0.8)
plt.xticks(x,data)
plt.grid(alpha=0.3)
plt.legend(loc="lower left")
plt.show()

#Hightlighting the highest source
total = [sum(orangic),sum(paid),sum(social),sum(referral)]
