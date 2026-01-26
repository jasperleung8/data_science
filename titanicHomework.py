import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.groupby("Pclass")["Fare"].mean())

print(titanic.groupby("Sex")["Fare"].mean())

print(titanic.groupby("Pclass")["Age"].mean())

print(titanic.groupby(["Pclass","Sex"])["Age"].mean())

print(titanic.groupby("Pclass").size())

print(titanic.groupby(["Pclass","Sex"]).size())

print(titanic.groupby(["Pclass","Sex"])["Age"].mean())

print(titanic.groupby("Pclass")["Fare"].mean())

print(titanic.groupby("Sex")["Fare"].mean())
