#biblioth�ques utilis�es
import pandas
import os #biblioth�que pour cr�er et manipuler des dossiers et fichiers
#on importe notre module WebScraping pour acc�der � 
#notre fonction de scraping : Scraping_joueurs_NBA_total
import WebScraping


#Ce programme la fa�on d'exporter un dataframe en .csv dans un dossier
#puis comment le r�importer


#exemple d'un dataframe
lien='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'
dataframe1=WebScraping.Scraping_joueurs_NBA_total(lien)


#####################################################################
### Pour exporter le data frame en .csv dans un nouveau dossier
#####################################################################

#cr�ation du dossier o� stocker les .csv (s'il n'existe pas d�j�)
if not os.path.exists('dossier1'):
   os.mkdir('dossier1')

#transformation du dataframe en .csv, envoy� vers notre nouveau dossier
#header=None, index=None   pour enlever les noms de colonnes ou de lignes
dataframe1.to_csv("dossier1/fichier1.csv" )



#####################################################################
### Pour r�importer le .csv en dataframe
#####################################################################

df=pandas.read_csv("dossier1/fichier1.csv",index_col=0)

print(df)


