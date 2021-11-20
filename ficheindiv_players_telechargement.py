import os
import fonctions_ficheindiv
import fonctions
import io

#Scrap des fiches individuelles des joueurs : création de fichier .txt pour chaque joueur
#envoyés dans un nouveau dossier "ficheindiv_players" dans le répertoire 

#choix de la page
######################################################################
lienpage='https://www.basketball-reference.com/leagues/NBA_2021_totals.html'
######################################################################


#création du fichier
if not os.path.exists('ficheindiv_players2'):
   os.mkdir('ficheindiv_players2')

   
#téléchargement des fiches individuelles de l'ensemble des joueurs du tableau
#dans le dossier nouvellement créé
for i in range(457,700):
    #récupération du nom du joueur pour créer le nom de fichier
    lienimage=fonctions.Scraping_liens_images_players(i,lienpage)
    a = lienimage.find("players/")
    nom = lienimage[a+8:-4]
    #on rajoute "sommaires_players/" pour l'envoyer vers notre dossier
    nomdufichier="ficheindiv_players2/"+nom+".txt"
    
    #ce que nous allons ecrire dans nos fichiers:
    wr=fonctions_ficheindiv.Scraping_ficheindiv_players(i,lienpage)
    
    #ouvrir un fichier .txt
    text_file = open(nomdufichier, "w")
    #ecrire notre texte sur le joueur "wr" dans le fichier .txt
    with io.open(nomdufichier, "w", encoding="utf-8") as f:
        f.write(wr)
    #fermer le fichier
    text_file.close()
   
#durée du téléchargement : environ 3 sec par fiche individuelle téléchargée