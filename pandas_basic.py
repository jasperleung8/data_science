import pandas as pd

data=pd.DataFrame({"name":["James","Mary"],"age":[12,6],"Year":[7,1]})

print(data.head())

print(data.shape)

print(data["age"])

print(data["age"].max())

print(type(data["age"]))

print(data.info())

print(data.describe())