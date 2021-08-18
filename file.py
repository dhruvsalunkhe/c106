import csv
from numpy.lib.function_base import corrcoef
import plotly.express as px
import pandas as pd
import numpy as np

def plotfigure(datapath):
    with open(datapath) as csv_file:
        dataframe = pd.read_csv(csv_file)

        figure = px.scatter(dataframe,x="Temperature",y="Ice-cream Sales")
        figure.show()



def getdatasource(datapath):
    temperature = []
    sales = []
    with open(datapath) as csv_file:
        csvreader = csv.DictReader(csv_file)
        for row in csvreader:
            temperature.append(float(row["Temperature"]))
            sales.append(float(row["Ice-cream Sales"]))
    return {"x":sales,"y":temperature}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)
    print(correlation[0,1])

def setup():
    datapath = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    plotfigure(datapath)
    data = getdatasource(datapath)
    findcorrelation(data)

setup()