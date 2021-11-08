import pandas as pd
from pandas import *
from arange import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import WebScraping
import fonctions

def dix(data):
    team = []
    pts = []
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        pts.append(df['PTS'][i])
    return pts

df=WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')

dg=dix(df)