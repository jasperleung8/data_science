import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.head(10))

print(titanic.shape)

print(titanic["Age"].max())

print(titanic.info())

print(titanic.describe())

#filtering out rows

data = titanic[titanic["Age"] < 40]

print(data.head())

print(data.shape)

#People who were male

male = titanic[titanic["Sex"] == "male"]

print(male.head())

siblings = titanic[titanic["Siblings/Spouses Aboard"] == 2 ]

print(siblings.head())

print(siblings.shape)

#Combiening muiltble condions

data2 = titanic[titanic["Pclass"].isin([2,3])]

print(data2.head())

print(data2.shape)

data3 = titanic[(titanic["Sex"]=="male") & (titanic["Pclass"]==1)]

print(data3.head())

data4 = titanic[(titanic["Sex"]=="female") & (titanic["Pclass"]==2)]

print(data4.head())

print(data4.shape)

#Group By

data5 = (titanic.groupby(["Pclass","Sex"])["Fare"].mean())

print(data5.head())

data6 = (titanic.groupby(["Survived","Pclass"])["Fare"].mean())

print(data6.head())

print(titanic["Age"].mean())

print((titanic["Sex"]=="male").sum())

print((titanic["Survived"]==1).sum())

print(titanic[titanic["Sex"]=="male"]["Fare"].max())

print(titanic[titanic["Sex"]=="female"]["Fare"].max())

print(titanic.groupby("Pclass")["Age"].mean())

print(titanic.groupby(["Pclass","Sex"]).sum())

print(titanic.groupby("Pclass")["Fare"].mean())

print(titanic[(titanic["Pclass"]==1)].groupby("Sex")["Fare"].mean())

print(titanic[(titanic["Pclass"]==2)].groupby("Sex")["Age"].mean())
