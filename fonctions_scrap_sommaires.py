import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import fonctions


#fonction pour récupérer le sommaire d'un joueur à partir du lien de sa page
def Scraping_sommaire_from_lien(site_team):
    
    #définition de l'url ou chercher les données :
    html = urlopen(site_team)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("div", {"class":"stats_pullout"})
    #récupération des noms des variables du tableau : les "span" du "div" imbriqué
    #dans un autre div
    rowss = divb.findAll('div')[1:]
    headers = [[div.getText() for div in rowss[i].findAll('span')]
                    for i in range(len(rowss))]

    #récupération des lignes du tableau : les "p" du "div" imbriqué
    #dans un autre div
    rows = divb.findAll('div')[1:]
    rows_data = [[div.getText() for div in rows[i].findAll('p')]
                    for i in range(len(rows))]
    
    #je dois trié mes listes multidimensionelles scrapés car elles ont des anomalies 
    #( des listes en trop, supérieures à 2 )
    rows_datatrie=[]
    for i in range(len(rows_data)):
        if len(rows_data[i])<=2:
            rows_datatrie.append(rows_data[i])
    headerstrie=[]
    for i in range(len(headers)):
        if len(headers[i])<=1:
            headerstrie.append(headers[i]) 
    #concatenation des deux dataframes des headers et des données
    df1 = pd.DataFrame(headerstrie)
    df2 = pd.DataFrame(rows_datatrie)
    df3 = pd.concat([df1,df2], axis=1)
    
    return df3


#cette fonction permet de récupérer le lien de la page du ième joueur
def Scraping_sommaire_players(i,varurl):
    
    #définition de l'url ou chercher les données :
    html = urlopen(varurl)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("table", {"id":"totals_stats"})
    #récupération des liens des pages des jouerus dans le bon ordre
    liens=divb.findAll('a', attrs={'href': re.compile("^/players/")})
    #récupération de la balise du ième joueur
    balise = liens[i]
    #conversion en type string
    schaine=str(balise)
    #recuperation du lien parmi la balise
    y = schaine.find("html")
    lienprecis = schaine[9:y+4]
     #reconstruction du lien complet
    urlteam="https://www.basketball-reference.com"+lienprecis
     #récupération du sommaire du joueurs grâce à la fonction Scraping_sommaire_from_lien
    sommaire=Scraping_sommaire_from_lien(urlteam)
    return sommaire



