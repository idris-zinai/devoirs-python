def factoriel(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Entez un nombre : "))
print("Factoriel:", factoriel(n))
