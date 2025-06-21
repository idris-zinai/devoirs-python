def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

nombre = int(input("Entrez un nombre : "))
if est_premier(nombre):
    print("C'est un nombre premier.")
else:
    print("Ce n'est pas un nombre premier.")
