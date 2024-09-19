import numpy as np
import matplotlib.pyplot as plt

# Definição da equação de Cp em função de T
def Cp(T):
    return (0.99403 
            + 1.671e-4 * T 
            + 9.7215e-8 * T**2 
            - 9.5838e-11 * T**3 
            + 1.9520e-14 * T**4)

def f(T):
    return Cp(T) - 1.1

def Cp_prime(T):
    return (1.671e-4 
            + 2 * 9.7215e-8 * T 
            - 3 * 9.5838e-11 * T**2 
            + 4 * 1.9520e-14 * T**3)

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        m = (a + b) / 2
        if f(m) == 0 or (b - a) / 2 < tol:
            return m
        if np.sign(f(m)) == np.sign(f(a)):
            a = m
        else:
            b = m
    return (a + b) / 2

def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivada zero. O método de Newton falhou.")
        x = x - fx / fpx
    return x

T_a = 1
T_b = 1200
T_initial_guess = 300

T_bisection = bisection_method(f, T_a, T_b)
T_newton = newton_method(f, Cp_prime, T_initial_guess)

print(f"Temperatura usando Bissecção: {T_bisection:.6f} K")
print(f"Temperatura usando Newton: {T_newton:.6f} K")