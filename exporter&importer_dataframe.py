#bibliothèques utilisées
import pandas
import os #bibliothèque pour créer et manipuler des dossiers et fichiers
#on importe notre module WebScraping pour accéder à 
#notre fonction de scraping : Scraping_joueurs_NBA_total
import WebScraping


#Ce programme la façon d'exporter un dataframe en .csv dans un dossier
#puis comment le réimporter


#exemple d'un dataframe
lien='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'
dataframe1=WebScraping.Scraping_joueurs_NBA_total(lien)


#####################################################################
### Pour exporter le data frame en .csv dans un nouveau dossier
#####################################################################

#création du dossier où stocker les .csv (s'il n'existe pas déjà )
if not os.path.exists('dossier1'):
   os.mkdir('dossier1')

#transformation du dataframe en .csv, envoyé vers notre nouveau dossier
#header=None, index=None   pour enlever les noms de colonnes ou de lignes
dataframe1.to_csv("dossier1/fichier1.csv" )



#####################################################################
### Pour réimporter le .csv en dataframe
#####################################################################

df=pandas.read_csv("dossier1/fichier1.csv",index_col=0)

print(df)


