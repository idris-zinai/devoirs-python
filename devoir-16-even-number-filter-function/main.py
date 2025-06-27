def supprimer_pairs():
    numbers = []
    while True:
        value = input("Entrez un nombre (ou 'q' pour arrêter) : ")
        if value.lower() == 'q':
            break
        try:
            number = int(value)
            numbers.append(number)
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            del numbers[i]
        else:
            i += 1
    print("Liste finale (sans les nombres pairs) :", numbers)

supprimer_pairs()
