import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import fonctions

#Fonctions certainement à mettre avec les autres fonction dans le fichier fonctions.py

#fonction pour récupérer la fiche individuelle d'un joueur à partir du lien de sa page
def Scraping_ficheindiv_from_lien(site_team):
    
    #définition de l'url ou chercher les données :
    html = urlopen(site_team)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("div", {"itemtype":"https://schema.org/Person"})
    

    #récupération du nom du joueur
    # le "span" de la balise "h1"
    rowss = divb.findAll('h1')[0:]
    nom = [[h1.getText() for h1 in rowss[i].findAll('span')]
                    for i in range(len(rowss))]
    nom=nom[0][0]
    
    #création des noms de lignes
    headers=['Nom', 'Nom complet', 'Taille', 'Poids', 'Date de naissance', 'Lieu de Naissance', 'College' , 'Equipe de Draft', 'Date de Draft', 'Début en NBA']
    
    
    #récupération des données
    # l'ensemble de la balise "p"
    rows = divb.findAll('p')[1:]
    #conversion en string
    stri=str(rows)
    #supression des balises et des espaces du texte
    stri=re.sub('<[^>]+>', '', stri)
    stri=stri.replace('  ','')
    stri = stri.replace('\n', ';')
    stri = stri.replace(';;;', ';;')
    stri = stri.replace(';;', ';')
    stri = stri.replace(';', '\n')
    stri = stri.replace('[', '')
    stri = stri.replace(']', '')
    stri = stri.replace(',', '  ')
    return stri
    

#Cette fonction permet de récupérer la fiche individuelle du ième joueur
#à partir du lien de la page des joueurs
def Scraping_ficheindiv_players(i,varurl):
    
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
    ficheindiv=Scraping_ficheindiv_from_lien(urlteam)
    return ficheindiv
