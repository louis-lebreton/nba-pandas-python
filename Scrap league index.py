from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd


"""
Import des librairies :

"""

    
def Scraping_league_index(var_url):
    #définition de l'url ou chercher les données :
    html = urlopen(var_url)
    #Collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #sous-partie de l'html de base
    divb = soup.find("table", {"id":"stats"})
   
  
    #récupération des noms des variables du tableau
    headers = [th.getText() for th in divb.findAll('tr', limit=2)[1].findAll('th')]
    #headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    #récupération des lignes
    
    rows = divb.findAll('tr')[2:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    #rajout du numéro de ligne en 1ère colonne
    numligne = 2021
    for i in range(0, len(rows_data)):
        rows_data[i].insert(0, numligne)
        numligne -=1
    #création du dataframe
    df = pd.DataFrame(rows_data, columns = headers)
    return df
df = Scraping_league_index('https://www.basketball-reference.com/leagues/')

print(df)
