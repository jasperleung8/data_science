import matplotlib.pyplot as plt

#Carbohydrates

CarFood = ["Bread","Rice","Noddles"]
CarCalories = [95,130,180]
CarProtien = [9,2.7,4.5]
CarColor = "Green"

#Protien

ProtienFood = ["Chicken","Fish","Eggs"]
ProtienCalories = [239,206,155]
Protien = [27,25,13]
ProtienColor = "Orange"

#Vegetables

VegeFoods = ["Broccoli","Potatos","Tomato"]
VageCalories = [34,120,20]
VageProtien = [2.8,3,1]
VageColor = "Yellow"

Fruits = ["Apple","Orange","Banana"]
FruitsCalories = [52,47,105]
FruitsProtien = [0.3,0.9,1.1]
FruitsColor = "Red"

plt.figure(figsize=(10,7))

#Ploting each category

plt.scatter(CarCalories,CarProtien,color=CarColor,s=150,label="Carbohydrates")
plt.scatter(ProtienCalories,Protien,color=ProtienColor,s=150,label="Protien")
plt.scatter(VageCalories,VageProtien,color=VageColor,s=150,label="Vagetables")
plt.scatter(FruitsCalories,FruitsProtien,color=FruitsColor,s=150,label="Fruits")

plt.show()
