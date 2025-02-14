import numpy as np
import math


def f(x):
    return (math.exp(x) * math.sin(x)) / (1 + x ** 2)


def simpson_simples(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))


# Método Composto de Simpson (1/3)
def simpson_composto(f, a, b, n):
    if n % 2 != 0:
        print("teste")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma


# Exemplo de uso
a = 0  # Limite inferior
b = 2  # Limite superior
n1 = 1  # Número de subintervalos (par para Simpson composto)
n2 = 5  # Número de subintervalos (par para Simpson composto)
n3 = 20  # Número de subintervalos (par para Simpson composto)


print("Simpson Composto:", simpson_composto(f, a, b, n1))
print("Simpson Composto:", simpson_composto(f, a, b, n2))
print("Simpson Composto:", simpson_composto(f, a, b, n3))