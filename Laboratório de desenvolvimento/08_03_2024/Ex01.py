import random

def megaSena(quantidade):
    numeros = []
    while len(numeros) != quantidade:
        n = random.randint(1, 61)
        if n not in numeros:
            numeros.append(n)
    return sorted(numeros)

print(megaSena(6))