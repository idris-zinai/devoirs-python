word = input("Veuillez entrer le mot : ")
vowel = 0
voyelles = "aeiouAEIOU"

for lettre in word:
    if lettre in voyelles:
        vowel += 1

print("Le nombre de voyelles dans le mot est :", vowel)
