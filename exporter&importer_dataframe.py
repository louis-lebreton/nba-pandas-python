import pandas
import os #module pour créer des dossiers
import WebScraping


#exemple d'un dataframe
dataframe1=WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')


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


