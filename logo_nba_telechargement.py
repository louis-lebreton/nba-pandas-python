import urllib.request
import os
import fonctions


#choix de la page
######################################################################
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_1960.html'
######################################################################
######################################################################

#création du dossier pour stocker les images s'il n'existe pas déjà
#le dossier est créé dans le repertoire où est ce script
if not os.path.exists('logos_nba'):
    os.mkdir('logos_nba')


#telechargement des images des 9 premières equipes du tableau
#dans le dossier nouvellement créé
# il y a 30 équipes en tout
for i in range(4):
    #importation du nom.png de l'image
    lienimage=fonctions.Scraping_liens_images_teams(i,lienpage)
    #choix du nouveau nom : CHO, NYK , LAL ...
    a = lienimage.find("bbr/")
    nom = lienimage[a+4:a+7]
    #selection de l'annee
    b=lienpage.find("NBA_")
    annee=lienpage[b+4:b+8]
    nouveaunom="logos_nba/"+nom+"_"+annee+".jpg"
    #telechargement dans le dossier
    f = open(nouveaunom,'wb')
    urllib.request.urlretrieve(lienimage,nouveaunom)

#durée du téléchargement : environ 2 sec par image téléchargée