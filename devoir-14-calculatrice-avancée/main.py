import math

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def puissance(a, b):
    try:
        return a ** b
    except:
        return "Erreur : puissance invalide"


def modulo(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a % b

def racine_carree(a):
    if a < 0:
        return "Erreur : racine carrée d’un nombre négatif"
    return math.sqrt(a)

def calculatrice_avancee(a, b, operation):
    if operation == '+':
        return addition(a, b)
    elif operation == '-':
        return soustraction(a, b)
    elif operation == '*':
        return multiplication(a, b)
    elif operation == '/':
        return division(a, b)
    elif operation == '^':
        return puissance(a, b)
    elif operation == '%':
        return modulo(a, b)
    elif operation == '√':
        return racine_carree(a)
    else:
        return "Erreur : opération non reconnue"

def interface_utilisateur():
    print("\n========== CALCULATRICE ==========")
    print("Opérations disponibles :")
    print("  +   : Addition")
    print("  -   : Soustraction")
    print("  *   : Multiplication")
    print("  /   : Division")
    print("  ^   : Puissance")
    print("  Modulo: %")
    print("  sqrt: Racine carrée")
    print("  exit: Quitter")
    print("==========================================\n")

    while True:
        operation = input("Entrez une opération : ").strip().lower()
        if operation == 'sqrt':
            operation = '√'
        
        if operation == 'modulo':
            operation = '%'
       
        if operation == 'exit':
            print("Merci d’avoir utilisé la calculatrice. À bientôt ! 👋")
            break

        if operation not in ['+', '-', '*', '/', '^', '%', '√']:
            print("Opération invalide. Réessayez.\n")
            continue

        try:
            if operation == '√':
                a = float(input("Entrez un nombre : "))
                b = 0
            else:
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Entrée invalide veuillez entrer des nombres valides\n")
            continue

        resultat = calculatrice_avancee(a, b, operation)
        print("Résultat :", resultat)

interface_utilisateur()