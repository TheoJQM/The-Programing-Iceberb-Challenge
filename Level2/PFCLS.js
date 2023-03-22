

// Differents options pour le jeu
let choix_options = {
    "Pierre": { "Lezard": "C'est gagne !", "Ciseaux": "C'est gagne !", "Spock": "C'est perdu !", "Feuille": "C'est perdu !", "Pierre": "Match nul !"},
    "Feuille": { "Pierre": "C'est gagne !", "Spock": "C'est gagne !", "Ciseaux": "C'est perdu !", "Lezard": "C'est perdu !", "Feuille": "Match nul !" },
    "Ciseaux": {"Feuille": "C'est gagne !","Lezard": "C'est gagne !", "Spock": "C'est perdu !", "Pierre": "C'est perdu !", "Ciseaux": "Match nul !" },
    "Lezard": { "Spock": "C'est gagne !", "Feuille": "C'est gagne !", "Ciseaux": "C'est perdu !", "Pierre": "C'est perdu !", "Lezard": "Match nul !" },
    "Spock": { "Pierre": "C'est gagne !", "Ciseaux": "C'est gagne !", "Lezard": "C'est perdu !", "Feuille": "C'est perdu !", "Spock": "Match nul !" }
};

// Varible pour rejouer
let jouer = "oui";

// Fonction pour que le joueur ne choississe que l'un des cinq choix proposés
function choisir() {
    readline.question('Pierre, Feuille, Ciseaux, Lezard ou Spock ?', (entree) => {
        if(entree !== 'Pierre' && entree !== 'Feuille' && entree !== 'Ciseaux' && entree !== 'Lezard' && entree !== 'Spock') {
            choisir();
        } else {
            choix_joueur = entree;
            readline.close();
        }
    });
}


// Recupere le choix du joueur parmis les choix disponibles
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let choix_joueur ="";
choisir();



// Recupere le choix de l'IA parmis les choix disponibles
choix_IA = Object.keys(choix_options).at(Math.floor(Math.random()*5));
console.log(choix_IA);
