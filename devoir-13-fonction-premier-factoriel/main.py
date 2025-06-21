import math

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorielle(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

def somme_premiers_racine_factorielle(n):
    fact = factorielle(n)
    limite = int(math.sqrt(fact))
    somme = 0
    for i in range(2, limite + 1):
        if est_premier(i):
            somme += i
    return somme

while True:
    n = int(input("Entrez un nombre premier pour continuer : "))
    if est_premier(n):
        break
    else:
        print("Ce n'est pas un nombre premier. Essayez encore.")

print("La factorielle de", n, "est :", factorielle(n))
print("La somme des nombres premiers entre 0 et √(n!) est :", somme_premiers_racine_factorielle(n))
print("Et oui,", n, "est bien un nombre premier.")
