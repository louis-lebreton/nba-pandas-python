from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
Import des librairies :

"""

def Scraping_joueurs_NBA_total(var_url):
    #définition de l'url ou chercher les données :
    url = var_url
    #Collecte du Code HTML de la page dans un object Soup :
    response = requests.get(url)
    if response.ok :
        soup = BeautifulSoup(response.content, 'html.parser')
        #Extraire les informations :
        #prendre les lignes des joueurs : trouver l'identifiant des joueurs :
        #full table trouver dans inspecter l'élément :
        #toutes les infos sont dans des td
        tableau = soup.find_all(class_ = 'full_table')
        joueurs = []
        for i in range(len(tableau)):
            joueur = []
            for j in tableau[i].find_all('td') :
                joueur.append(j.text)
            joueurs.append(joueur)
        #print(joueurs)
        """
        Exemple information sur un joueur :

        joueur = []
        for j in tableau[1].find_all('td') :
            joueur.append(j.text)
        print(joueur)
        """
        #scraper les colonnes :
        #HTML : balise THEAD < TR < TH
        variables = soup.find(class_ = 'thead')
        nom_variable = [variables.text for item in variables][0]
        #supprimer les espaces et les : /n
        nom_variable_clean = nom_variable.split('\n')[2: -1]
        df = pd.DataFrame(joueurs, columns = nom_variable_clean)
        return df 
    
def Scraping_equipes_NBA_autretable(var_url):
    #définition de l'url ou chercher les données :
    html = urlopen(var_url)
    #Collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="lxml")
    #récupération des noms des variables du tableau
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    #récupération des lignes
    rows = soup.findAll('tr')[2:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    #rajout du numéro de ligne en 1ère colonne
    numligne = 1
    for i in range(0, len(rows_data)):
        rows_data[i].insert(0, numligne)
        numligne +=1
    #création du dataframe
    df = pd.DataFrame(rows_data, columns = headers)
    return df

def Scraping_equipes_NBA(var_url):
    #définition de l'url ou chercher les données :
    html = urlopen(var_url)
    #Collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #sous-partie de l'html de base
    divb = soup.find("table", {"id":"totals-team"})
    #per_poss-team 
    #per_game-team
  
    #récupération des noms des variables du tableau
    headers = [th.getText() for th in divb.findAll('tr', limit=2)[0].findAll('th')]
    #headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    #récupération des lignes
    
    rows = divb.findAll('tr')[1:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    #rajout du numéro de ligne en 1ère colonne
    numligne = 1
    for i in range(0, len(rows_data)):
        rows_data[i].insert(0, numligne)
        numligne +=1
    #création du dataframe
    df = pd.DataFrame(rows_data, columns = headers)
    return df

def Scraping_Draft_NBA(var_url):
    #définition de l'url ou chercher les données :
    html = urlopen(var_url)
    #Collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #sous-partie de l'html de base
    divb = soup.find("table", {"id":"first_overall"})
    #per_poss-team 
    #per_game-team
  
    #récupération des noms des variables du tableau
    headers = [th.getText() for th in divb.findAll('tr', limit=2)[0].findAll('th')]
    #headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    #récupération des lignes
    
    rows = divb.findAll('tr')[1:]
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