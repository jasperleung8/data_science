import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.head(10))

print(titanic.shape)

print(titanic["Age"].max())

print(titanic.info())

print(titanic.describe())