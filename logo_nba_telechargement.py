import urllib.request
import os
import scraplienimage

#création du dossier pour stocker les images s'il n'existe pas déjà
#le dossier est créé dans le repertoire où est ce script
if not os.path.exists('logos_nba'):
    os.mkdir('logos_nba')
    
#telechargement des images des 5 premières equipes du tableau
#dans le dossier nouvellement créé
# il y a 30 équipes en tout
for i in range(5):
    #importation du nom.png de l'image
    lienimage=scraplienimage.Scraping_liens_images(i,'https://www.basketball-reference.com/leagues/NBA_2022.html')
    #choix du nouveau nom : CHO, NYK , LAL ...
    a = lienimage.find("bbr/")
    nom = lienimage[a+4:a+7]
    nouveaunom="logos_nba/"+nom+".jpg"
    #telechargement dans le dossier
    f = open(nouveaunom,'wb')
    urllib.request.urlretrieve(lienimage,nouveaunom)

#durée du téléchargement : environ 2 sec par image téléchargée