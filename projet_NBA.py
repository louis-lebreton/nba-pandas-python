# -*- coding: utf-8 -*-
"""
Projet Python/pandas et NBA : fichier principal
"""

###############################################################################
# Modules importés
###############################################################################

# TODO : faire le tri et classer !!!

# non utilisés :
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# import random
# import seaborn as sns
# from PyQt5.QtWidgets import *

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

import fonctions
import WebScraping
import itertools
import pandas as pd
import numpy as np
import os

from PyQt5.QtWidgets import QComboBox, QDialog, QPushButton, QVBoxLayout, QDesktopWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 

import re
import datetime
import deroulement_match_scraping


###############################################################################
# Fonctions
###############################################################################



"""

Graphique Louis :

"""

def telechargement_images():
    
    for filename in os.listdir('images_deroulement_match') :
            os.remove('images_deroulement_match' + "/" + filename)
            
    ##################################################################################################
    ##################################################################################################
    
    ##### Choix des 4 matchs que l'on souhaite
    ##### Selection : 1 seul True et 2 False
    
    cinq_derniers_matchs=True
    cinq_matchs_serrés=False
    cinq_matchs_non_serrés=False
    

    ##################################################################################################
    #######################   CHOIX DES 4 EQUIPES
    ##################################################################################################
    
    #Importation des matchs serrés et non-serrés
    matchs_grand_ecart=deroulement_match_scraping.listefinalemax
    matchs_petit_ecart=deroulement_match_scraping.listefinalemin
    
    lienfev='https://www.basketball-reference.com/leagues/NBA_2022_games-march.html'
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
    for e in range(3):
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
        plt.axhline(max(listez), color='blue')
    # Date du match
        plt.text(730,max(listez)+5,listedatematchs[e],fontsize=11,color='green')
    # Maximums des 2 equipes
        if max(listez)==max(listea):
            plt.text(50,max(listez), 'Max '+str(nom1)+' : '+str(abs(max(listez))), fontsize=10, backgroundcolor='b')
            plt.text(50,min(listez), 'Max '+str(nom2)+' : '+str(abs(min(listez))), fontsize=10, backgroundcolor='r')
        else:
            plt.text(50,max(listez), 'Max '+str(nom2)+' : '+str(abs(max(listez))), fontsize=10, backgroundcolor='b')
            plt.text(50,min(listez), 'Max '+str(nom1)+' : '+str(abs(min(listez))), fontsize=10, backgroundcolor='r')
        plt.axhline(min(listez), color='red')
    # Coloration des surfaces
        plt.fill_between(listet, X, listez,where=listez>X,facecolor='blue')
        plt.fill_between(listet, X, listez,where=listez<X,facecolor='red')
    # Choix de la gradation des axes
        plt.axis([datetime.time(0, 0, 0), datetime.time(0,48, 0), min(listez)-10,max(listez)+10])
        plt.ioff()
        plt.savefig("images_deroulement_match/Graphe1" + str(e) + ".png")
        plt.show()
    
    ########### 2ème graph
    
    # Choix de la dimension du graph
        fig, ax = plt.subplots(1, figsize=(8, 6))
    
    # Titre et ajouts de texte (date du match)
        fig.suptitle(str(nom1)+" vs "+str(nom2), fontsize=18)
        # Date du match
        plt.text(50,max(listea)-5,listedatematchs[e],fontsize=14,color='green')
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
        plt.ioff()
        plt.savefig("images_deroulement_match/Graphe2" + str(e) + ".png")
        plt.show()
    
    
    
    




class graphique_louis(QtWidgets.QWidget):

    fermeturegraphique_louis = QtCore.pyqtSignal()
    #construction du constructeur :
    def __init__(self, parent=None):
        super(graphique_louis, self).__init__(parent)
        
        
        telechargement_images()

        self.setWindowTitle(" ")
 
  
        bouton_1 = QtWidgets.QPushButton(self)
        bouton_1.setGeometry(0, 0, 432, 288)
        bouton_1.setStyleSheet("background-image : url("'images_deroulement_match/Graphe10.png'");")

        bouton_2 = QtWidgets.QPushButton(self)
        bouton_2.setGeometry(0, 288, 432, 288)
        bouton_2.setStyleSheet("background-image : url("'images_deroulement_match/Graphe11.png'");")

        bouton_3 = QtWidgets.QPushButton(self)
        bouton_3.setGeometry(0, 576, 432, 288)
        bouton_3.setStyleSheet("background-image : url("'images_deroulement_match/Graphe12.png'");")

    
        bouton_5 = QtWidgets.QPushButton(self)
        bouton_5.setGeometry(600, 0, 576, 432)
        bouton_5.setStyleSheet("background-image : url("'images_deroulement_match/Graphe20.png'");")

        bouton_6 = QtWidgets.QPushButton(self)
        bouton_6.setGeometry(1175, 216, 576, 432)
        bouton_6.setStyleSheet("background-image : url("'images_deroulement_match/Graphe21.png'");")

        bouton_7 = QtWidgets.QPushButton(self)
        bouton_7.setGeometry(600, 432, 576, 432)
        bouton_7.setStyleSheet("background-image : url("'images_deroulement_match/Graphe22.png'");")





    def closeEvent(self, event):
        self.fermeturegraphique_louis.emit() 
        event.accept()






























"""
##############################

Comparaison équipe

##############################
"""

class comparaison_equipe(QDialog): 
       
    fermeturecomparaison_equipe = QtCore.pyqtSignal()
    
    def __init__(self, parent=None): 
        super(comparaison_equipe, self).__init__(parent)
        self.setWindowTitle(" ")

        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 
        layout = QVBoxLayout() 
        layout.addWidget(self.toolbar) 
        layout.addWidget(self.canvas)
        self.setLayout(layout) 

        listecombo_2 = ['Charlotte Hornets', 'Milwaukee Bucks', 'Memphis Grizzlies', 'Utah Jazz', 'Sacramento Kings', 'San Antonio Spurs', 'Brooklyn Nets', 'Los Angeles Lakers', 'Indiana Pacers', 'Boston Celtics', 'Phoenix Suns', 'Los Angeles Clippers', 'Golden State Warriors', 'Cleveland Cavaliers', 'Atlanta Hawks', 'Minnesota Timberwolves', 'Miami Heat', 'Portland Trail Blazers', 'Houston Rockets', 'Chicago Bulls', 'Washington Wizards', 'Dallas Mavericks', 'Denver Nuggets', 'New York Knicks', 'Philadelphia 76ers', 'Orlando Magic', 'New Orleans Pelicans', 'Toronto Raptors', 'Detroit Pistons', 'Oklahoma City Thunder', 'League Average']
                    

        self.comboBox = QComboBox(self)
        #self.comboBox.setGeometry(50, 50, 400, 35)
        self.comboBox.addItems(listecombo_2)

        self.comboBox_2 = QComboBox(self)
        #self.comboBox_2.setGeometry(50, 150, 400, 35)
        self.comboBox_2.addItems(listecombo_2)

        self.choix_equipe1 = QtWidgets.QLabel(self)
        self.choix_equipe1.setText("Choix de l'équipe 1 :")
        self.choix_equipe2 = QtWidgets.QLabel(self)
        self.choix_equipe2.setText("Choix de l'équipe 2 :")
        self.blanc = QtWidgets.QLabel(self)
        self.blanc.setText(" ")

        layout.addWidget(self.choix_equipe1)
        layout.addWidget(self.comboBox_2)
        layout.addWidget(self.choix_equipe2)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.blanc)

        self.btn = QPushButton('Comparer', self)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(lambda: self.plot(self.comboBox_2.currentText(), self.comboBox.currentText()))


        
        
    
    def plot(self, team_1, team_2): 
        data = pd.read_csv('mesina_test/test_projet/Team/total.csv') 
        df = pd.DataFrame(data)
        L = list(df)
        L.remove('Rk')
        L.remove('Unnamed: 0')
        L.remove('Team')
        
   




        X_1 = df.loc[df['Team'] == team_1]
        X_2 = df.loc[df['Team'] == team_2]
        X_1 = X_1.values.tolist()
        X_2 = X_2.values.tolist()

        X_1 = itertools.chain(*X_1)
        X_1 = list(X_1)

        X_2 = itertools.chain(*X_2)
        X_2 = list(X_2)

        for _ in range(3):
            del X_1[0]
            del X_2[0]



        df_2 = pd.DataFrame({'Stat': L, 
                    team_1: X_1, 
                    team_2: X_2})
    
        #print(df_2[team_1])

        self.figure.clear() 
        


        y = df_2['Stat']
        x1 = df_2[team_1]
        x2 = df_2[team_2]
        
        #print(y)
        #print(x1)
        #print(x2)
       
        plt.barh(y, x1, color = 'r')
        plt.barh(y, -x2, color = 'b') 

        self.canvas.draw()

    def closeEvent(self, event):
        self.fermeturecomparaison_equipe.emit() 
        event.accept()



















"""
##############################

Statistiques équipe

##############################
"""



class statistiques_equipe(QDialog): 

    fermeturestatistiques_equipe = QtCore.pyqtSignal()
       
    
    def __init__(self, parent=None): 
        super(statistiques_equipe, self).__init__(parent)
        self.setWindowTitle(" ")

        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 
        layout = QVBoxLayout() 
        layout.addWidget(self.toolbar) 
        layout.addWidget(self.canvas)
        self.setLayout(layout) 

        listecombo = ['G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS/G']
        #liste_a = ['G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS/G']
        listecombo_2 = ["ATL" , "BOS" , "BRK" ,"CHI", "CHO", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAS", "TOR", "UTA", "WAS"]

        self.comboBox = QComboBox(self)
        #self.comboBox.setGeometry(50, 50, 400, 35)
        self.comboBox.addItems(listecombo)

        self.comboBox_2 = QComboBox(self)
        #self.comboBox_2.setGeometry(50, 150, 400, 35)
        self.comboBox_2.addItems(listecombo_2)

        self.choix_equipe = QtWidgets.QLabel(self)
        self.choix_equipe.setText("Choix de l'équipe :")
        self.choix_stat = QtWidgets.QLabel(self)
        self.choix_stat.setText("Choix de la catégorie statistique :")
        self.blanc = QtWidgets.QLabel(self)
        self.blanc.setText(" ")

        layout.addWidget(self.choix_equipe)
        layout.addWidget(self.comboBox_2)
        layout.addWidget(self.choix_stat)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.blanc)

        self.btn = QPushButton('Générer graphique', self)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(lambda: self.plot(self.comboBox_2.currentText(), self.comboBox.currentText()))

        
   
    
    def plot(self, team, stat): 
        data = pd.read_csv('mesina_test/test_projet/stats_joueurs/fichier'+ team +'.csv') 
        df = pd.DataFrame(data)
        L = list(df)
        df2 = df.sort_values(by = [stat], ascending = False)
        X = list(df2[L[2]])
        Y = list(df2[stat])
        
        
        self.figure.clear() 
        plt.bar(X, Y, color='b')
        plt.xlabel("Players")
        plt.ylabel(stat)
        plt.xticks(rotation=90)

        self.canvas.draw() 

    def creation_graph(self, team, stat):
        data = pd.read_csv('mesina_test/test_projet/stats_joueurs/fichier'+ team +'.csv')
        df = pd.DataFrame(data)
        L = list(df)
        df2 = df.sort_values(by = [stat], ascending = False)
        X = list(df2[L[2]])
        Y = list(df2[stat])
        plt.bar(X, Y, color='b')
        plt.xlabel("Players")
        plt.ylabel(stat)
        plt.xticks(rotation=90)
        plt.show() 

    def closeEvent(self, event):
        self.fermeturestatistiques_equipe.emit() 
        event.accept()

    


















"""
##############################

top 10 scoreurs 

##############################
"""


class top_10_scoreurs(QtWidgets.QWidget):

        fermeturefentop_10_scoreurs = QtCore.pyqtSignal()

        def __init__(self , parent = None):
                
                super().__init__(parent)
                self.setWindowTitle(" ")

                self.data = WebScraping.Scraping_joueurs_NBA_total("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
                self.dix_meilleurs = fonctions.dix_joueurs_meilleurs_points_tk2(self.data)

                #print(self.dix_meilleurs)
                
                self.joueurs = self.dix_meilleurs[0]
                self.PTS = self.dix_meilleurs[1]
                self.team = self.dix_meilleurs[2]


                Liste_acronymes = []
                for i in range(len(self.joueurs)):

                        self.joueur = self.dix_meilleurs[0][i]
                        self.score = self.dix_meilleurs[1][i]
                        self.team_2 = self.dix_meilleurs[2][i]

                        chemin="images_joueurs_et_csv_equipes/teams/" + self.team_2 + ".csv"
                        self.df = pd.read_csv(chemin,index_col=0,header=None)

                        self.liste_1 = self.df.index.tolist()
                        self.liste_2 = self.df.values.tolist()
                        self.liste_2 = itertools.chain(*self.liste_2)
                        self.liste_2 = list(self.liste_2)
                        

                        for e in range(len(self.liste_1)):
                                if str(self.liste_1[e]) == str(self.joueur) :
                                        resultat = str(self.liste_2[e])
                                        Liste_acronymes.append(resultat)
                        
                
                Liste_acronymes
  
                self.liste_image = []
                for i in Liste_acronymes :
                        self.liste_image.append("images_joueurs_et_csv_equipes/images_players/"+str(i)+".jpg")
                
                

                bouton_1 = QtWidgets.QPushButton(self)
                bouton_1.setGeometry(0, 0, 120, 180)
                bouton_1.setStyleSheet("background-image : url('" + self.liste_image[0] + "');")

                bouton_2 = QtWidgets.QPushButton(self)
                bouton_2.setGeometry(300, 0, 120, 180)
                bouton_2.setStyleSheet("background-image : url('" + self.liste_image[1] + "');")

                bouton_3 = QtWidgets.QPushButton(self)
                bouton_3.setGeometry(600, 0, 120, 180)
                bouton_3.setStyleSheet("background-image : url('" + self.liste_image[2] + "');")

                bouton_4 = QtWidgets.QPushButton(self)
                bouton_4.setGeometry(900, 0, 120, 180)
                bouton_4.setStyleSheet("background-image : url('" + self.liste_image[3] + "');")

                bouton_5 = QtWidgets.QPushButton(self)
                bouton_5.setGeometry(1200, 0, 120, 180)
                bouton_5.setStyleSheet("background-image : url('" + self.liste_image[4] + "');")

                bouton_6 = QtWidgets.QPushButton(self)
                bouton_6.setGeometry(0, 180, 120, 180)
                bouton_6.setStyleSheet("background-image : url('" + self.liste_image[5] + "');")

                bouton_7 = QtWidgets.QPushButton(self)
                bouton_7.setGeometry(300, 180, 120, 180)
                bouton_7.setStyleSheet("background-image : url('" + self.liste_image[6] + "');")

                bouton_8 = QtWidgets.QPushButton(self)
                bouton_8.setGeometry(600, 180, 120, 180)
                bouton_8.setStyleSheet("background-image : url('" + self.liste_image[7] + "');")

                bouton_9 = QtWidgets.QPushButton(self)
                bouton_9.setGeometry(900, 180, 120, 180)
                bouton_9.setStyleSheet("background-image : url('" + self.liste_image[8] + "');")

                bouton_10 = QtWidgets.QPushButton(self)
                bouton_10.setGeometry(1200, 180, 120, 180)
                bouton_10.setStyleSheet("background-image : url('" + self.liste_image[9] + "');")



                self.lbl_1 = QtWidgets.QLabel(self)
                self.lbl_1.setGeometry(120, 0, 150, 150)
                self.lbl_1.setText(" 1. \n Nom : "+ str(self.dix_meilleurs[0][0]) + " \n Points par match : " + str(self.dix_meilleurs[1][0]) + "")

                self.lbl_2 = QtWidgets.QLabel(self)
                self.lbl_2.setGeometry(420, 0, 150, 150)
                self.lbl_2.setText(" 2. \n Nom : "+ str(self.dix_meilleurs[0][1]) + " \n Points par match : " + str(self.dix_meilleurs[1][1]) + "")

                self.lbl_3 = QtWidgets.QLabel(self)
                self.lbl_3.setGeometry(720, 0, 150, 150)
                self.lbl_3.setText(" 3. \n Nom : "+ str(self.dix_meilleurs[0][2]) + " \n Points par match : " + str(self.dix_meilleurs[1][2]) + "")

                self.lbl_4 = QtWidgets.QLabel(self)
                self.lbl_4.setGeometry(1020, 0, 150, 150)
                self.lbl_4.setText(" 4. \n Nom : "+ str(self.dix_meilleurs[0][3]) + " \n Points par match : " + str(self.dix_meilleurs[1][3]) + "")

                self.lbl_5 = QtWidgets.QLabel(self)
                self.lbl_5.setGeometry(1320, 0, 150, 150)
                self.lbl_5.setText(" 5. \n Nom : "+ str(self.dix_meilleurs[0][4]) + " \n Points par match : " + str(self.dix_meilleurs[1][4]) + "")

                self.lbl_6 = QtWidgets.QLabel(self)
                self.lbl_6.setGeometry(120, 180, 150, 150)
                self.lbl_6.setText(" 6. \n Nom : "+ str(self.dix_meilleurs[0][5]) + " \n Points par match : " + str(self.dix_meilleurs[1][5]) + "")

                self.lbl_7 = QtWidgets.QLabel(self)
                self.lbl_7.setGeometry(420, 180, 150, 150)
                self.lbl_7.setText(" 7. \n Nom : "+ str(self.dix_meilleurs[0][6]) + " \n Points par match : " + str(self.dix_meilleurs[1][6]) + "")

                self.lbl_8 = QtWidgets.QLabel(self)
                self.lbl_8.setGeometry(720, 180, 150, 150)
                self.lbl_8.setText(" 8. \n Nom : "+ str(self.dix_meilleurs[0][7]) + " \n Points par match : " + str(self.dix_meilleurs[1][7]) + "")

                self.lbl_9 = QtWidgets.QLabel(self)
                self.lbl_9.setGeometry(1020, 180, 150, 150)
                self.lbl_9.setText(" 9. \n Nom : "+ str(self.dix_meilleurs[0][8]) + " \n Points par match : " + str(self.dix_meilleurs[1][8]) + "")

                self.lbl_10 = QtWidgets.QLabel(self)
                self.lbl_10.setGeometry(1320, 180, 150, 150)
                self.lbl_10.setText(" 10. \n Nom : "+ str(self.dix_meilleurs[0][9]) + " \n Points par match : " + str(self.dix_meilleurs[1][9]) + "")



        def closeEvent(self, event):
            self.fermeturefentop_10_scoreurs.emit() 
            event.accept()

































"""
##############################

Fenetre 4

##############################
"""

class fenetre_4(QtWidgets.QWidget):


    fermeturefen4 = QtCore.pyqtSignal()


    def __init__(self, joueur, team):
        super().__init__()
        self.setWindowTitle(" ")

        ##################### choix du joueur
        self.player = joueur 
        self.team = team
        ##################### 
        #récupération nom du joueur
        cheminjoueur="images_joueurs_et_csv_equipes/teams/"+self.team+".csv"
        self.df = pd.read_csv(cheminjoueur,header = None)
        self.liste2 = self.df.values.tolist()
        i=0
        # récupréation du rang du joueur sur le tableau .csv team
        while self.liste2[i][1] != joueur:
            i=i+1

        #chemin du fichier pour le .csv
        chemin = "sommaires_players/" + self.player + ".csv"
        #conversion en dataframe
        self.df = pd.read_csv(chemin,index_col = 0,header = None)
        self.liste = self.df.values.tolist()
        

        self.left = 300
        self.top = 300
        self.width = 600
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable(i) 
   
        self.layout = QtWidgets.QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

    def createTable(self, i): 
        self.tableWidget = QtWidgets.QTableWidget() 
  
        
        self.tableWidget.setRowCount(11)  
  
        
        self.tableWidget.setColumnCount(3)   
  
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem(self.liste2[i][0])) 
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("2021-2022")) 
        self.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Carrière")) 

        self.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem('Matchs joués')) 
        self.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem('Points')) 
        self.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem('Rebonds')) 
        self.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem('Passes décisives')) 
        self.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem('% de shoots marqués')) 
        self.tableWidget.setItem(6,0, QtWidgets.QTableWidgetItem('% de shoots marqués à 3 points')) 
        self.tableWidget.setItem(7,0, QtWidgets.QTableWidgetItem('% de lancers francs marqués')) 
        self.tableWidget.setItem(8,0, QtWidgets.QTableWidgetItem('% de shoots marqués ajusté aux 3 points')) 
        self.tableWidget.setItem(9,0, QtWidgets.QTableWidgetItem("Note d'efficience")) 
        self.tableWidget.setItem(10,0, QtWidgets.QTableWidgetItem('Victoires par sa contribution')) 

        for e in range(1, 11):
            self.tableWidget.setItem(e,1 ,QtWidgets.QTableWidgetItem(self.liste[e][0]))

        for j in range(1, 11):
            self.tableWidget.setItem(j ,2 ,QtWidgets.QTableWidgetItem(self.liste[j][1]))

   
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QtWidgets.QHeaderView.Stretch)

 


        
   
    
"""
##############################

Fenetre 3

##############################
"""


class fenetre_3(QtWidgets.QWidget):


    fermeturefen3 = QtCore.pyqtSignal()

    def __init__(self, equipe):
        super().__init__()
        self.setWindowTitle(" ")
        self.team = equipe

        chemin="images_joueurs_et_csv_equipes/teams/"+self.team+".csv"
        # importation du .csv en dataframe
        self.df = pd.read_csv(chemin,index_col=0,header=None)
        #création d'une liste multidimensionnelle des noms de fichiers des joueurs
        self.liste = self.df.values.tolist()

        while len(self.liste) < 20 :
            self.liste.append('NULL')

        listechemin=[]
        #création d'une liste avec les chemins de fichiers de chaque joueur
        for i in self.liste:
            if i == 'NULL' :
                chemin="gris.jpg"
                listechemin.append(chemin)
            else :
                #j'utilise i[0] et pas i car c'est un liste multidimensionnelle
                chemin="images_joueurs_et_csv_equipes/images_players/"+str(i[0])+".jpg"
                listechemin.append(chemin)
        
    

        a = QtWidgets.QPushButton(self)
        a.setGeometry(0, 0, 120, 180)
        a.setStyleSheet("background-image : url('" + listechemin[0] + "');")
        a.clicked.connect(lambda: self.appelfen4(str(self.liste[0][0]), self.team))

        b = QtWidgets.QPushButton(self)
        b.setGeometry(120, 0, 120, 180)
        b.setStyleSheet("background-image : url('" + listechemin[1] + "');")
        b.clicked.connect(lambda: self.appelfen4(str(self.liste[1][0]), self.team))
        
        


        c = QtWidgets.QPushButton(self)
        c.setGeometry(240, 0, 120, 180)
        c.setStyleSheet("background-image : url('" + listechemin[2] + "');")
        c.clicked.connect(lambda: self.appelfen4(str(self.liste[2][0]), self.team))

        d = QtWidgets.QPushButton(self)
        d.setGeometry(360, 0, 120, 180)
        d.setStyleSheet("background-image : url('" + listechemin[3] + "');")
        d.clicked.connect(lambda: self.appelfen4(str(self.liste[3][0]), self.team))

        e = QtWidgets.QPushButton(self)
        e.setGeometry(480, 0, 120, 180)
        e.setStyleSheet("background-image : url('" + listechemin[4] + "');")
        e.clicked.connect(lambda: self.appelfen4(str(self.liste[4][0]), self.team))

        f = QtWidgets.QPushButton(self)
        f.setGeometry(0, 180, 120, 180)
        f.setStyleSheet("background-image : url('" + listechemin[5] + "');")
        f.clicked.connect(lambda: self.appelfen4(str(self.liste[5][0]), self.team))

        g = QtWidgets.QPushButton(self)
        g.setGeometry(120, 180, 120, 180)
        g.setStyleSheet("background-image : url('" + listechemin[6] + "');")
        g.clicked.connect(lambda: self.appelfen4(str(self.liste[6][0]), self.team))

        h = QtWidgets.QPushButton(self)
        h.setGeometry(240, 180, 120, 180)
        h.setStyleSheet("background-image : url('" + listechemin[7] + "');")
        h.clicked.connect(lambda: self.appelfen4(str(self.liste[7][0]), self.team))

        i = QtWidgets.QPushButton(self)
        i.setGeometry(360, 180, 120, 180)
        i.setStyleSheet("background-image : url('" + listechemin[8] + "');")
        i.clicked.connect(lambda: self.appelfen4(str(self.liste[8][0]), self.team))

        j = QtWidgets.QPushButton(self)
        j.setGeometry(480, 180, 120, 180)
        j.setStyleSheet("background-image : url('" + listechemin[9] + "');")
        j.clicked.connect(lambda: self.appelfen4(str(self.liste[9][0]), self.team))

        k = QtWidgets.QPushButton(self)
        k.setGeometry(0, 360, 120, 180)
        k.setStyleSheet("background-image : url('" + listechemin[10] + "');")
        k.clicked.connect(lambda: self.appelfen4(str(self.liste[10][0]), self.team))

        l = QtWidgets.QPushButton(self)
        l.setGeometry(120, 360, 120, 180)
        l.setStyleSheet("background-image : url('" + listechemin[11] + "');")
        l.clicked.connect(lambda: self.appelfen4(str(self.liste[11][0]), self.team))

        m = QtWidgets.QPushButton(self)
        m.setGeometry(240, 360, 120, 180)
        m.setStyleSheet("background-image : url('" + listechemin[12] + "');")
        m.clicked.connect(lambda: self.appelfen4(str(self.liste[12][0]), self.team))

        n = QtWidgets.QPushButton(self)
        n.setGeometry(360, 360, 120, 180)
        n.setStyleSheet("background-image : url('" + listechemin[13] + "');")
        n.clicked.connect(lambda: self.appelfen4(str(self.liste[13][0]), self.team))

        o = QtWidgets.QPushButton(self)
        o.setGeometry(480, 360, 120, 180)
        o.setStyleSheet("background-image : url('" + listechemin[14] + "');")
        o.clicked.connect(lambda: self.appelfen4(str(self.liste[14][0]), self.team))

        p = QtWidgets.QPushButton(self)
        p.setGeometry(0, 540, 120, 180)
        p.setStyleSheet("background-image : url('" + listechemin[15] + "');")
        p.clicked.connect(lambda: self.appelfen4(str(self.liste[15][0]), self.team))


        q = QtWidgets.QPushButton(self)
        q.setGeometry(120, 540, 120, 180)
        q.setStyleSheet("background-image : url('" + listechemin[16] + "');")
        q.clicked.connect(lambda: self.appelfen4(str(self.liste[16][0]), self.team))

        r = QtWidgets.QPushButton(self)
        r.setGeometry(240, 540, 120, 180)
        r.setStyleSheet("background-image : url('" + listechemin[17] + "');")
        r.clicked.connect(lambda: self.appelfen4(str(self.liste[17][0]), self.team))

        s = QtWidgets.QPushButton(self)
        s.setGeometry(360, 540, 120, 180)
        s.setStyleSheet("background-image : url('" + listechemin[18] + "');")
        s.clicked.connect(lambda: self.appelfen4(str(self.liste[18][0]), self.team))

        self.fenetre4 = None 


###

    def appelfen4(self, joueur, team):
        """méthode appelée par le bouton, Lance la deuxième fenêtre
        """
        if self.fenetre4==None:
            self.fenetre4 = fenetre_4(joueur, team)
            # prépare la future fermeture de la fenêtre 2 
            self.fenetre4.fermeturefen4.connect(self.fen4close)
            # affiche la 2ème fenêtre
            self.fenetre4.show()
    

    def fen4close(self):
        """méthode appelée par la fermeture de la fenêtre 2
        """
        self.fenetre4 = None


###




"""
##############################

Fenetre 2

##############################
"""




class fenetre_2(QtWidgets.QWidget):


    fermeturefen2 = QtCore.pyqtSignal()


    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(" ")
        #self.setGeometry(0, 0, 1200, 1800)

        ATL = QtWidgets.QPushButton(self)
        ATL.setGeometry(0, 0, 125, 125)
        ATL.setStyleSheet("background-image : url('logos_nba/ATL_2022.png');")
        ATL.clicked.connect(lambda: self.appelfen3("ATL"))

        BOS = QtWidgets.QPushButton(self)
        BOS.setGeometry(125, 0, 125, 125)
        BOS.setStyleSheet("background-image : url('logos_nba/BOS_2022.png');")
        BOS.clicked.connect(lambda: self.appelfen3("BOS"))

        BRK = QtWidgets.QPushButton(self)
        BRK.setGeometry(250, 0, 125, 125)
        BRK.setStyleSheet("background-image : url('logos_nba/BRK_2022.png');")
        BRK.clicked.connect(lambda: self.appelfen3("BRK"))

        CHI = QtWidgets.QPushButton(self)
        CHI.setGeometry(375, 0, 125, 125)
        CHI.setStyleSheet("background-image : url('logos_nba/CHI_2022.png');")
        CHI.clicked.connect(lambda: self.appelfen3("CHI"))

        CHO = QtWidgets.QPushButton(self)
        CHO.setGeometry(500, 0, 125, 125)
        CHO.setStyleSheet("background-image : url('logos_nba/CHO_2022.png');")
        CHO.clicked.connect(lambda: self.appelfen3("CHO"))

        CLE = QtWidgets.QPushButton(self)
        CLE.setGeometry(625, 0, 125, 125)
        CLE.setStyleSheet("background-image : url('logos_nba/CLE_2022.png');")
        CLE.clicked.connect(lambda: self.appelfen3("CLE"))

        DAL = QtWidgets.QPushButton(self)
        DAL.setGeometry(0, 125, 125, 125)
        DAL.setStyleSheet("background-image : url('logos_nba/DAL_2022.png');")
        DAL.clicked.connect(lambda: self.appelfen3("DAL"))

        DEN = QtWidgets.QPushButton(self)
        DEN.setGeometry(125, 125, 125, 125)
        DEN.setStyleSheet("background-image : url('logos_nba/DEN_2022.png');")
        DEN.clicked.connect(lambda: self.appelfen3("DEN"))
        
        DET = QtWidgets.QPushButton(self)
        DET.setGeometry(250, 125, 125, 125)
        DET.setStyleSheet("background-image : url('logos_nba/DET_2022.png');")
        DET.clicked.connect(lambda: self.appelfen3("DET"))

        GSW = QtWidgets.QPushButton(self)
        GSW.setGeometry(375, 125, 125, 125)
        GSW.setStyleSheet("background-image : url('logos_nba/GSW_2022.png');")
        GSW.clicked.connect(lambda: self.appelfen3("GSW"))

        HOU = QtWidgets.QPushButton(self)
        HOU.setGeometry(500, 125, 125, 125)
        HOU.setStyleSheet("background-image : url('logos_nba/HOU_2022.png');")
        HOU.clicked.connect(lambda: self.appelfen3("HOU"))

        IND = QtWidgets.QPushButton(self)
        IND.setGeometry(625, 125, 125, 125)
        IND.setStyleSheet("background-image : url('logos_nba/IND_2022.png');")
        IND.clicked.connect(lambda: self.appelfen3("IND"))

        LAC = QtWidgets.QPushButton(self)
        LAC.setGeometry(0, 250, 125, 125)
        LAC.setStyleSheet("background-image : url('logos_nba/LAC_2022.png');")
        LAC.clicked.connect(lambda: self.appelfen3("LAC"))

        LAL = QtWidgets.QPushButton(self)
        LAL.setGeometry(125, 250, 125, 125)
        LAL.setStyleSheet("background-image : url('logos_nba/LAL_2022.png');")
        LAL.clicked.connect(lambda: self.appelfen3("LAL"))

        MEM = QtWidgets.QPushButton(self)
        MEM.setGeometry(250, 250, 125, 125)
        MEM.setStyleSheet("background-image : url('logos_nba/MEM_2022.png');")
        MEM.clicked.connect(lambda: self.appelfen3("MEM"))

        MIA = QtWidgets.QPushButton(self)
        MIA.setGeometry(375, 250, 125, 125)
        MIA.setStyleSheet("background-image : url('logos_nba/MIA_2022.png');")
        MIA.clicked.connect(lambda: self.appelfen3("MIA"))

        MIL = QtWidgets.QPushButton(self)
        MIL.setGeometry(500, 250, 125, 125)
        MIL.setStyleSheet("background-image : url('logos_nba/MIL_2022.png');")
        MIL.clicked.connect(lambda: self.appelfen3("MIL"))

        MIN = QtWidgets.QPushButton(self)
        MIN.setGeometry(625, 250, 125, 125)
        MIN.setStyleSheet("background-image : url('logos_nba/MIN_2022.png');")
        MIN.clicked.connect(lambda: self.appelfen3("MIN"))

        NOP = QtWidgets.QPushButton(self)
        NOP.setGeometry(0, 375, 125, 125)
        NOP.setStyleSheet("background-image : url('logos_nba/NOP_2022.png');")
        NOP.clicked.connect(lambda: self.appelfen3("NOP"))

        NYK = QtWidgets.QPushButton(self)
        NYK.setGeometry(125, 375, 125, 125)
        NYK.setStyleSheet("background-image : url('logos_nba/NYK_2022.png');")
        NYK.clicked.connect(lambda: self.appelfen3("NYK"))

        OKC = QtWidgets.QPushButton(self)
        OKC.setGeometry(250, 375, 125, 125)
        OKC.setStyleSheet("background-image : url('logos_nba/OKC_2022.png');")
        OKC.clicked.connect(lambda: self.appelfen3("OKC"))

        ORL = QtWidgets.QPushButton(self)
        ORL.setGeometry(375, 375, 125, 125)
        ORL.setStyleSheet("background-image : url('logos_nba/ORL_2022.png');")
        ORL.clicked.connect(lambda: self.appelfen3("ORL"))

        PHI = QtWidgets.QPushButton(self)
        PHI.setGeometry(500, 375, 125, 125)
        PHI.setStyleSheet("background-image : url('logos_nba/PHI_2022.png');")
        PHI.clicked.connect(lambda: self.appelfen3("PHI"))

        PHO = QtWidgets.QPushButton(self)
        PHO.setGeometry(625, 375, 125, 125)
        PHO.setStyleSheet("background-image : url('logos_nba/PHO_2022.png');")
        PHO.clicked.connect(lambda: self.appelfen3("PHO"))

        POR = QtWidgets.QPushButton(self)
        POR.setGeometry(0, 500, 125, 125)
        POR.setStyleSheet("background-image : url('logos_nba/POR_2022.png');")
        POR.clicked.connect(lambda: self.appelfen3("POR"))

        SAC = QtWidgets.QPushButton(self)
        SAC.setGeometry(125, 500, 125, 125)
        SAC.setStyleSheet("background-image : url('logos_nba/SAC_2022.png');")
        SAC.clicked.connect(lambda: self.appelfen3("SAC"))

        SAS = QtWidgets.QPushButton(self)
        SAS.setGeometry(250, 500, 125, 125)
        SAS.setStyleSheet("background-image : url('logos_nba/SAS_2022.png');")
        SAS.clicked.connect(lambda: self.appelfen3("SAS"))

        TOR = QtWidgets.QPushButton(self)
        TOR.setGeometry(375, 500, 125, 125)
        TOR.setStyleSheet("background-image : url('logos_nba/TOR_2022.png');")
        TOR.clicked.connect(lambda: self.appelfen3("TOR"))

        UTA = QtWidgets.QPushButton(self)
        UTA.setGeometry(500, 500, 125, 125)
        UTA.setStyleSheet("background-image : url('logos_nba/UTA_2022.png');")
        UTA.clicked.connect(lambda: self.appelfen3("UTA"))

        WAS = QtWidgets.QPushButton(self)
        WAS.setGeometry(625, 500, 125, 125)
        WAS.setStyleSheet("background-image : url('logos_nba/WAS_2022.png');")
        WAS.clicked.connect(lambda: self.appelfen3("WAS"))

        self.fenetre3 = None 




    def closeEvent(self, event):
        """à la fermeture de cette fenêtre 2, celle-ci envoie un signal à la 
           fenêtre 1 appelante
        """
        self.fermeturefen2.emit() 
        event.accept()


###

    def appelfen3(self, team):
        """méthode appelée par le bouton, Lance la deuxième fenêtre
        """
        if self.fenetre3==None:
            self.fenetre3 = fenetre_3(team)
            # prépare la future fermeture de la fenêtre 2 
            self.fenetre3.fermeturefen3.connect(self.fen3close)
            # affiche la 2ème fenêtre
            self.fenetre3.show()
    

    def fen3close(self):
        """méthode appelée par la fermeture de la fenêtre 2
        """
        self.fenetre3 = None



###



"""
##############################

Fenetre 1

##############################
"""




#QWidget permet de crée des fenetres
class MyWindow(QtWidgets.QWidget):

    #construction du constructeur :
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(" ")
        #self.setGeometry(100, 100, 400, 400)

        #création d'un label
        self.lbl = QtWidgets.QLabel(self)
        #self.lbl.setGeometry(20, 30, 350, 50)
        self.lbl.setText("Analyse de données NBA avec Python")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet('QLabel{ \
            color: black; \
            font-weight: bold; \
            font-size: 40px; \
            text-align: center; \
            }'
                           'QPushButton {background-color: #c8dce3; color: black; font-weight:bold; font-size:20px;}'
                            'MyWindow {background-color: #8babb5;}')
        #self.setStyleSheet('QPushButton {background-color: red; color: blue; font-weight:bold;}')



        qBTN1 = QtWidgets.QPushButton(self)
        qBTN1.setText("Statistiques joueurs (saison/carrière)")
        # qBTN1.setGeometry(100, 100, 200, 30)
        qBTN1.clicked.connect(self.appelfen2)

        qBTN2 = QtWidgets.QPushButton(self)
        qBTN2.setText("Statistiques équipes (saison)")
        qBTN2.clicked.connect(self.appelstatistiques_equipe)

        qBTN3 = QtWidgets.QPushButton(self)
        qBTN3.setText("Bonus : comparaison de deux équipes")
        qBTN3.clicked.connect(self.appelcomparaison_equipe)

        qBTN4 = QtWidgets.QPushButton(self)
        qBTN4.setText("Top 10 meilleurs marqueurs (saison)")
        qBTN4.clicked.connect(self.appelfen_top_10_scoreurs)
        
        qBTN5 = QtWidgets.QPushButton(self)
        qBTN5.setText("Déroulement matchs récents")
        qBTN5.clicked.connect(self.appelgraphique_louis)

        qBTN6 = QtWidgets.QPushButton(self)
        qBTN6.setText("Bonus : matchs les moins serrés (saison)")
        qBTN6.clicked.connect(self.appelgraphique_louis)

        qBTN7 = QtWidgets.QPushButton(self)
        qBTN7.setText("Bonus : matchs les plus serrés (saison)")
        qBTN7.clicked.connect(self.appelgraphique_louis)

        qBTN8 = QtWidgets.QPushButton(self)
        qBTN8.setText("Quitter")
        qBTN8.clicked.connect(self.quitter)

        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap('STID.png') 
        # self.pixmap.scaledToWidth(15664)

        self.pixmap_resized = self.pixmap.scaledToWidth(200)
        # self.pixmap_resized.save('STID.png')

        self.label.setPixmap(self.pixmap_resized)


        # positionne le bouton dans la fenêtre
        posit = QtWidgets.QGridLayout()
        posit.addWidget(self.lbl, 0, 0)
        posit.addWidget(self.label, 1, 0)
        posit.addWidget(qBTN1, 2, 0)
        posit.addWidget(qBTN2, 3, 0)
        posit.addWidget(qBTN3, 4, 0)
        posit.addWidget(qBTN4, 5, 0)
        posit.addWidget(qBTN5, 6, 0)
        posit.addWidget(qBTN6, 7, 0)
        posit.addWidget(qBTN7, 8, 0)
        posit.addWidget(qBTN8, 9, 0)


        self.setLayout(posit)

        self.fenetre2 = None
        self.top_10_scoreurs = None
        self.statistiques_equipe = None
        self.comparaison_equipe = None
        self.graphique_louis = None

    def quitter(self):
        quit()


###


    def appelfen2(self):
        """méthode appelée par le bouton, Lance la deuxième fenêtre
        """
        if self.fenetre2==None:
            self.fenetre2 = fenetre_2()
            # prépare la future fermeture de la fenêtre 2 
            self.fenetre2.fermeturefen2.connect(self.fen2close)
            # affiche la 2ème fenêtre
            self.fenetre2.show()

    def appelfen_top_10_scoreurs(self):
        if self.top_10_scoreurs==None:
            self.top_10_scoreurs = top_10_scoreurs()
            # prépare la future fermeture de la fenêtre 2 
            self.top_10_scoreurs.fermeturefentop_10_scoreurs.connect(self.top_10_scoreursclose)
            # affiche la 2ème fenêtre
            self.top_10_scoreurs.show()

    def appelstatistiques_equipe(self):
        if self.statistiques_equipe==None:
                self.statistiques_equipe = statistiques_equipe()
                # prépare la future fermeture de la fenêtre 2 
                self.statistiques_equipe.fermeturestatistiques_equipe.connect(self.statistiques_equipeclose)
                # affiche la 2ème fenêtre
                self.statistiques_equipe.show()

    def appelcomparaison_equipe(self):
        if self.comparaison_equipe==None:
                self.comparaison_equipe = comparaison_equipe()
                # prépare la future fermeture de la fenêtre 2 
                self.comparaison_equipe.fermeturecomparaison_equipe.connect(self.comparaison_equipeclose)
                # affiche la 2ème fenêtre
                self.comparaison_equipe.show()
                
    def appelgraphique_louis(self):
        if self.graphique_louis==None:
                self.graphique_louis = graphique_louis()
                # prépare la future fermeture de la fenêtre 2 
                self.graphique_louis.fermeturegraphique_louis.connect(self.graphique_louisclose)
                # affiche la 2ème fenêtre
                self.graphique_louis.show()
                
                

    def fen2close(self):
        self.fenetre2 = None

    def top_10_scoreursclose(self):
        self.top_10_scoreurs = None

    def statistiques_equipeclose(self):
        self.statistiques_equipe = None

    def comparaison_equipeclose(self):
        self.comparaison_equipe = None
        
    def graphique_louisclose(self):
        self.graphique_louis = None


#création de l'instance de la fenetre Pyqt
if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    fenetre1 =  MyWindow()
    fenetre1.show()
    sys.exit(app.exec_())