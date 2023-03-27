import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""
Les fonctions :

"""

def verif_choix(variable, x):
    if x == 1 :
        while variable != "1" :
            variable = input()
        return int(variable)
    elif x == 2 :
        while variable != "1" and variable != "2" :
            variable = input()
        return int(variable)
    elif x == 3 :
        while variable != "1" and variable != "2" and variable != "3" :
            variable = input()
        return int(variable)
    elif x == 4 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" :
             variable = input()
        return int(variable)
    elif x == 5 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" and variable != "5":
             variable = input()
        return int(variable)
    elif x == 6 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" and variable != "5" and variable != "6":
             variable = input()
        return int(variable)

def marge():
    print()
    print()
    print("#####################################################################################")
    print("#####################################################################################")
    print()
    print()
    return

def dix_joueurs_meilleurs_points(data):
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['PTS'][i])
    return

def dix_joueurs_ages(data):
    df = data  
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['Age'][i])
    return

def dix_joueurs_jeunes(data):
    df = data  
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = True)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['Age'][i])
    return 

def dix_joueurs_jeunes_tk(data):
    player = []
    age = []
    df = data  
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = True)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        player.append(df['Player'][i])
        age.append(df['Age'][i])
    return player , age




def dix_joueurs_meilleurs_points_tk(data):
    player = []
    pts = []
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        player.append(df['Player'][i])
        pts.append(df['PTS'][i])
    return player, pts


def dix_joueurs_meilleurs_points_tk2(data):
    player = []
    pts = []
    team = []
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        player.append(df['Player'][i])
        pts.append(df['PTS'][i])
        team.append(df['Tm'][i])
    return player, pts, team

def dix_joueurs_ages_tk(data):
    player = []
    age = []
    df = data  
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        player.append(df['Player'][i])
        age.append(df['Age'][i])

    return player , age

def choix_saison():
    marge()
    print("1 . NBA 2021-22")
    print("2 . NBA 2020-21")
    print("3 . NBA 2019-20")
    marge()
    choix_saison = input("")
    #Verification de saisi
    verif_choix(choix_saison, 3)
    choix_saison = int(choix_saison)
    return choix_saison

def dix_meilleurs_equipe_points_tk(data):
    team = []
    pts = []
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        team.append(df['Team'][i])
        pts.append(df['PTS'][i])
    return team, pts

###############################################################################
##################### fonctions scrap image
###############################################################################


#Cette fonction permet de récupérer le lien .png ou .jpg de l'image 
#en entrant en paramètre le lien de la page individuelle du joueur
def Scraping_lien_image(site_team):
    
    #définition de l'url ou chercher les données :
    html = urlopen(site_team)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("div", {"id":"info"})
    #récupération du lien de l'image grâce au pattern "https://" (utilisation de re)
    liens=divb.findAll('img', attrs={'src': re.compile("^https://")})
    #conversion du lien récupéré en type string
    schaine=str(liens)
    #récuperation du lien parmi la balise img (ce qu'il y a entre "src="+5 et ">"-1)
    a = schaine.find("src=")
    b = schaine.find("/>")
    #création de l'url précis
    urlprecis = schaine[a+5:b-1]
    
    return urlprecis

#cette fonction permet de récupérer le lien .png ou .jpg de l'image du i-ème joueur
#en entrant en paramètre le lien de la page de l'ensemble des joueurs d'une même saison
def Scraping_liens_images_players(i,varurl):
    
    #définition de l'url ou chercher les données :
    html = urlopen(varurl)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("table", {"id":"totals_stats"})
    #récupération des liens des pages des joueurs dans le bon ordre
    liens=divb.findAll('a', attrs={'href': re.compile("^/players/")})
    #récupération de la balise du ième joueur
    balise = liens[i]
    #conversion en type string
    schaine=str(balise)
    #récuperation du lien parmi la balise
    y = schaine.find("html")
    lienprecis = schaine[9:y+4]
    #reconstruction du lien complet
    urlteam="https://www.basketball-reference.com"+lienprecis
    #utilisation de la 1ere fonction pour récuperer le lien .jpg de l'image 
    lienimage=Scraping_lien_image(urlteam)
    
    return lienimage 

#cette fonction permet de récupérer le lien .png de l'image de la i-ème team
#en entrant en paramètre le lien d'une page de Basket-Reference
def Scraping_liens_images_teams(i,varurl):
    
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
    #utilisation de la 1ere fonction pour recuperer le lien .png de l'image 
    lienimage=Scraping_lien_image(urlteam)

    return lienimage


