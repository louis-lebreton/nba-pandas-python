import tkinter as tk 
from tkinter import ttk

import fonctions
import WebScraping
 



"""
Fonctions spécifiques :

"""

def reset(fen):
    for widget in fen.winfo_children():
        widget.destroy()

def reset_app():
    reset(app)

def DataFrame_NBA_saison(n):
    global df
    if n == 1 :
        df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')
    elif n == 2 :
        df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2021_totals.html')
    elif n == 3 :
        df = WebScraping.Scraping_joueurs_NBA_total('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')
    elif n == 4 :
        df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2022.html')
    elif n == 5 :
        df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2021.html')
    elif n == 6 :
        df = WebScraping.Scraping_equipes_NBA('https://www.basketball-reference.com/leagues/NBA_2020.html')
    else :
        exit()


"""
Ensembles des menus de l'app

"""


def menu_1():

    reset_app()

    titre = tk.Label(text = "Projet tutore 2A \n Analyse des données NBA \n Parmentier ; Makké ; Lebreton ; Messina")
    bouton_app_1 = tk.Button(app, text = "Accèder aux analyses" , command = menu_2)
    bouton_app_2 = tk.Button(app, text = "Quitter" , command = app.quit)
    


    
    titre.pack(expand = 1)
    bouton_app_1.pack()
    bouton_app_2.pack(expand = 1)

def menu_2():

    reset_app()

    titre = tk.Label(text = "Choix des statistiques par équipe / indiviuelle :")

    bouton_app_1 = tk.Button(app, text = "1 . Statistiques individuelles :" , command = menu_2_choix1)
    bouton_app_2 = tk.Button(app, text = "2 . Statistiques des équipes :", command = menu_2_choix2)
    bouton_app_3 = tk.Button(app, text = "Retour" , command = menu_1)
    
    titre.pack()
    bouton_app_1.pack()
    bouton_app_2.pack()
    bouton_app_3.pack()

def menu_2_choix1():

    reset_app()

    titre = tk.Label(text = "Choix des données :")
    bouton_app_1 = tk.Button(app, text = "1 . NBA 2021-22", command = lambda:[ DataFrame_NBA_saison(1), menu_3_choix1()])
    bouton_app_2 = tk.Button(app, text = "2 . NBA 2020-21", command = lambda:[ DataFrame_NBA_saison(2), menu_3_choix1()])
    bouton_app_3 = tk.Button(app, text = "3 . NBA 2019-20", command = lambda:[ DataFrame_NBA_saison(3), menu_3_choix1()])
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_2)
    

    titre.pack()
    bouton_app_1.pack()
    bouton_app_2.pack()
    bouton_app_3.pack()
    bouton_app_4.pack()

def menu_2_choix2():

    reset_app()

    titre = tk.Label(text = "Choix des données :")
    bouton_app_1 = tk.Button(app, text = "1 . NBA 2021-22", command = lambda:[ DataFrame_NBA_saison(4), menu_3_choix2()])
    bouton_app_2 = tk.Button(app, text = "2 . NBA 2020-21", command = lambda:[ DataFrame_NBA_saison(5), menu_3_choix2()])
    bouton_app_3 = tk.Button(app, text = "3 . NBA 2019-20", command = lambda:[ DataFrame_NBA_saison(6), menu_3_choix2()])
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_2)
    

    titre.pack()
    bouton_app_1.pack()
    bouton_app_2.pack()
    bouton_app_3.pack()
    bouton_app_4.pack()

def menu_3_choix1():

    reset_app()
    titre = tk.Label(text = "Choix des statistiques indiviuelles :")

    bouton_app_1 = tk.Button(app, text = "1 . Les 10 meilleurs scoreurs de la NBA :", command = menu_3_choix1_rep1)
    bouton_app_2 = tk.Button(app, text = "2 . Les 10 plus agés de la NBA :", command = menu_3_choix1_rep2)
    bouton_app_3 = tk.Button(app, text = "3 . Les 10 plus jeunes de la NBA :", command = menu_3_choix1_rep3)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_2_choix1)
    
    titre.pack()
    bouton_app_1.pack()
    bouton_app_2.pack()
    bouton_app_3.pack()
    bouton_app_4.pack()

def menu_3_choix1_rep1():

    global df

    reset_app()

    titre = tk.Label(text = "1 . Les 10 meilleurs scoreurs de la NBA :")

    Liste = fonctions.dix_joueurs_meilleurs_points_tk(df)
    
    
    listbox = tk.Listbox(app)  
    listbox_2 = tk.Listbox(app)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_3_choix1)
    
    listbox.insert(1, Liste[0][0])  
    listbox.insert(2, Liste[0][1])  
    listbox.insert(3, Liste[0][2])  
    listbox.insert(4, Liste[0][3])
    listbox.insert(5, Liste[0][4])  
    listbox.insert(6, Liste[0][5])  
    listbox.insert(7, Liste[0][6])  
    listbox.insert(8, Liste[0][7])  
    listbox.insert(9, Liste[0][8])
    listbox.insert(10, Liste[0][9])    

    listbox_2.insert(1, Liste[1][0])  
    listbox_2.insert(2, Liste[1][1])  
    listbox_2.insert(3, Liste[1][2])  
    listbox_2.insert(4, Liste[1][3])
    listbox_2.insert(5, Liste[1][4])  
    listbox_2.insert(6, Liste[1][5])  
    listbox_2.insert(7, Liste[1][6])  
    listbox_2.insert(8, Liste[1][7])  
    listbox_2.insert(9, Liste[1][8])
    listbox_2.insert(10, Liste[1][9])   
    
    titre.pack()
    listbox.pack(side = 'left')  
    listbox_2.pack(side = 'right')
    bouton_app_4.pack()
  
def menu_3_choix1_rep2():
    global df

    reset_app()

    titre = tk.Label(text = "2 . Les 10 plus agés de la NBA cette saison")

    Liste = fonctions.dix_joueurs_ages_tk(df)
    
    
    listbox = tk.Listbox(app)  
    listbox_2 = tk.Listbox(app)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_3_choix1)
    
    listbox.insert(1, Liste[0][0])  
    listbox.insert(2, Liste[0][1])  
    listbox.insert(3, Liste[0][2])  
    listbox.insert(4, Liste[0][3])
    listbox.insert(5, Liste[0][4])  
    listbox.insert(6, Liste[0][5])  
    listbox.insert(7, Liste[0][6])  
    listbox.insert(8, Liste[0][7])  
    listbox.insert(9, Liste[0][8])
    listbox.insert(10, Liste[0][9])    

    listbox_2.insert(1, Liste[1][0])  
    listbox_2.insert(2, Liste[1][1])  
    listbox_2.insert(3, Liste[1][2])  
    listbox_2.insert(4, Liste[1][3])
    listbox_2.insert(5, Liste[1][4])  
    listbox_2.insert(6, Liste[1][5])  
    listbox_2.insert(7, Liste[1][6])  
    listbox_2.insert(8, Liste[1][7])  
    listbox_2.insert(9, Liste[1][8])
    listbox_2.insert(10, Liste[1][9])   
    
    titre.pack()
    listbox.pack(side = 'left')  
    listbox_2.pack(side = 'right')
    bouton_app_4.pack()

def menu_3_choix1_rep3():
    global df

    reset_app()

    titre = tk.Label(text = "3 . Les 10 plus jeunes de la NBA :")

    Liste = fonctions.dix_joueurs_jeunes_tk(df)
    
    
    listbox = tk.Listbox(app)  
    listbox_2 = tk.Listbox(app)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_3_choix1)
    
    listbox.insert(1, Liste[0][0])  
    listbox.insert(2, Liste[0][1])  
    listbox.insert(3, Liste[0][2])  
    listbox.insert(4, Liste[0][3])
    listbox.insert(5, Liste[0][4])  
    listbox.insert(6, Liste[0][5])  
    listbox.insert(7, Liste[0][6])  
    listbox.insert(8, Liste[0][7])  
    listbox.insert(9, Liste[0][8])
    listbox.insert(10, Liste[0][9])    

    listbox_2.insert(1, Liste[1][0])  
    listbox_2.insert(2, Liste[1][1])  
    listbox_2.insert(3, Liste[1][2])  
    listbox_2.insert(4, Liste[1][3])
    listbox_2.insert(5, Liste[1][4])  
    listbox_2.insert(6, Liste[1][5])  
    listbox_2.insert(7, Liste[1][6])  
    listbox_2.insert(8, Liste[1][7])  
    listbox_2.insert(9, Liste[1][8])
    listbox_2.insert(10, Liste[1][9])   
    
    titre.pack()
    listbox.pack(side = 'left')  
    listbox_2.pack(side = 'right')
    bouton_app_4.pack()

def menu_3_choix2():

    reset_app()
    titre = tk.Label(text = "Choix des statistiques par équipe :")

    bouton_app_1 = tk.Button(app, text = "1 . Les 10 meilleurs équipes NBA : scores :", command = menu_3_choix2_rep1)
    bouton_app_2 = tk.Button(app, text = "2 . Résumés par équipe :", command = menu_3_choix2_rep2)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_2_choix2)
    
    titre.pack()
    bouton_app_1.pack()
    bouton_app_2.pack()
    bouton_app_4.pack()

def menu_3_choix2_rep1():
    global df

    reset_app()

    titre = tk.Label(text = "1 . Les 10 meilleurs équipes NBA : scores :")

    Liste = fonctions.dix_meilleurs_equipe_points_tk(df)
    
    
    listbox = tk.Listbox(app)  
    listbox_2 = tk.Listbox(app)
    bouton_app_4 = tk.Button(app, text = "Retour" , command = menu_3_choix2)
    
    listbox.insert(1, Liste[0][0])  
    listbox.insert(2, Liste[0][1])  
    listbox.insert(3, Liste[0][2])  
    listbox.insert(4, Liste[0][3])
    listbox.insert(5, Liste[0][4])  
    listbox.insert(6, Liste[0][5])  
    listbox.insert(7, Liste[0][6])  
    listbox.insert(8, Liste[0][7])  
    listbox.insert(9, Liste[0][8])
    listbox.insert(10, Liste[0][9])    

    listbox_2.insert(1, Liste[1][0])  
    listbox_2.insert(2, Liste[1][1])  
    listbox_2.insert(3, Liste[1][2])  
    listbox_2.insert(4, Liste[1][3])
    listbox_2.insert(5, Liste[1][4])  
    listbox_2.insert(6, Liste[1][5])  
    listbox_2.insert(7, Liste[1][6])  
    listbox_2.insert(8, Liste[1][7])  
    listbox_2.insert(9, Liste[1][8])
    listbox_2.insert(10, Liste[1][9])   
    
    titre.pack()
    listbox.pack(side = 'left')  
    listbox_2.pack(side = 'right')
    bouton_app_4.pack()


def menu_3_choix2_rep2():
    reset_app()
    global df

    L =[]
    for i in range(len(df['Team'])):
        L.append(df['Team'][i])
    

    Combo = ttk.Combobox(app, values = L)
    Combo.set("Choisir une équipe : ")
    Combo.pack(padx = 5, pady = 5)

    print(Combo.ttk.SelectedValue.ToString())


















app = tk.Tk()
app.title("PROJET PYTHON" )
app.minsize(height = 400, width = 800)
app.resizable()
menu_1()
df = 0
df_2 = 0


app.mainloop()



