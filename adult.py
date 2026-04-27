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
#data["income"]=data["income"].str.strip()
data["income"]=data["income"].map({' <=50K':0,' >50K':1}).astype(int)
print(data.head())

data["gender"]=data["gender"].map({" Male":0, " Female":1}).astype(int)
data["race"]=data["race"].map({" White":0," Black":1," Asian-Pac-Islander":2," Amer-Indian-Eskimo":3," Other":4}).astype(int)
data["marriage"]=data["marriage"].map({" Married-civ-spouse":0," Never-married":1," Divorced":2," Separated":3," Widowed":4," Married-spouse-absent":5," Married-AF-spouse":6}).astype(int)
data["occupation"]=data["occupation"].map({" Prof-specialty":0," Craft-repair":1," Exec-managerial":2," Adm-clerical":3," Sales":4," Other-service":5," Machine-op-inspct":6," ?":7," Transport-moving":8," Handlers-cleaners":9," Farming-fishing":10," Tech-support":11," Protective-serv":12," Priv-house-serv":13," Armed-Forces":14}).astype(int)
data["relationship"]=data["relationship"].map({" Husband":0," Not-in-family":1," Own-child":2," Unmarried":3," Wife":4," Other-relative":5}).astype(int)
data["work"]=data["work"].map({" Private":0," Self-emp-not-inc":1," Local-gov":2," ?":3," State-gov":4," Self-emp-inc":5," Federal-gov":6," Without-pay":7," Never-worked":8}).astype(int)
data["study"]=data["study"].map({" HS-grad":0," Some-college":1," Bachelors":2," Masters":3," Assoc-voc":4," 11th":5," Assoc-acdm":6," 10th":7," 7th-8th":8," Prof-school":9," 9th":10," 12th":11," Doctorate":12," 5th-6th":13," 1st-4th":14," Preschool":15}).astype(int)

#Ploting the bar graph for education againest income

data.groupby("study").income.mean().plot(kind="bar")
plt.show()

data.groupby("occupation").income.mean().plot(kind="bar")
plt.show()

data.groupby("relationship").income.mean().plot(kind="bar")
plt.show()

data.groupby("race").income.mean().plot(kind="bar")
plt.show()

data.groupby("gender").income.mean().plot(kind="bar")
plt.show()

data.groupby("work").income.mean().plot(kind="bar")
plt.show()

data.groupby("marriage").income.mean().plot(kind="bar")
plt.show()
