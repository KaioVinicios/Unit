import numpy as np

T0 = 300  # K
T = 1000  # K
mu0 = 1360  # cm^2 / V.s
q = 1.7e-19  # C
ni = 6.21e9  # cm^-3
rho_desejada = 6.5e6  # Ohm.cm


def mobilidade(T, T0, mu0):
    return mu0 * (T / T0) ** (-2.42)


def densidade_eletronica(N, ni):
    return 0.5 * (N + np.sqrt(N**2 + 4 * ni**2))


def resistividade(N, q, mu, ni):
    n = densidade_eletronica(N, ni)
    return 1 / (q * n * mu)


def funcao_resistividade(N):
    mu = mobilidade(T, T0, mu0)
    return resistividade(N, q, mu, ni) - rho_desejada


def newton_method(func, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        f_x0 = func(x0)
        f_prime_x0 = (func(x0 + tol) - f_x0) / tol  
        x1 = x0 - f_x0 / f_prime_x0
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("Função não muda de sinal no intervalo dado.")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol or abs(b - a) < tol:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return None


N_inicial = 1e10  
a = 1e8 
b = 1e12  

N_newton = newton_method(funcao_resistividade, N_inicial)
print(f"Valor de N encontrado pelo método de Newton: {N_newton}")

N_bissecao = bisection_method(funcao_resistividade, a, b)
print(f"Valor de N encontrado pelo método de Bisseção: {N_bissecao}")