import tkinter as tk 
from tkinter import ttk
import pandas
from PIL import ImageTk, Image


import fonctions
import WebScraping







class Application():
    def __init__(self, root):
        # Ajouter les titres :
        
        self.creer_titres = ttk.Label(root, text = " Projet tutoré de 2ème année \n Analyse des données NBA \n Parmentier ; Makké ; Lebreton ; Messina")
        self.creer_bouton_1 = tk.Button(root, text = "Accéder aux analyses", command = self.menu_2) 
        self.creer_bouton_2 = tk.Button(root, text = "Quitter" , command = root.quit)
        #logo = tk.PhotoImage(file = 'STID.jpg') 
        #self.logo_1 = tk.Button(root, image = logo)

       
        self.creer_titres.pack(expand = 1)
        self.creer_bouton_1.pack()
        self.creer_bouton_2.pack(expand = 1)
        #self.logo_1.pack()

    
    def delete_widget(self):
        for widget in root.winfo_children():
            widget.destroy()

    
    def menu_2(self):
        self.delete_widget()

        # Créer un objet photoimage pour utiliser l'image
        # on créé une image "crash" car tkinter ne veut pas afficher la première image
        crash = tk.PhotoImage(file = 'logos_nba/ATL_2022.jpg')
        ATL = tk.PhotoImage(file = 'logos_nba/ATL_2022.jpg')
        BOS = tk.PhotoImage(file = 'logos_nba/BOS_2022.jpg') 
        BRK = tk.PhotoImage(file = 'logos_nba/BRK_2022.jpg') 
        CHI = tk.PhotoImage(file = 'logos_nba/CHI_2022.jpg') 
        CHO = tk.PhotoImage(file = 'logos_nba/CHO_2022.jpg') 
        CLE = tk.PhotoImage(file = 'logos_nba/CLE_2022.jpg') 
        DAL = tk.PhotoImage(file = 'logos_nba/DAL_2022.jpg') 
        DEN = tk.PhotoImage(file = 'logos_nba/DEN_2022.jpg') 
        DET = tk.PhotoImage(file = 'logos_nba/DET_2022.jpg') 
        GSW = tk.PhotoImage(file = 'logos_nba/GSW_2022.jpg') 
        HOU = tk.PhotoImage(file = 'logos_nba/HOU_2022.jpg') 
        IND = tk.PhotoImage(file = 'logos_nba/IND_2022.jpg') 
        LAC = tk.PhotoImage(file = 'logos_nba/LAC_2022.jpg') 
        LAL = tk.PhotoImage(file = 'logos_nba/LAL_2022.jpg') 
        MEM = tk.PhotoImage(file = 'logos_nba/MEM_2022.jpg') 
        MIA = tk.PhotoImage(file = 'logos_nba/MIA_2022.jpg') 
        MIL = tk.PhotoImage(file = 'logos_nba/MIL_2022.jpg') 
        MIN = tk.PhotoImage(file = 'logos_nba/MIN_2022.jpg') 
        NOP = tk.PhotoImage(file = 'logos_nba/NOP_2022.jpg') 
        NYK = tk.PhotoImage(file = 'logos_nba/NYK_2022.jpg') 
        OKC = tk.PhotoImage(file = 'logos_nba/OKC_2022.jpg') 
        ORL = tk.PhotoImage(file = 'logos_nba/ORL_2022.jpg') 
        PHI = tk.PhotoImage(file = 'logos_nba/PHI_2022.jpg') 
        PHO = tk.PhotoImage(file = 'logos_nba/PHO_2022.jpg') 
        POR = tk.PhotoImage(file = 'logos_nba/POR_2022.jpg') 
        SAC = tk.PhotoImage(file = 'logos_nba/SAC_2022.jpg') 
        SAS = tk.PhotoImage(file = 'logos_nba/SAS_2022.jpg') 
        TOR = tk.PhotoImage(file = 'logos_nba/TOR_2022.jpg') 
        UTA = tk.PhotoImage(file = 'logos_nba/UTA_2022.jpg') 
        WAS = tk.PhotoImage(file = 'logos_nba/WAS_2022.jpg')


        # Ajouter l'image dans le bouton
        self.bouton_0 = tk.Button(root, image = crash, command = lambda: self.menu_3('ATL'))
        self.bouton_0.grid(row = 0, column = 0)
        self.bouton_1 = tk.Button(root, image = ATL, command = lambda: self.menu_3('ATL'))
        self.bouton_1.grid(row = 0, column = 1)
        self.bouton_2 = tk.Button(root, image = BOS, command = lambda: self.menu_3('BOS'))
        self.bouton_2.grid(row = 0, column = 2)
        self.bouton_3 = tk.Button(root, image = BRK, command = lambda: self.menu_3('BRK'))
        self.bouton_3.grid(row = 0, column = 3)
        self.bouton_4 = tk.Button(root, image = CHI, command = lambda: self.menu_3('CHI'))
        self.bouton_4.grid(row = 0, column = 4)
        self.bouton_5 = tk.Button(root, image = CHO, command = lambda: self.menu_3('CHO'))
        self.bouton_5.grid(row = 0, column = 5)
        self.bouton_6 = tk.Button(root, image = CLE, command = lambda: self.menu_3('CLE'))
        self.bouton_6.grid(row = 0, column = 6)
        self.bouton_7 = tk.Button(root, image = DAL, command = lambda: self.menu_3('DAL'))
        self.bouton_7.grid(row = 0, column = 7)
        self.bouton_8 = tk.Button(root, image = DEN, command = lambda: self.menu_3('DEN'))
        self.bouton_8.grid(row = 1, column = 0)
        self.bouton_9 = tk.Button(root, image = DET, command = lambda: self.menu_3('DET'))
        self.bouton_9.grid(row = 1, column = 1)
        self.bouton_10 = tk.Button(root, image = GSW, command = lambda: self.menu_3('GSW'))
        self.bouton_10.grid(row = 1, column = 2)
        self.bouton_11 = tk.Button(root, image = HOU, command = lambda: self.menu_3('HOU'))
        self.bouton_11.grid(row = 1, column = 3)
        self.bouton_12 = tk.Button(root, image = IND, command = lambda: self.menu_3('IND'))
        self.bouton_12.grid(row = 1, column = 4)
        self.bouton_13 = tk.Button(root, image = LAC, command = lambda: self.menu_3('LAC'))
        self.bouton_13.grid(row = 1, column = 5)
        self.bouton_14 = tk.Button(root, image = LAL, command = lambda: self.menu_3('LAL'))
        self.bouton_14.grid(row = 1, column = 6)
        self.bouton_15 = tk.Button(root, image = MEM, command = lambda: self.menu_3('MEM'))
        self.bouton_15.grid(row = 1, column = 7)
        self.bouton_16 = tk.Button(root, image = MIA, command = lambda: self.menu_3('MIA'))
        self.bouton_16.grid(row = 2, column = 0)
        self.bouton_17 = tk.Button(root, image = MIL, command = lambda: self.menu_3('MIL'))
        self.bouton_17.grid(row = 2, column = 1)
        self.bouton_18 = tk.Button(root, image = MIN, command = lambda: self.menu_3('MIN'))
        self.bouton_18.grid(row = 2, column = 2)
        self.bouton_19 = tk.Button(root, image = NOP, command = lambda: self.menu_3('NOP'))
        self.bouton_19.grid(row = 2, column = 3)
        self.bouton_20 = tk.Button(root, image = NYK, command = lambda: self.menu_3('NYK'))
        self.bouton_20.grid(row = 2, column = 4)
        self.bouton_21 = tk.Button(root, image = OKC, command = lambda: self.menu_3('OKC'))
        self.bouton_21.grid(row = 2, column = 5)
        self.bouton_22 = tk.Button(root, image = ORL, command = lambda: self.menu_3('ORL'))
        self.bouton_22.grid(row = 2, column = 6)
        self.bouton_23 = tk.Button(root, image = PHI, command = lambda: self.menu_3('PHI'))
        self.bouton_23.grid(row = 2, column = 7)
        self.bouton_24 = tk.Button(root, image = PHO, command = lambda: self.menu_3('PHO'))
        self.bouton_24.grid(row = 3, column = 0)
        self.bouton_25 = tk.Button(root, image = POR, command = lambda: self.menu_3('POR'))
        self.bouton_25.grid(row = 3, column = 1)
        self.bouton_26 = tk.Button(root, image = SAC, command = lambda: self.menu_3('SAC'))
        self.bouton_26.grid(row = 3, column = 2)
        self.bouton_27 = tk.Button(root, image = SAS, command = lambda: self.menu_3('SAS'))
        self.bouton_27.grid(row = 3, column = 3)
        self.bouton_28 = tk.Button(root, image = TOR, command = lambda: self.menu_3('TOR'))
        self.bouton_28.grid(row = 3, column = 4)
        self.bouton_29 = tk.Button(root, image = UTA, command = lambda: self.menu_3('UTA'))
        self.bouton_29.grid(row = 3, column = 5)
        self.bouton_30 = tk.Button(root, image = WAS, command = lambda: self.menu_3('WAS'))
        self.bouton_30.grid(row = 3, column = 6)




        self.bouton_0.pack()
        self.bouton_1.pack()
        self.bouton_2.pack()
        self.bouton_3.pack()
        self.bouton_4.pack()
        self.bouton_5.pack()
        self.bouton_6.pack()
        self.bouton_7.pack()
        self.bouton_8.pack()
        self.bouton_9.pack()
        self.bouton_10.pack()
        self.bouton_11.pack()
        self.bouton_12.pack()
        self.bouton_13.pack()
        self.bouton_14.pack()
        self.bouton_15.pack()
        self.bouton_16.pack()
        self.bouton_17.pack()
        self.bouton_18.pack()
        self.bouton_19.pack()
        self.bouton_20.pack()
        self.bouton_21.pack()
        self.bouton_22.pack()
        self.bouton_23.pack()
        self.bouton_24.pack()
        self.bouton_25.pack()
        self.bouton_26.pack()
        self.bouton_27.pack()
        self.bouton_28.pack()
        self.bouton_29.pack()
        self.bouton_30.pack()


    def menu_3(self, equipe):

        self.delete_widget()

        ##################### choix de team
        self.team = equipe 
        ##################### 
        #chemin du fichier
        chemin="images_joueurs_et_csv_equipes/teams/"+self.team+".csv"
        # importation du .csv en dataframe
        self.df = pandas.read_csv(chemin,index_col=0,header=None)
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
        


    
        #listechemin[i]= chemin du fichier du ième joueur
        #création de deux crashs car Tkinter n'affiche pas les deux premières images
        self.crash = ImageTk.PhotoImage(Image.open(listechemin[0]))    
        self.a = ImageTk.PhotoImage(Image.open(listechemin[0]))  
        self.b = ImageTk.PhotoImage(Image.open(listechemin[1]))
        self.c = ImageTk.PhotoImage(Image.open(listechemin[2]))
        self.d = ImageTk.PhotoImage(Image.open(listechemin[3]))
        self.e = ImageTk.PhotoImage(Image.open(listechemin[4]))
        self.f = ImageTk.PhotoImage(Image.open(listechemin[5]))
        self.g = ImageTk.PhotoImage(Image.open(listechemin[6]))
        self.h = ImageTk.PhotoImage(Image.open(listechemin[7]))
        self.i = ImageTk.PhotoImage(Image.open(listechemin[8]))
        self.j = ImageTk.PhotoImage(Image.open(listechemin[9]))
        self.k = ImageTk.PhotoImage(Image.open(listechemin[10])) 
        self.l = ImageTk.PhotoImage(Image.open(listechemin[11]))
        self.m = ImageTk.PhotoImage(Image.open(listechemin[12]))
        self.n = ImageTk.PhotoImage(Image.open(listechemin[13]))
        self.o = ImageTk.PhotoImage(Image.open(listechemin[14])) 
        self.p = ImageTk.PhotoImage(Image.open(listechemin[15]))

        self.q = ImageTk.PhotoImage(Image.open(listechemin[16]))
        self.r = ImageTk.PhotoImage(Image.open(listechemin[17]))
        self.s = ImageTk.PhotoImage(Image.open(listechemin[18]))
        



        # Ajouter l'image dans le bouton 
        self.bouton_crash = tk.Button(root, image = self.crash)
        self.bouton_crash.grid(row = 0, column = 0)
        self.bouton_1 = tk.Button(root, image = self.a,command = lambda: self.menu_4(str(self.liste[0][0])))
        self.bouton_1.grid(row = 0, column = 1)
        self.bouton_2 = tk.Button(root, image = self.b,command = lambda: self.menu_4(str(self.liste[1][0])))
        self.bouton_2.grid(row = 0, column = 2)
        self.bouton_3 = tk.Button(root, image = self.c,command = lambda: self.menu_4(str(self.liste[2][0])))
        self.bouton_3.grid(row = 0, column = 3)
        self.bouton_4 = tk.Button(root, image = self.d,command = lambda: self.menu_4(str(self.liste[3][0])))
        self.bouton_4.grid(row = 0, column = 4)
        self.bouton_5 = tk.Button(root, image = self.e,command = lambda: self.menu_4(str(self.liste[4][0])))
        self.bouton_5.grid(row = 1, column = 0)
        self.bouton_6 = tk.Button(root, image = self.f,command = lambda: self.menu_4(str(self.liste[5][0])))
        self.bouton_6.grid(row = 1, column = 1)
        self.bouton_7 = tk.Button(root, image = self.g,command = lambda: self.menu_4(str(self.liste[6][0])))
        self.bouton_7.grid(row = 1, column = 2)
        self.bouton_8 = tk.Button(root, image = self.h,command = lambda: self.menu_4(str(self.liste[7][0])))
        self.bouton_8.grid(row = 1, column = 3)
        self.bouton_9 = tk.Button(root, image = self.i,command = lambda: self.menu_4(str(self.liste[8][0])))
        self.bouton_9.grid(row = 1, column = 4)
        self.bouton_10 = tk.Button(root, image = self.j,command = lambda: self.menu_4(str(self.liste[9][0])))
        self.bouton_10.grid(row = 2, column =0)
        self.bouton_11 = tk.Button(root, image = self.k,command = lambda: self.menu_4(str(self.liste[10][0])))
        self.bouton_11.grid(row = 2, column = 1)
        self.bouton_12 = tk.Button(root, image = self.l,command = lambda: self.menu_4(str(self.liste[11][0])))
        self.bouton_12.grid(row = 2, column = 2)
        self.bouton_13 = tk.Button(root, image = self.m,command = lambda: self.menu_4(str(self.liste[12][0])))
        self.bouton_13.grid(row = 2, column = 3)
        self.bouton_14 = tk.Button(root, image = self.n,command = lambda: self.menu_4(str(self.liste[13][0])))
        self.bouton_14.grid(row = 2, column = 4)
        self.bouton_15 = tk.Button(root, image = self.o,command = lambda: self.menu_4(str(self.liste[14][0])))
        self.bouton_15.grid(row = 3, column = 0)
        self.bouton_16 = tk.Button(root, image = self.p,command = lambda: self.menu_4(str(self.liste[15][0])))
        self.bouton_16.grid(row = 3, column = 1)
        self.bouton_17 = tk.Button(root, image = self.q,command = lambda: self.menu_4(str(self.liste[16][0])))
        self.bouton_17.grid(row = 3, column = 2)
        self.bouton_18 = tk.Button(root, image = self.r,command = lambda: self.menu_4(str(self.liste[17][0])))
        self.bouton_18.grid(row = 3, column = 3)
        self.bouton_19 = tk.Button(root, image = self.s,command = lambda: self.menu_4(str(self.liste[18][0])))
        self.bouton_19.grid(row = 3, column = 4)
        
        

        self.bouton_crash.pack()
        self.bouton_1.pack()
        self.bouton_2.pack()
        self.bouton_3.pack()
        self.bouton_4.pack()
        self.bouton_5.pack()
        self.bouton_6.pack()
        self.bouton_7.pack()
        self.bouton_8.pack()
        self.bouton_9.pack()
        self.bouton_10.pack()
        self.bouton_11.pack()
        self.bouton_12.pack()
        self.bouton_13.pack()
        self.bouton_14.pack()
        self.bouton_15.pack()
        self.bouton_16.pack()
        self.bouton_17.pack()
        self.bouton_18.pack()
        self.bouton_19.pack()
        
        
        
        
    def menu_4(self, joueur):

        self.delete_widget()

        ##################### choix du joueur
        self.player = joueur 
        ##################### 
        #récupération nom du joueur
        cheminjoueur="images_joueurs_et_csv_equipes/teams/"+self.team+".csv"
        self.df = pandas.read_csv(cheminjoueur,header=None)
        self.liste2 = self.df.values.tolist()
        i=0
        # récupréation du rang du joueur sur le tableau .csv team
        while self.liste2[i][1] != joueur:
            i=i+1
        
        
        
        
        #chemin du fichier pour le .csv
        chemin="sommaires_players/"+self.player+".csv"
        #conversion en dataframe
        self.df = pandas.read_csv(chemin,index_col=0,header=None)
        self.liste = self.df.values.tolist()
        
        #création et affichage du tableau
        self.table_frame = tk.Frame(root)
        self.table_frame.pack()

        self.my_table = ttk.Treeview(self.table_frame)

        self.my_table['columns'] = ('0', '1', '2')

        self.my_table.column("#0", width=0,  stretch=tk.NO)
        self.my_table.column("0", width=222)
        self.my_table.column("1",anchor=tk.CENTER,width=80)
        self.my_table.column("2",anchor=tk.CENTER,width=80)


        self.my_table.heading("#0",text="",anchor=tk.CENTER)
        #ici on réutilise le rang du joueur i sur le tableau scv teams pour obtenir son nom
        # en haut à gauche du tableau du sommaire
        self.my_table.heading("0",text=self.liste2[i][0],anchor=tk.CENTER)
        self.my_table.heading("1",text="2021-2022",anchor=tk.CENTER)
        self.my_table.heading("2",text="Carrière",anchor=tk.CENTER)


        self.my_table.insert(parent='',index='end',iid=0,text='',
        values=('Matchs joués',self.liste[1][0],self.liste[1][1]))
        self.my_table.insert(parent='',index='end',iid=1,text='',
        values=('Points',self.liste[2][0],self.liste[2][1]))
        self.my_table.insert(parent='',index='end',iid=2,text='',
        values=('Rebonds',self.liste[3][0],self.liste[3][1]))
        self.my_table.insert(parent='',index='end',iid=3,text='',
        values=('Passes décisives',self.liste[4][0],self.liste[4][1]))
        self.my_table.insert(parent='',index='end',iid=4,text='',
        values=('% de shoots marqués',self.liste[5][0],self.liste[5][1]))
        self.my_table.insert(parent='',index='end',iid=5,text='',
        values=('% de shoots marqués à 3 points',self.liste[6][0],self.liste[6][1]))
        self.my_table.insert(parent='',index='end',iid=6,text='',
        values=('% de lancers francs marqués',self.liste[7][0],self.liste[7][1]))
        self.my_table.insert(parent='',index='end',iid=7,text='',
        values=('% de shoots marqués ajusté aux 3 points',self.liste[8][0],self.liste[8][1]))
        self.my_table.insert(parent='',index='end',iid=8,text='',
        values=("Note d'efficience",self.liste[9][0],self.liste[9][1]))
        self.my_table.insert(parent='',index='end',iid=9,text='',
        values=('Victoires par sa contribution',self.liste[10][0],self.liste[10][1]))
        
        self.my_table.pack()
        
        
        
        
        
        #chemin du fichier pour le texte 
        chemin="ficheindiv_players/"+self.player+".txt"
        
        #affichage du texte 
        self.fichier = open(chemin, "r",encoding='utf-8')
        self.content = self.fichier.read()
        self.fichier.close()
        
        self.texteLabel = tk.Label(root, text = self.content)
        self.texteLabel.pack()
        
        
        

        
        

        

        


def test():
    print("yo")


  

root = tk.Tk()
app = Application(root)
root.minsize(height = 400, width = 400)
root.resizable(width=False, height=False)
root.mainloop()