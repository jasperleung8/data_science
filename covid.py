import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

#renaming columes

data.columns = ["State","Country","update","Lat","Long","Confirmed","Recovered","Deaths","Active"]
print(data.describe())
print(data.info())

#Replacing missing values with empty text

data["State"].fillna(" ",inplace=True)
