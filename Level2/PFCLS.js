// Differents options pour le jeu
let choix_options = {
    "Pierre": { "Lezard": "C'est gagne !", "Ciseaux": "C'est gagne !", "Spock": "C'est perdu !", "Feuille": "C'est perdu !", "Pierre": "Match nul !"},
    "Feuille": { "Pierre": "C'est gagne !", "Spock": "C'est gagne !", "Ciseaux": "C'est perdu !", "Lezard": "C'est perdu !", "Feuille": "Match nul !" },
    "Ciseaux": {"Feuille": "C'est gagne !","Lezard": "C'est gagne !", "Spock": "C'est perdu !", "Pierre": "C'est perdu !", "Ciseaux": "Match nul !" },
    "Lezard": { "Spock": "C'est gagne !", "Feuille": "C'est gagne !", "Ciseaux": "C'est perdu !", "Pierre": "C'est perdu !", "Lezard": "Match nul !" },
    "Spock": { "Pierre": "C'est gagne !", "Ciseaux": "C'est gagne !", "Lezard": "C'est perdu !", "Feuille": "C'est perdu !", "Spock": "Match nul !" }
};

// Variables pour l'input
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Le joueur choisit
let choix_joueur = "";

function jouer() {
    // Recupere le choix de l'IA parmis les choix disponibles
    choix_IA = Object.keys(choix_options).at(Math.floor(Math.random()*5));
    console.log(choix_IA);
    console.log(choix_joueur);

    console.log(choix_options[choix_joueur][choix_IA]);
    rejouer();
}

function readInput() {
    rl.question('Pierre, Feuille, Ciseaux, Lezard ou Spock ? ', (input) => {
        if (Object.keys(choix_options).includes(input)) {
            choix_joueur = input;
            jouer();
        } else {
            readInput();
        }
  });
}

function rejouer() {
    rl.question('Voulez vous rejouer ? (Oui ou Non) ', (input) => {
        if (input === "Oui") {
            console.clear();
            readInput();
        } else if (input === "Non") {
            rl.close();
        } else {
            rejouer();
        }
  });
}

readInput();

