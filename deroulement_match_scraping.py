import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup



##################################################################################################
##################################################################################################
#######################   SCRAPING
##################################################################################################
##################################################################################################


############## Scrap du lien des rencontres d'un mois de cette saison
def Scraping_rencontres(var_url):
    #var_url : définition de l'url ou chercher les données
    
    #Ouverture de l'url grâce à la fonction urlopen de la biliothèque urllib.request 
    html = urlopen(var_url)
    #Collecte du code HTML de la page dans un object Soup grâce à beautifulsoup
    soup = BeautifulSoup(html, features="html.parser")
    #Découpage d'une sous-partie de l'html de base en 
    # ne prenant en compte que la balise "table" ayant comme "id":"totals-team"
    divb = soup.find("table", {"id":"schedule"})
    headers = [th.getText() for th in divb.findAll('tr', limit=2)[0].findAll('th')]
    rows = divb.findAll('tr')[1:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    #rajout
    dates = [[th.getText() for th in rows[i].findAll('th')]
                    for i in range(len(rows))]
    for i in range(0, len(rows_data)):
        rows_data[i].insert(0, dates[i])
        
    df = pd.DataFrame(rows_data, columns = headers)
    return df






############## Scrap du déroulement d'1 match à partir du lien de la page

def Scraping_deroulement(var_url):
    #var_url : définition de l'url ou chercher les données
    
    #Ouverture de l'url grâce à la fonction urlopen de la biliothèque urllib.request 
    html = urlopen(var_url)
    #Collecte du code HTML de la page dans un object Soup grâce à beautifulsoup
    soup = BeautifulSoup(html, features="html.parser")
    #Découpage d'une sous-partie de l'html de base en 
    # ne prenant en compte que la balise "table" ayant comme "id":"totals-team"
    divb = soup.find("table", {"id":"pbp"})
    

    headers = [th.getText() for th in divb.findAll('tr', limit=2)[1].findAll('th')]
    
    rows = divb.findAll('tr')[2:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    
    #Création du dataframe grâce à la bibliothèque pandas
    df = pd.DataFrame(rows_data, columns = headers)
    #garder seulement les colonnes qui nous intéressent
    updatedf = df[['Time','Score']]
    return updatedf





############## Récupération noms des équipes

def Scraping_noms_equipes(var_url):
    
    #définition de l'url ou chercher les données :
    html = urlopen(var_url)
    #collecte du Code HTML de la page dans un object Soup :
    soup = BeautifulSoup(html, features="html.parser")
    #création d'une sous-partie de l'html de base
    divb = soup.find("table", {"id":"pbp"})

    headers = [th.getText() for th in divb.findAll('tr', limit=2)[1].findAll('th')]
    
    
    return headers[1],headers[5]


##################################################################################
##################################################################################
# But ici : récupérer les liens des 4 matchs les plus serrés, les moins serrés
##################################################################################
##################################################################################

octo=Scraping_rencontres('https://www.basketball-reference.com/leagues/NBA_2022_games-october.html')
nov=Scraping_rencontres('https://www.basketball-reference.com/leagues/NBA_2022_games-november.html')
dec=Scraping_rencontres('https://www.basketball-reference.com/leagues/NBA_2022_games-december.html')
jan=Scraping_rencontres('https://www.basketball-reference.com/leagues/NBA_2022_games-january.html')
fev=Scraping_rencontres('https://www.basketball-reference.com/leagues/NBA_2022_games-february.html')


df=pd.concat([octo,nov,dec,jan,fev])
listd=df.values.tolist()


ll=[]
for i in range(len(listd)):
    if listd[i][3]!='' and listd[i][5]!='':
        ll.append(abs(float(listd[i][3])-float(listd[i][5])))
        
######################## On récupère les max et les min      
def maxN(elements, n):
    return sorted(elements, reverse=True)[:n]
def minN(elements, n):
    return sorted(elements, reverse=True)[-n:]

#print(maxN(ll,6))
#print(minN(ll,5))

positionmax=[]
positionmin=[]


for i in range(len(ll)):
    if ll[i]>=43.0:
        positionmax.append(i)
    elif ll[i]<=1.0:
        positionmin.append(i)

positionmin=[2,67,70,660,677]
listefinalemin=[]
listefinalemax=[]
for i in positionmax:
    listefinalemax.append(listd[i])
for i in positionmin[:5]:
    listefinalemin.append(listd[i])

#suppression du match mal annoté par le site : 20211220MEM
del listefinalemax[1]
del listefinalemin[1]

