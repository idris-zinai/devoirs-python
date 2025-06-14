print("=== Calculatrice élémentaire ===\n")

nbr_1 = int(input("Veuillez entrer le premier nombre : "))
operation = input("Veuillez entrer l'opération (+, -, *, /) : ")
nbr_2 = int(input("Veuillez entrer le deuxième nombre : "))

if operation == "+":
    resultat = nbr_1 + nbr_2
elif operation == "-":
    resultat = nbr_1 - nbr_2
elif operation == "*":
    resultat = nbr_1 * nbr_2
elif operation == "/":
    if nbr_2 != 0:
        resultat = nbr_1 / nbr_2
    else:
        print("Erreur : division par zéro.")
        resultat = None
else:
    print("Opération invalide.")
    resultat = None

# a partir d'ici j'ai ajouté un traitement spécial pour améliorer l'affichage du résultat
# en effet lors des tests par exemple quand j'ai saisi 10 divisé par 2 le programme m'a donné 5 0 comme résultat
# techniquement c'est correct puisque la division en python retourne toujours un nombre à virgule float
# même quand le résultat est en réalité un entier comme 10 / 2 qui donne 5,0
# cependant du point de vue de l'utilisateur afficher 5 au lieu de 5,0 est plus propre et plus lisible
# surtout lorsque le résultat n a pas besoin de chiffres après la virgule
# pour cela je vérifie si le résultat est égal à sa version entière resultat == int(resultat)
# si c est le cas cela signifie qu il n y a pas de partie décimale significative et j affiche donc l entier sans la virgule
# sinon j affiche normalement le résultat flottant avec les décimales

if resultat is not None:
    if resultat == int(resultat):
        print("Le résultat est :", int(resultat))
    else:
        print("Le résultat est :", resultat)
