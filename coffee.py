import csv
from numpy.lib.function_base import corrcoef
import plotly.express as px
import pandas as pd
import numpy as np

def plotfigure(datapath):
    with open(datapath) as csv_file:
        dataframe = pd.read_csv(csv_file)

        figure = px.scatter(dataframe,x="Coffee in ml",y="sleep in hours")
        figure.show()



def getdatasource(datapath):
    coffee = []
    sleep = []
    with open(datapath) as csv_file:
        csvreader = csv.DictReader(csv_file)
        for row in csvreader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)
    print(correlation[0,1])

def setup():
    datapath = "cups of coffee vs hours of sleep.csv"
    plotfigure(datapath)
    data = getdatasource(datapath)
    findcorrelation(data)

setup()