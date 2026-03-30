import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

#renaming columes

data.columns = ["States","Country","update","Lat","Long","Confirmed","Recovered","Deaths","Active"]
print(data.describe())
print(data.info())

#Replacing missing values with empty text

data["States"].fillna('',inplace=True)

#Top 10 countries by confirmed cases

confirmed = (data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))

graph = px.scatter(x=confirmed.index,y=confirmed.values,size=confirmed.values,color=confirmed.index,size_max=120,title="Top ten contries by confirmed covid cases")

graph.write_html("Top 10 Confirmed Cases.html",auto_open=True)

#Top 10 countries by confirmed deaths

deaths = (data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))

graph2 = px.scatter(x=deaths.index,y=deaths.values,size=deaths.values,color=deaths.index,size_max=120,title="Top 10 countries by confirmed deaths")

graph2.write_html("Top 10 Confirmed deaths.html",auto_open=True)

#Top 10 countries by confirmed recovery

recovery = (data.groupby("Country")["Recovered"].sum().nlargest(10).sort_values(ascending=False))

graph3 = px.bar(x=recovery.index,y=recovery.values,color=recovery.values,title="Top 10 countries by recovered cases",height=600)

graph3.write_html("Top 10 confirmed recovery.html",auto_open=True)

#Top 10 countries by active

active = (data.groupby("Country")["Active"].sum().nlargest(10).sort_values(ascending=False))

graph4 = px.scatter(x=active.index,y=active.values,size=active.values,color=active.index,size_max=120,title="Top 10 countries by active")

graph4.write_html("Top 10 by active.html",auto_open=True)

#Top 10 states of a country

def findTop10(name,n=5):
    countryData = data[data["Country"]==name]
    return countryData.nlargest(n,"Confirmed")

usStates = findTop10("US")

graph5 = go.Figure()

graph5.add_bar(name="Confirmed",x=usStates["Confirmed"],y=usStates["States"],orientation="h")

graph5.update_layout(title="Most affected states in US",barmode="group",height=600)

graph5.write_html("Figure 5_States.html",auto_open=True)

# France Data

franceStates = findTop10("France")

graph6 = go.Figure()

graph6.add_bar(name="Confirmed",x=franceStates["Confirmed"],y=franceStates["States"],orientation="h")
graph6.update_layout(title="Most affected states in France")
graph6.write_html("Most affected states in France.html",auto_open=True)

#Calating the recovery rate and death rate

data["Recovery_rate"]=(data["Recovered"]/data["Confirmed"])*100
data["Death_rate"]=(data["Deaths"]/data["Confirmed"])*100
data.replace([np.inf,-np.inf],0,inplace=True)

recoveryRate = (data.groupby("Country")["Recovery_rate"].mean().nlargest(5))
print("Top 5 countries by recovery rate")
print(recoveryRate)

deathRate = (data.groupby("Country")["Death_rate"].mean().nlargest(5))
print("Top 5 counties by death rate")
print(deathRate)

#World map of comfirmed cases

data2 = px.scatter_geo(data,lat="Lat",lon="Long",size="Confirmed",color="Confirmed",hover_name="Country",projection="natural earth",title="World Map of Covid-19 confirmed cases")
data2.write_html("World Map of confirmed cases.html",auto_open=True)
#data2.write_html("")

#Gobal Covid distribution

totalConfirmed = data["Confirmed"].sum()
totalRecovered = data["Recovered"].sum()
totalDeaths = data["Deaths"].sum()
totalActive = data["Active"].sum()

pieChart = px.pie(names=["Confirmed","Recovered","Deaths","Active"],values=[totalConfirmed,totalRecovered,totalDeaths,totalActive],title="Gobal Covid distribution")
pieChart.write_html("Covid data.html",auto_open=True)

#Country Data in a CSV file

csv = data.groupby("Country").sum()[["Confirmed","Recovered","Deaths","Active"]]
csv.to_csv("Contry Data.csv")
print("file saved as a csv")

