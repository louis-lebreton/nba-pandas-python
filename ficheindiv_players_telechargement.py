import urllib.request
import os
import fonctions_ficheindiv
import fonctions
import pandas 
import io

#Scrap des fiches individuelles des joueurs : création de fichier .txt pour chaque joueur
#envoyés dans un nouveau dossier "ficheindiv_players" dans le répertoire 
#à partir d'unne année souhaitée

#choix de la page
######################################################################
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'
######################################################################
######################################################################

#création du fichier
if not os.path.exists('ficheindiv_players'):
   os.mkdir('ficheindiv_players')

   
#téléchargement des fiches individuelles des 4 premiers joueurs du tableau
#dans le dossier nouvellement créé
# il y a environ 500 joueurs en tout
for i in range(4):
    #récupération du nom du joueur pour le créer nom de fichier
    lienimage=fonctions.Scraping_liens_images_players(i,lienpage)
    a = lienimage.find("players/")
    nom = lienimage[a+8:-4]
    #on rajoute "sommaires_players/" pour l'envoyer vers notre dossier
    nomdufichier="ficheindiv_players/"+nom+".txt"
    
    #ce que nous allons ecrire dans nos fichiers:
    wr=fonctions_ficheindiv.Scraping_ficheindiv_players(i,lienpage)
    
    #ouvrir un fichier txt
    text_file = open(nomdufichier, "w")
    #ecrire notre texte sur le joueur
    with io.open(nomdufichier, "w", encoding="utf-8") as f:
        f.write(wr)
    #fermer le fichier
    text_file.close()
   


#durée du téléchargement : environ 3 sec par fiche individuelle téléchargée