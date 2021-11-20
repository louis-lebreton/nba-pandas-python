import urllib.request
import os
import fonctions
import fonctions_scrap_sommaires
import pandas 

#Scrap des sommaires des joueurs : création de fichier .csv pour chaque joueur
#envoyés dans un nouveau dossier "sommaires_players" dans le répertoire 
#à partir d'unne année souhaitée

#choix de la page
######################################################################
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'
######################################################################
######################################################################

#création du dossier pour stocker les .csv s'il n'existe pas déjà
#le dossier est créé dans le repertoire où est ce script
if not os.path.exists('sommaires_players'):
   os.mkdir('sommaires_players')
   
#téléchargement des sommaires des 2 premiers joueurs du tableau
#dans le dossier nouvellement créé
# il y a environ 500 joueurs en tout
for i in range(402,458):
    #récupération du nom du joueur pour le créer nom de fichier
    lienimage=fonctions.Scraping_liens_images_players(i,lienpage)
    a = lienimage.find("players/")
    nom = lienimage[a+8:-4]
    #on rajoute "sommaires_players/" pour l'envoyer vers notre dossier
    nomdufichier="sommaires_players/"+nom+".csv"

    #utilisation de la fonction Scraping_sommaire_players pour scraper le sommaire
    #du i-ème joueur
    df=fonctions_scrap_sommaires.Scraping_sommaire_players(i,lienpage)
    #transformation du dataframe en csv vers notre nouveau dossier
    df.to_csv(nomdufichier, header=None, index=None)


#durée du téléchargement : environ 4 sec par sommaire téléchargé
   
