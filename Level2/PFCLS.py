import random
import os

## Differents options pour le jeu
choix_options = ["Pierre", "Feuille", "Ciseau", "Lezard", "Spock"]

jouer = "Oui"

while jouer == "Oui":
    ## Efaccer le contenu de la console
    os.system('cls' if os.name == 'nt' else 'clear')

    ## Choix du joueur
    choix_joueur = input("Pierre, Feuille, Ciseau, Lezard ou Spock ? ")
    while choix_joueur not in choix_options:
        choix_joueur = input("Pierre, Feuille, Ciseau, Lezard ou Spock ? ")   


    ## Choix de l'ia
    choix_IA = choix_options[random.randint(0,4)]


    ## Affichage des choix
    print ("Choix du joueur : " + choix_joueur)
    print ("Choix de l'IA : " + choix_IA)

    ## Gestion de match
    if choix_joueur == "Pierre" :
        if choix_IA == "Lezard" or choix_IA == "Ciseau" :
            print ("Vous avez gagne !")
        elif choix_IA == "Spock" or choix_IA == "Feuille" :
            print("Vous avez perdu !")
        else :
            print ("Match nul !")
    elif choix_joueur == "Lezard" :
        if choix_IA == "Spock" or choix_IA == "Feuille" :
            print ("Vous avez gagne !")
        elif choix_IA == "Pierre" or choix_IA == "Ciseau" :
            print("Vous avez perdu !")
        else :
            print ("Match nul !")
    elif choix_joueur == "Spock" :
        if choix_IA == "Ciseau" or choix_IA == "Pierre" :
            print ("Vous avez gagne !")
        elif choix_IA == "Lezard" or choix_IA == "Feuille" :
            print("Vous avez perdu !")
        else :
            print ("Match nul !")
    elif choix_joueur == "Ciseau" :
        if choix_IA == "Feuile" or choix_IA == "Lezard" :
            print ("Vous avez gagne !")
        elif choix_IA == "Spock" or choix_IA == "Pierre" :
            print("Vous avez perdu !")
        else :
            print ("Match nul !")
    else :
        if choix_IA == "Pierre" or choix_IA == "Spock" :
            print ("Vous avez gagne !")
        elif choix_IA == "Ciseau" or choix_IA == "Lezard" :
            print("Vous avez perdu !")
        else :
            print ("Match nul !")

    jouer = input("Voulez-vous rejouer (Oui ou Non) ? ")
    while jouer != "Oui" and jouer != "Non" :
        jouer = input("Voulez-vous rejouer (Oui ou Non) ? ")