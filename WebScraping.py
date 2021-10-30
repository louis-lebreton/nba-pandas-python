
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
    
    
def Scraping_equipes_NBA(var_url):
    #définition de l'url ou chercher les données :
    url = var_url
    #Collecte du Code HTML de la page dans un object Soup :
    response = requests.get(url)
    if response.ok :
        soup = BeautifulSoup(response.content, 'html.parser')
        #Extraire les informations :
        #prendre les lignes des équipes : trouver l'identifiant des équipes :
        #full table trouver dans inspecter l'élément :
        #toutes les infos sont dans des td
        tableau = soup.find_all(class_ = 'full_table')
        equipes = []
        for i in range(len(tableau)):
            equipe = []
            for j in tableau[i].find_all('td') :
                equipe.append(j.text)
            equipes.append(equipe)
        #print(equipes)
        """
        Exemple information sur une équipe :

        équipe = []
        for j in tableau[1].find_all('td') :
            équipe.append(j.text)
        print(équipe)
        """
        #scraper les colonnes :
        #HTML : balise THEAD < TR < TH
        variables = soup.find(class_ = 'thead')
        nom_variable = [variables.text for item in variables][0]
        #supprimer les espaces et les : /n
        nom_variable_clean = nom_variable.split('\n')[2: -1]
        df = pd.DataFrame(equipes, columns = nom_variable_clean)
        return df