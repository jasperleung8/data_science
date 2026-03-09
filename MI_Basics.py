import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv")

#Spliting x and y

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

print(x)
print(y)

#handling missing data

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")

imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

print(x)

#encoding categorical data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

data2 = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
x = np.array(data2.fit_transform(x))
print("after conventing words into numbers")
print(x)

#Conventing yes and no into 1 & 0

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y = encoder.fit_transform(y)
print("After conventing output labels")
print(y)

#Spliting into training and test data

from sklearn.model_selection import train_test_split

xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size=0.3,random_state=1)
print("Training input")
print(xTrain)
print("Testing input")
print(xTest)

print("Training output")
print(yTrain)
print("Testing output")
print(yTest)

#Training simple machine learning model

print("Start training")
from sklearn.linear_model import LogisticRegression

classifer = LogisticRegression()
classifer.fit(xTrain,yTrain)

#predicting on test data

predictions = classifer.predict(xTest)
print("predictions made by model")
print(predictions)
print("Correct answers")
print(yTest)

#Printing accuary score

from sklearn.metrics import accuracy_score

score = accuracy_score(yTest,predictions)
print("Model Accuracy")
score = round((score*100),1)
print(str(score)+"%")
