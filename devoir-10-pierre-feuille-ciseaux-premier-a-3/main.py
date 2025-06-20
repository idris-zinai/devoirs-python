print("Ceci est le jeu pierre feuille ciseaux Le gagnant est le premier à 3 victoires !")
Joueur1gagne = 0
Joueur2gagne = 0
while Joueur1gagne < 3 and Joueur2gagne < 3:
    joueur1 = input("Joueur 1 faites votre choix (pierre feuille ou ciseaux) : ")
    joueur2 = input("Joueur 2 faites votre choix (pierre feuille ou ciseaux) : ")

    if joueur1 == joueur2:
        print("Égalité !")
    elif (joueur1 == "pierre" and joueur2 == "ciseaux") \
        or (joueur1 == "feuille" and joueur2 == "pierre") \
        or (joueur1 == "ciseaux" and joueur2 == "feuille"):
        print("Joueur 1 gagne la manche !")
        Joueur1gagne += 1
    else:
        print("Joueur 2 gagne la manche !")
        Joueur2gagne += 1
if Joueur1gagne == 3:
    print("Le joueur 1 a gagné la partie !")
else:
    print("Le joueur 2 a gagné la partie !")
print("Score final : Joueur 1 =", Joueur1gagne, "| Joueur 2 =", Joueur2gagne)
