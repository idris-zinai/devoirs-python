print("ceci est le jeu pierre feuille ciseaux bienvenu")
joueur1 = input("Joueur 1 faites votre choix pierre feuille ou ciseaux: ")
joueur2 = input("Au tour du Joueur 2 faites votre choix pierre feuille ou ciseaux : ")
if joueur1 == joueur2:
    print("Égalité !")
elif (joueur1 == "pierre" and joueur2 == "ciseaux") \
    or (joueur1 == "feuille" and joueur2 == "pierre") \
    or (joueur1 == "ciseaux" and joueur2 == "feuille"):
    print("Joueur 1 gagne !")
else:
    print("Joueur 2 gagne !")
