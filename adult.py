import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
import pandas as pd

data = pd.read_csv("adult.csv")

data.columns = ["age","work_class","id","study","study_class","marriage_state","occupation","relationship","race","gender","gain","lose","work_per_week","country","income"]
data.rename(columns={"work_class":"work","study_class":"class","marriage_state":"marriage"},inplace=True)

print(data.describe())
print(data.info())

#Count of missing values

print(data.isnull().sum())

#Finding special character

print(data.isin(["?"]).sum(axis=0))

#Finding unique values

for i in data.columns:
    print("---- %s ---"% i)
    print(data[i].value_counts())

#droping columes

data.drop(["id","class","work_per_week","gain","lose","country"],axis=1,inplace=True)
income = set(data["income"])
print(income)

#maping data into numbers
data["income"]=data["income"].str.strip()
data["income"]=data["income"].map({' <=50k':0,' >50k':1})
print(data.head())
