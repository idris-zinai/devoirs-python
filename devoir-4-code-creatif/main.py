print("Bienvenue dans le site de notre auto-école")

age = int(input("Quel est votre âge ? :"))

if age < 18:
    print("Vous n'êtes pas apte à passer votre permis, nous sommes désolés.")
else:
    print("Vous êtes apte à passer votre permis.\n")

    sexe = input("Sexe (M/F) : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    date_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
    ville = input("Ville de résidence : ")
    num_tel = input("Numéro de téléphone : ")
    email = input("Email : ")
    print("\nMerci pour votre visite. Nous avons enregistré vos informations et nous vous contacterons dès que possible.")
