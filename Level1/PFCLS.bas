Randomize Timer
Dim choix_joueur As String
Dim choix_IA As String
Dim tableau_choix(5)
Data "Pierre","Feuille","Ciseau","Lezard","Spock"
Dim jouer As String

jouer = "Oui"

Rem Initialisation du tableau
For i = 1 To 5
    Read choix$
    tableau_choix$(i) = choix$
Next i


While jouer = "Oui"

    Rem Effacer le contenu de la fenetre
    Cls


    Rem On vide la variable jouer
    jouer = ""


    Rem L'IA choisit
    choix_IA_int = Int(Rnd * 5) + 1
    choix_IA = tableau_choix$(choix_IA_int)


    Rem Le joueur choisitDo
    Input "Pierre, Feuille, Ciseau, Lezard ou Spock ? ", choix_joueur
    While choix_joueur <> "Pierre" And choix_joueur <> "Feuille" And choix_joueur <> "Ciseau" And choix_joueur <> "Lezard" And choix_joueur <> "Spock"
        Input "Pierre, Feuille, Ciseau, Lezard ou Spock ? ", choix_joueur
    Wend

    Rem Afficher les choix et le resultat
    Print "Vous avez choisi : ", choix_joueur
    Print "L'IA a choisit : ", choix_IA
    If choix_joueur = "Feuille" Then
        If choix_IA = "Pierre" Or choix_IA = "Spock" Then
            Print "Vous avez gagne !"
        ElseIf choix_IA = "Ciseau" Or choix_IA = "Lezard" Then
            Print "Vous avez perdu !"
        Else
            Print "Match nul"
        End If
    ElseIf choix_joueur = "Pierre" Then
        If choix_IA = "Lezard" Or choix_IA = "Ciseau" Then
            Print "Vous avez gagne !"
        ElseIf choix_IA = "Spock" Or choix_IA = "Feuille" Then
            Print "Vous avez perdu !"
        Else
            Print "Match nul"
        End If
    ElseIf choix_joueur = "Lezard" Then
        If choix_IA = "Spock" Or choix_IA = "Feuille" Then
            Print "Vous avez gagne !"
        ElseIf choix_IA = "Ciseau" Or choix_IA = "Pierre" Then
            Print "Vous avez perdu !"
        Else
            Print "Match nul"
        End If
    ElseIf choix_joueur = "Spock" Then
        If choix_IA = "Ciseau" Or choix_IA = "Pierre" Then
            Print "Vous avez gagne !"
        ElseIf choix_IA = "Feuille" Or choix_IA = "Lezard" Then
            Print "Vous avez perdu !"
        Else
            Print "Match nul"
        End If
    ElseIf choix_joueur = "Ciseau" Then
        If choix_IA = "Feuille" Or choix_IA = "Lezard" Then
            Print "Vous avez gagne !"
        ElseIf choix_IA = "Spock" Or choix_IA = "Pierre" Then
            Print "Vous avez perdu !"
        Else
            Print "Match nul"
        End If
    End If

    While jouer <> "Oui" And jouer <> "Non"
        Input "Voulez vous rejouer ?", jouer
    Wend
Wend