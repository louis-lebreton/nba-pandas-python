import pandas as pd 


"""
Les fonctions :

"""

def verif_choix(variable, x):
    if x == 1 :
        while variable != "1" :
            variable = input()
        return int(variable)
    elif x == 2 :
        while variable != "1" and variable != "2" :
            variable = input()
        return int(variable)
    elif x == 3 :
        while variable != "1" and variable != "2" and variable != "3" :
            variable = input()
        return int(variable)
    elif x == 4 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" :
             variable = input()
        return int(variable)
    elif x == 5 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" and variable != "5":
             variable = input()
        return int(variable)
    elif x == 6 :
        while variable != "1" and variable != "2" and variable != "3" and variable != "4" and variable != "5" and variable != "6":
             variable = input()
        return int(variable)

def marge():
    print()
    print()
    print("#####################################################################################")
    print("#####################################################################################")
    print()
    print()
    return

def dix_joueurs_meilleurs_points(data):
    df = data
    df["PTS"] = pd.to_numeric(df["PTS"])
    df = df.sort_values(by = 'PTS', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['PTS'][i])
    return

def dix_joueurs_ages(data):
    df = data  
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['Age'][i])
    return

def dix_joueurs_jeunes(data):
    df = data 
    df["Age"] = pd.to_numeric(df["Age"])
    df = df.sort_values(by = "Age", ascending = True)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Player'][i], df['Age'][i])
    return

def choix_saison():
    marge()
    print("1 . NBA 2021-22")
    print("2 . NBA 2020-21")
    print("3 . NBA 2019-20")
    marge()
    choix_saison = input("")
    #Verification de saisi
    verif_choix(choix_saison, 3)
    choix_saison = int(choix_saison)
    return choix_saison


def dix_meilleurs_équipes(data):
    df = data
    df["W/L%"] = pd.to_numeric(df["W/L%"])
    df = df.sort_values(by = 'W/L%', ascending = False)
    df = df.reset_index()
    df = df.iloc[:-len(df)+10]
    for i in range(10):
        print(df['Team'][i], df['W/L%'][i])
    return




    