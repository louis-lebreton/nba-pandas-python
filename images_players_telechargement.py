import urllib.request
import os
import fonctions


#choix de la page
######################################################################
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_2015_totals.html'
######################################################################
######################################################################

#création du dossier pour stocker les images s'il n'existe pas déjà
#le dossier est créé dans le repertoire où est ce script
if not os.path.exists('images_players'):
    os.mkdir('images_players')


#telechargement des images des 9 premiers joueurs du tableau
#dans le dossier nouvellement créé
# il y a environ 500 joueurs en tout
for i in range(9):
    #importation du nom.png de l'image
    lienimage=fonctions.Scraping_liens_images_players(i,lienpage)
    #choix du nouveau nom 
    a = lienimage.find("players/")
    nom = lienimage[a+8:-1]

    nouveaunom="images_players/"+nom+"g"
    #telechargement dans le dossier
    f = open(nouveaunom,'wb')
    urllib.request.urlretrieve(lienimage,nouveaunom)

#durée du téléchargement : environ 2 sec par image téléchargée