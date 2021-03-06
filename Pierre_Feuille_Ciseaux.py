from random import choice
recommencer = "o"
while (recommencer == "o"):
    print("Ceci est un jeu tout simple :) ")
    print("Mais je pense que le robot aura un winrate superieur au tiens :D ")
    print("Parce que c'est moi qui l'ai crÃ©e :') ")
    print("Je vous expllique vous devrez choisir un chiffre entre 1 et 3  ")
    print("1 = pierre, 2 = feuille, 3= ciseaux")
    nbpartie = int(input("Combien de partie tu veux faire ? "))
    partie = 0
    winrate = 0
    userwin = 0
    possibilites = [1,2,2,3] # 2 Feuilles car proba Pierre pour User est  + elever
    listeChoixUser = [0,4,0] # liste historique des choix du User, 0,4,0 parce que plus tard nous regardons les deux dernier chiffre de la liste, 3 vlr car la premiere valeur dune liste = 0

    for i in range (nbpartie):

        ChoixRobot = choice(possibilites) # choisi un nombre aleatoire dans une liste
        # on a choisi un chiffre pour le robot mais si le user a deja jouer 2 fois le meme ont force le robot a choisir le chiffre prÃ©cÃ©dent en partant du principe  quil ne jouera pas une 3eme fois le meme
        if (listeChoixUser[-1] == listeChoixUser[-2]): # Si les 2 derniere valeur de lhistorique du User sont les meme alors :
            a = (listeChoixUser[-1]) - 1 # On recupere la derniere valeur de cettte liste et on prend le signe precedent grace au - 1
            if (a == 0): # En fessant -1 si "a"(la derniere valeur du User) est = 1 alors nous allons se retrouver avec un 0 alors quon a besoin du 3
                a = 3
            ChoixRobot = a # On impose au robot de prendre le signe precedant le signe que le user a repeter 2 fois car on estime quil ne le refera pas alors le robot fera une egaliter ou une victoire

        possibilites = [1,2,3] # RÃ©initialise la liste au 2eme tour car ChoixRobot deja fais
        ChoixUser = int(input("selectionner :  "))
    #1 bat 3
    #2 bat 1
    #3 bat 2

    #EgalitÃ©
        if (ChoixRobot == 1 and ChoixUser == 1):
            print("EgalitÃ© :v ")
            partie = partie + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Pierre")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Pierre")
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif (ChoixRobot == 2 and ChoixUser == 2):
            print("EgalitÃ© :v ")
            partie = partie + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Feuille")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Feuille")
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif (ChoixRobot == 3 and ChoixUser == 3):
            print("EgalitÃ© :v ")
            partie = partie + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Ciseaux")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Ciseaux")
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

    #DefaiteRobot
        elif (ChoixRobot == 1 and ChoixUser == 2):
            print("Oh non tu as battu le robot :'( ")
            partie = partie +  1
            userwin = userwin + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Feuille")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Pierre")
            possibilites.append(3) # Ajoute le choix du User a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif  (ChoixRobot == 2 and ChoixUser == 3):
            print("Oh non tu as battu le robot  :'( ")
            partie = partie + 1
            userwin = userwin + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Ciseaux")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Feuille")
            possibilites.append(1) # Ajoute le choix du User a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif (ChoixRobot == 3 and ChoixUser == 1):
            print("Oh  non tu as battu le robot :'( ")
            partie = partie + 1
            userwin = userwin + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Pierre")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Ciseaux")
            possibilites.append(2) # Ajoute le choix du User a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

    #Victoire
        elif (ChoixRobot == 1 and ChoixUser == 3):
            print("Ahah le robot t'as battu :D ")
            partie = partie +  1
            print("Ton choix a Ã©tÃ© : ")
            print("Ciseaux")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Pierre")
            possibilites.append(2) # Ajoute le choix du Robot a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif  (ChoixRobot == 2 and ChoixUser == 1):
            print("Ahah le robot t'as battu :D ")
            partie = partie + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Pierre")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Feuille")
            possibilites.append(3) # Ajoute le choix du Robot a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

        elif (ChoixRobot == 3 and ChoixUser == 2):
            print("Ahah le robot t'as battu :D ")
            partie = partie + 1
            print("Ton choix a Ã©tÃ© : ")
            print("Feuille")
            print("Le choix du robot a Ã©tÃ© : "  )
            print("Ciseaux")
            possibilites.append(1) # Ajoute le choix du Robot a la liste pour avoir + de chance de tomber au prochain tour
            listeChoixUser.append(ChoixUser) # Permet de rÃ©cuperer les choix du User et l'incrire dans une liste pour voir plus tard si il fais 2 fois la meme chose

    print("Tu as fait " , nbpartie , "partie")
    winrate = (userwin/nbpartie*100)
    print("ton winrate est de : ", round(winrate,2),"%")
    if (winrate <50):
        print("J'ai gagner !! :p")
    else:
        print("Tu as gagner, coup de chance.. :c")
    recommencer = str(input("Voulez vous continuer (o/n)"))
    if(recommencer != "o" or recommencer != "n"):
        print("Erreur")
