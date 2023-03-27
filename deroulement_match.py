import pandas as pd 
import re
import numpy as np
import matplotlib.pyplot as plt
import datetime
import deroulement_match_scraping

##################################################################################################
##################################################################################################

##### Choix des 4 matchs que l'on souhaite
##### Selection : 1 seul True et 2 False

cinq_derniers_matchs=True
cinq_matchs_serrés=False
cinq_matchs_non_serrés=False

##################################################################################################
##################################################################################################








##################################################################################################
#######################   CHOIX DES 4 EQUIPES
##################################################################################################

#Importation des matchs serrés et non-serrés
matchs_grand_ecart=deroulement_match_scraping.listefinalemax
matchs_petit_ecart=deroulement_match_scraping.listefinalemin

lienfev='https://www.basketball-reference.com/leagues/NBA_2022_games-february.html'
#Scrap des matchs de fevrier
df=deroulement_match_scraping.Scraping_rencontres(lienfev)
#Transformation en liste
listd=df.values.tolist()
#Je garde seulement les 4 derniers matchs
if cinq_derniers_matchs:
    liste5=[]
    for i in range(len(listd)):
        if listd[i][3]!='':
            liste5.append(listd[i])

    liste5 = liste5[-5:]
elif cinq_matchs_serrés:
    liste5=matchs_petit_ecart
else:
    liste5=matchs_grand_ecart

liste5finale=[]
for i in range(len(liste5)):
    liste5finale.append(liste5[i][0][0])
    liste5finale.append(liste5[i][4])

#Récupération des liens des matchs souhaités        
acronymnba= [['ATL','Atlanta Hawks'],['BOS','Boston Celtics'],['BRK','Brooklyn Nets'],['CHI','Chicago Bulls'],['CHO','Charlotte Hornets'],['CLE','Cleveland Cavaliers'],['DAL','Dallas Mavericks'],['DEN','Denver Nuggets'],['DET','Detroit Pistons'],['GSW','Golden State Warriors'],['HOU','Houston Rockets'],['IND','Indiana Pacers'],['LAC','Los Angeles Clippers'],['LAL','Los Angeles Lakers'],['MEM','Memphis Grizzlies'],['MIA','Miami Heat'],['MIL','Milwaukee Bucks'],['MIN','Minnesota Timberwolves'],['NOP','New Orleans Pelicans'],['NYK','New York Knicks'],['OKC','Oklahoma City Thunder'],['ORL','Orlando Magic'],['PHI','Philadelphia 76ers'],['PHO','Phoenix Suns'],['POR','Portland Trail Blazers'],['SAC','Sacramento Kings'],['SAS','San Antonio Spurs'],['TOR','Toronto Raptors'],['UTA','Utah Jazz'],['WAS','Washington Wizards']]
mois=['Oct','10','Nov','11','Dec','12','Jan','01','Feb','02','Mar','03','Apr','04']
listeliens=[]
#liste qui permettre d'afficher les dates sur les graphs
listedatematchs=[]
for i in range(1,len(liste5finale),2):
    for j in range(len(acronymnba)):
        if liste5finale[i]==acronymnba[j][1]:
            equipe=acronymnba[j][0]
    datedorigine=liste5finale[i-1]
    annee=datedorigine[-1]
    marquage = datedorigine.find(",",5,15)
    if marquage==11:
        jour=datedorigine[9:11]
    else:
        jour=datedorigine[9:10]
    for j in range(len(mois)):
        if datedorigine[5:8]==mois[j]:
            nummois=mois[j+1]
    listeliens.append("https://www.basketball-reference.com/boxscores/pbp/"+"202"+str(annee)+nummois+jour+"0"+str(equipe)+".html")
    listedatematchs.append('Date du match : '+str(jour)+"/"+str(nummois)+"/202"+str(annee))



########################################################################
############# CREATION DES LISTES A TRACER
########################################################################


#Boucle pour avoir les 4 match affichés
for e in range(4):
#Execution du scraping 
    lien_page=listeliens[e]


    df=deroulement_match_scraping.Scraping_deroulement(lien_page)
    nomsteams=deroulement_match_scraping.Scraping_noms_equipes(lien_page)
    nom1=nomsteams[0]
    nom2=nomsteams[1]
    
############# Création de 2 listes ayant le score des deux équipes : listea et listeb
#création d'une liste multidimensionnelle 
    liste = df['Score'].values.tolist()
#Conversion en string
    stri=str(liste)
    stri = stri.replace('-', "','")
    stri=re.sub("'", '', stri)
    stri=re.sub("None", '', stri)
    stri=re.sub(" ", '', stri)
    stri=re.sub(",,", ',', stri)
    
#Conversion en liste
    liste=stri.split(',')
    
    del liste[0]
    del liste[-1]
    
        
    listeaa=[]
    listebb=[]

    for i in range(len(liste)):
        if i%2==0:
            listeaa.append(liste[i])
        else:
            listebb.append(liste[i])
   
#Transformation des cases de la liste vides
    listea=[]
    listeb=[]
    n=0
    while n<len(listeaa):
        if listeaa[n]=="":
            listea.append(int(listea[n-1]))
        
        else:
            listea.append(int(listeaa[n]))
        

        n=n+1
    n=0
    while n<len(listebb):
        if listebb[n]=="":
            listeb.append(int(listeb[n-1]))
        else:
            listeb.append(int(listebb[n]))

        n=n+1

############# Création de 1 liste ayant les temps de changement de score : listet
   
    listetime = df['Time'].values.tolist()
    ll=[]
    listeq1=[]
    listeq2=[]
    listeq3=[]
    listeq4=[]

#pour comprendre où sont les différentes quarts de jeu
    for i in range(len(listetime)):
        if listetime[i]==None:
            ll.append(i)
        

#création des liste des quart temps
#q1
    if len(ll)!=10:
        tempstotal=48
        for i in range(ll[0]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=36)
            listeq1.append(newdate.time())
#q2
        for i in range(ll[1]+1,ll[2]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=24)
            listeq2.append(newdate.time())
#q3
        for i in range(ll[3]+1,ll[4]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=12)
            listeq3.append(newdate.time())
#q4
        for i in range(ll[5]+1,len(listetime)):
            if listetime[i]!=None:
                date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
                listeq4.append(date.time())
        listet=listeq1+listeq2+listeq3+listeq4
        
# cas d'overtime pour les matchs qui se sont prolongés
    else:
        tempstotal=58
        listeq5=[]
        listeq6=[]
        for i in range(ll[0]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=46)
            listeq1.append(newdate.time())
#q2
        for i in range(ll[1]+1,ll[2]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=34)
            listeq2.append(newdate.time())
#q3
        for i in range(ll[3]+1,ll[4]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=22)
            listeq3.append(newdate.time())
#q4
        for i in range(ll[5]+1,ll[6]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=10)
            listeq4.append(newdate.time())
#q5       
        for i in range(ll[7]+1,ll[8]):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            newdate = date + datetime.timedelta(minutes=5)
            listeq5.append(newdate.time())
#q6        
        for i in range(ll[9]+1,len(listetime)):
            date = datetime.datetime.strptime(listetime[i], '%M:%S.%f')
            listeq6.append(date.time())
        listet=listeq1+listeq2+listeq3+listeq4+listeq5+listeq6
    
    

    while len(listet)!=len(listea) or  len(listea)!=len(listeb):
        if len(listet)>len(listea) :
            ajout=listea[-1]
            listea.append(ajout)
        elif len(listet)>len(listeb):
            ajout=listeb[-1]
            listeb.append(ajout)
    
    listet.reverse()
    pd.plotting.register_matplotlib_converters()


############# Différence entre les points
    listez=[]
    for i in range(len(listea)):
        listez.append((int(listeb[i])-int(listea[i])))



########################################################################
############# TRACAGE DU GRAPHIQUE
########################################################################

    X  = np.linspace(0,0,len(listea))

########### 1er graph

    plt.plot(listet, listez, c='black')

    plt.xlabel("Temps")
    plt.ylabel("Différence de points")
    plt.title(str(nom1)+" vs "+str(nom2))

    plt.axhline(0, color='darkblue')
    plt.axhline(max(listez), color='green')
# Date du match
    plt.text(730,max(listez)+5,listedatematchs[e],fontsize=11,color='blue')
# Maximums des 2 equipes
    if max(listez)==max(listea):
        plt.text(50,max(listez), 'Max '+str(nom1)+' : '+str(abs(max(listez))), fontsize=10, backgroundcolor='g')
        plt.text(50,min(listez), 'Max '+str(nom2)+' : '+str(abs(min(listez))), fontsize=10, backgroundcolor='r')
    else:
        plt.text(50,max(listez), 'Max '+str(nom2)+' : '+str(abs(max(listez))), fontsize=10, backgroundcolor='g')
        plt.text(50,min(listez), 'Max '+str(nom1)+' : '+str(abs(min(listez))), fontsize=10, backgroundcolor='r')
    plt.axhline(min(listez), color='red')
# Coloration des surfaces
    plt.fill_between(listet, X, listez,where=listez>X,facecolor='green')
    plt.fill_between(listet, X, listez,where=listez<X,facecolor='red')
# Choix de la gradation des axes
    plt.ylim(min(listez)-10,max(listez)+10)
    plt.show()

########### 2ème graph

# Choix de la dimension du graph
    fig, ax = plt.subplots(1, figsize=(8, 6))

# Titre et ajouts de texte (date du match)
    fig.suptitle(str(nom1)+" vs "+str(nom2), fontsize=18)
    # Date du match
    plt.text(50,100,listedatematchs[e],fontsize=14,color='green')
    ax.set_title(str(max(listea))+" - "+str(max(listeb)), fontsize=15)
# Definition des courbes
    ax.plot(listet, listea, color="red", label=str(nom1))
    ax.plot(listet, listeb, color="blue", label=str(nom2))

    plt.xlabel("Temps")
    plt.ylabel("Points")
# Legende
    plt.legend(loc="lower right", title="Legende", frameon=False,fontsize=12)
#pour changer la gradation des axes
    plt.axis([datetime.time(0, 0, 0), datetime.time(0,tempstotal, 0), 0, max(max(listea),max(listeb))+5])
#pour convertir les dates en un axe representable graphiquement
    pd.plotting.register_matplotlib_converters()
    plt.show()


    
