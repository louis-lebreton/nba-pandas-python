import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

#Création des csv des equipes comprenants les noms des joueurs et leurs noms de fichier (acronymes)

####################################################################################
####### Fonctions
####################################################################################

#Scrap des liens des equipes (la ième équipe)
def Scraping_lien_equipe(i,varurl):
    
    #définition de l'url ou chercher les données :
    html = urlopen(varurl)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("table", {"id":"totals-team"})
    #récupération des liens des pages des équipes dans le bon ordre
    liens=divb.findAll('a', attrs={'href': re.compile("^/teams/")})
 
    #récupération de la balise de la ième equipe
    balise = liens[i]
    #conversion en type string
    schaine=str(balise)
    #recuperation du lien parmi la balise
    lienprecis = schaine[9:29]
    #reconstruction du lien complet
    urlteam="https://www.basketball-reference.com"+lienprecis
    

    return urlteam


#scrap des liens des jouerus et de leur prenom (de la ième equipe)
def Scraping_joueurs_equipe(varurl):
    
    #définition de l'url ou chercher les données :
    html = urlopen(varurl)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("table", {"id":"roster"})
    #récupération des noms des variables du tableau
    headers = [th.getText() for th in divb.findAll('tr', limit=2)[0].findAll('th')]
    #headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    #récupération des lignes
    rows = divb.findAll('tr')[1:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]   
    
        
     #récupération des liens des pages des joueurs dans le bon ordre
    liens=divb.findAll('a', attrs={'href': re.compile("^/players/")})
    
    #récupération des acronymes des joueurs
    acronym=[]
    for j in range(len(rows)):
        #récupération du lien du ième joueur
        balise = liens[j]
        schaine=str(balise)
        #recuperation du lien parmi la balise
        y = schaine.find("html")
        acronymprecis = schaine[20:y-1]
        acronym.append(acronymprecis)
        
    #rajout des acronym dans le tableau
    numligne = 0
    for i in range(0, len(rows_data)):
        rows_data[i].append(acronym[i])
        numligne +=1
    #création du dataframe
    df = pd.DataFrame(rows_data, columns = headers)
    #garder seulement les colonnes qui nous intéressent
    update_df = df[['No.','College']]
    return update_df

####################################################################################
####### Exportation des dataframes en fichiers csv des différentes équipes
####################################################################################
#création du dossier
if not os.path.exists('teams'):
   os.mkdir('teams')

#lien de la page de base
lien="https://www.basketball-reference.com/leagues/NBA_2022.html"

#Scrap des i premières equipes 
for i in range(2):
    
    lienequipe= Scraping_lien_equipe(i,lien)
    df=Scraping_joueurs_equipe(lienequipe)
    #choix du nouveau nom : CHO, NYK , LAL ...
    a = lienequipe.find("teams/")
    nom = lienequipe[a+6:a+9]
    nomfichier="teams/"+nom+".csv"
    df.to_csv(nomfichier,header=None, index=None )

#Durée du téléchargement : environ 2 sec par fichier .csv