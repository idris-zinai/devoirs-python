print("Bienvenue dans le vérificateur de mot de passe")
print("Vous avez un maximum de 10 essais pour trouver le bon mot de passe")

mot_de_passe = "az123"
essais = 0
max_essais = 10

while essais < max_essais:
    tentative = input("Entrez votre mot de passe : ")
    
    if tentative == mot_de_passe:
        print("Félicitations ! Vous avez trouvé le bon mot de passe")
        break
    else:
        essais += 1
        print("Mot de passe incorrect il vous reste", max_essais - essais, "essai(s)")

if essais == max_essais:
    print("Vous avez épuisé tous vos essais accès refusé")
