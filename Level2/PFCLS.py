import random
import os

## Differents options pour le jeu
choix_options = {
    "Pierre": {
        "Lezard": "C'est gagne !",
        "Ciseaux": "C'est gagne !",
        "Spock": "C'est perdu !",
        "Feuille": "C'est perdu !",
        "Pierre": "Match nul !"
    },
    "Feuille": {
        "Pierre": "C'est gagne !",
        "Spock": "C'est gagne !",
        "Ciseaux": "C'est perdu !",
        "Lezard": "C'est perdu !",
        "Feuille": "Match nul !"
    },
    "Ciseaux": {
        "Feuille": "C'est gagne !",
        "Lezard": "C'est gagne !",
        "Spock": "C'est perdu !",
        "Pierre": "C'est perdu !",
        "Ciseaux": "Match nul !"
    },
    "Lezard": {
        "Spock": "C'est gagne !",
        "Feuille": "C'est gagne !",
        "Ciseaux": "C'est perdu !",
        "Pierre": "C'est perdu !",
        "Lezard": "Match nul !"
    },
    "Spock": {
        "Pierre": "C'est gagne !",
        "Ciseaux": "C'est gagne !",
        "Lezard": "C'est perdu !",
        "Feuille": "C'est perdu !",
        "Spock": "Match nul !"
    }
}

jouer = "Oui"

while jouer == "Oui":
    ## Efaccer le contenu de la console
    os.system('cls' if os.name == 'nt' else 'clear')

    ## Choix du joueur
    choix_joueur = input("Pierre, Feuille, Ciseaux, Lezard ou Spock ? ")
    while choix_joueur not in choix_options:
        choix_joueur = input("Pierre, Feuille, Ciseau, Lezard ou Spock ? ")   


    ## Choix de l'ia
    choix_IA = list(choix_options.keys())[random.randint(0,4)]


    ## Affichage des choix
    print ("Choix du joueur : " + choix_joueur)
    print ("Choix de l'IA : " + choix_IA)

    ## Gestion de match
    print(choix_options[choix_joueur][choix_IA])

    jouer = input("Voulez-vous rejouer (Oui ou Non) ? ")
    while jouer != "Oui" and jouer != "Non" :
        jouer = input("Voulez-vous rejouer (Oui ou Non) ? ")