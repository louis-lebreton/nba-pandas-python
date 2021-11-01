from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


#cette fonction permet de récupérer le lien .png de l'image 
#en entrant en paramètre le lien du site de la team : exemple: https://www.basketball-reference.com/teams/CHO/2022.html
def Scraping_lien_image(site_team):
    
    #définition de l'url ou chercher les données :
    html = urlopen(site_team)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("div", {"id":"info"})
    #récupération du lien de l'image 
    liens=divb.findAll('img', attrs={'src': re.compile("^https://")})
    #conversion en type string
    schaine=str(liens)
    #recuperation du lien parmi la balise img
    a = schaine.find("src=")
    b = schaine.find("/>")
    urlprecis = schaine[a+5:b-1]
    
    return urlprecis

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

#cette fonction permet de récupérer le lien .png de l'image du i-ème joueur
#en entrant en paramètre le lien d'une page de Basket-Reference
def Scraping_liens_images_players(i,varurl):
    
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
    #utilisation de la 1ere fonction pour recuperer le lien .png de l'image 
    lienimage=Scraping_lien_image(urlteam)
    
    return lienimage 

