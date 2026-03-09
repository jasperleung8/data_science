import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv("iris.csv")
print(data.head())

#types of columns

print(data.info())

#data preprosessing

data["species"] = data["species"].replace({"setosa":0,"versicolor":1,"virginica":2})

#ploting flower features againest species

plt.subplot(221)
plt.scatter(data["sepal_length"],data["species"],s=10,c="blue",marker="o")
plt.title("Sepal length vs species")

#plot2

plt.subplot(222)
plt.scatter(data["sepal_width"],data["species"],s=10,c="blue",marker="o")
plt.title("Sepal width vs species")

#plot3

plt.subplot(223)
plt.scatter(data["petal_length"],data["species"],s=10,c="blue",marker="o")
plt.title("Patal length vs species")

#plot4

plt.subplot(224)
plt.scatter(data["petal_width"],data["species"],s=10,c="blue",marker="o")
plt.title("Petal width vs species")

plt.tight_layout()
plt.show()
