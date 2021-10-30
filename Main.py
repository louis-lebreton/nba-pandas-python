import time

import pandas as pd 

import fonctions
import WebScraping
 



"""
Message de départ :

"""


fonctions.marge()
print("Analyse des données NBA : BasketBall Reference")
print("Projet Tutoret 2A")
print("Parmentier ; Makke ; Lebreton ; Messina")
fonctions.marge()

time.sleep(1.5)




"""
Programme principale :

"""

verification = True

#Menu principale :
while verification == True :

    #Menu 1 : Choix type de variable :
    fonctions.marge()
    print("1 . Statistiques individuelles :")
    print("2 . Statistiques des équipes :")
    fonctions.marge()
    choix_utilisateur_1 = input("")

    #Verification de saisi
    fonctions.verif_choix(choix_utilisateur_1, 2)
    choix_utilisateur_1 = int(choix_utilisateur_1)


    #Si les statistiques sont individuelles :
    if choix_utilisateur_1 == 1 :
        fonctions.marge()
        print("1 . Les 10 meilleurs scoreurs de la NBA")
        print("2 . Les 10 plus agés de la NBA")
        print("3 . Les 10 plus jeunes de la NBA")

        fonctions.marge()
        choix_utilisateur_2 = input("")

        #Verification de saisi
        fonctions.verif_choix(choix_utilisateur_2, 3)
        choix_utilisateur_2 = int(choix_utilisateur_2)

        if choix_utilisateur_2 == 1 :
            
            choix_saison = fonctions.choix_saison()
            if choix_saison == 1 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')
                fonctions.dix_joueurs_meilleurs_points(df)
            
            elif choix_saison == 2 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2021_totals.html')
                fonctions.dix_joueurs_meilleurs_points(df)

            elif choix_saison == 3 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')
                fonctions.dix_joueurs_meilleurs_points(df)
        

        elif choix_utilisateur_2 == 2 :
            choix_saison = fonctions.choix_saison()

            if choix_saison == 1 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')
                fonctions.dix_joueurs_ages(df)
            
            elif choix_saison == 2 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2021_totals.html')
                fonctions.dix_joueurs_ages(df)

            elif choix_saison == 3 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')
                fonctions.dix_joueurs_ages(df)


        elif choix_utilisateur_2 == 3 :
            choix_saison = fonctions.choix_saison()

            if choix_saison == 1 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')
                fonctions.dix_joueurs_jeunes(df)

            elif choix_saison == 2 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2021_totals.html')
                fonctions.dix_joueurs_jeunes(df)

            elif choix_saison == 3 :
                df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')
                fonctions.dix_joueurs_jeunes(df)
        




        else :
            exit()




    #Si les statistiques sont par équipe :
    elif choix_utilisateur_1 == 2 :
        fonctions.marge()
        print("1 . Les 10 meilleurs équipes de la NBA")
        
        fonctions.marge()
        choix_utilisateur_2 = input("")
        
        #Verification de saisi
        fonctions.verif_choix(choix_utilisateur_2, 3)
        choix_utilisateur_2 = int(choix_utilisateur_2)
        
        if choix_utilisateur_2 == 1 :
            
            choix_saison = fonctions.choix_saison()
            if choix_saison == 1 :
                df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2022_ratings.html')
                fonctions.dix_meilleurs_équipes(df)
            
            elif choix_saison == 2 :
                df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2021_ratings.html')
                fonctions.dix_meilleurs_équipes(df)

            elif choix_saison == 3 :
                df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2020_ratings.html')
                fonctions.dix_meilleurs_équipes(df)
        
        







    else :
        exit()

verification = False