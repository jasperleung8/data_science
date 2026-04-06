import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("CovidData2.csv",encoding="ISO-8859-1")

#renaming columns

data.columns = ["Date","Code","Country","region","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths"]
#print(data.columns)

#Converting date from string into date time data type

data["Date"]=pd.to_datetime(data["Date"])
print(data.dtypes)

total = data.groupby("Date")[["New_cases","Cumulative_cases","New_deaths","Cumulative_deaths"]].sum()
print(total.head())

#Creating new empty figures

figure = go.Figure()
figure.add_trace(go.Scatter(x=total,y=total["Cumulative_cases"],fill="tonexty",line_color="light blue"))
figure.update_layout(title="Scatter")
figure.write_html("Scatter_Graph.html",auto_open=True)

#figure for cumulative deaths

figure2 = go.Figure()
figure2.add_trace(go.Scatter(x=total,y=total["Cumulative_deaths"],line_color="light blue"))
figure2.update_layout(title="Graph for cmulative deaths")
figure2.write_html("cumulative death graph.html",auto_open=True)

#figure for new cases

figure3 = go.Figure()
figure3.add_trace(go.Scatter(x=total,y=total["New_cases"],fill="tonexty",line_color="red"))
figure3.update_layout(title="New cases graph")
figure3.write_html("New Cases Graph.html",auto_open=True)

#figure for new deaths

figure4 = go.Figure()
figure4.add_traces(go.Scatter(x=total,y=total["New_deaths"],fill="tonexty",line_color="red"))
figure4.update_layout(title="New deaths graph")
figure4.write_html("New deaths graph.html",auto_open=True)
