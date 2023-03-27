import urllib.request
import os
# on utilise le module fonctions.py pour accéder à
# notre fonction Scraping_liens_images_players(i,lienpage)
import fonctions


#choix de la page
######################################################################
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_2021_totals.html'
######################################################################
######################################################################

#création du dossier pour stocker les images s'il n'existe pas déjà
#le dossier est créé dans le repertoire où est ce script
if not os.path.exists('images_players2'):
    os.mkdir('images_players2')


# téléchargement des images de l'ensemble des joueurs du tableau
# dans le dossier nouvellement créé, grâce à une boucle

for i in range(610,740):
    #importation du nom.jpg de l'image
    lienimage=fonctions.Scraping_liens_images_players(i,lienpage)
    #choix du nouveau nom 
    a = lienimage.find("players/")
    nom = lienimage[a+8:-1]

    nouveaunom="images_players2/"+nom+"g"
    #téléchargement dans le dossier
    f = open(nouveaunom,'wb')
    urllib.request.urlretrieve(lienimage,nouveaunom)

#Durée du téléchargement : environ 2 sec par image téléchargée