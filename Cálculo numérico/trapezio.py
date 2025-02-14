import math


def f(x):
    return (math.exp(x) * math.sin(x)) / (1 + x ** 2)


# Método Simples do Trapézio
def trapezio_simples(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2


# Método Composto do Trapézio
def trapezio_composto(f, a, b, n):
    h = (b - a) / n # h == "altura" de cada sub-intervalo.
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma


# Exemplo de uso
a = 0  # Limite inferior
b = 2  # Limite superior
n1 = 1  # Número de subintervalos (par para Simpson composto)
n2 = 5  # Número de subintervalos (par para Simpson composto)
n3 = 20  # Número de subintervalos (par para Simpson composto)

print("Trapézio Simples:", trapezio_simples(f, a, b))
print("Trapézio Composto:", trapezio_composto(f, a, b, n1))
print("Trapézio Composto:", trapezio_composto(f, a, b, n2))
print("Trapézio Composto:", trapezio_composto(f, a, b, n3))