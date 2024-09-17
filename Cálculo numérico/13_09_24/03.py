import numpy as np
import matplotlib.pyplot as plt

# Definição da equação de Cp em função de T
def Cp(T):
    return (0.99403 
            + 1.671e-4 * T 
            + 9.7215e-8 * T**2 
            - 9.5838e-11 * T**3 
            + 1.9520e-14 * T**4)

# Faixa de temperatura
T_range = np.linspace(0, 1200, 500)

# Valores correspondentes de Cp para a faixa de temperatura
Cp_values = Cp(T_range)

# Plot do gráfico Cp vs T
plt.figure(figsize=(8, 6))
plt.plot(T_range, Cp_values, label=r'$C_p(T)$')
plt.axhline(y=1.1, color='r', linestyle='--', label=r'$C_p = 1.1 \, \mathrm{kJ/(Kg.K)}$')
plt.title(r'Gráfico de $C_p$ vs $T$')
plt.xlabel(r'Temperatura $T$ (K)')
plt.ylabel(r'$C_p$ (kJ/(Kg.K))')
plt.grid(True)
plt.legend()
plt.show()

# Definição da função f(T) para o método numérico (f(T) = Cp(T) - 1.1)
def f(T):
    return Cp(T) - 1.1

# Derivada da função Cp(T) para o método de Newton
def Cp_prime(T):
    return (1.671e-4 
            + 2 * 9.7215e-8 * T 
            - 3 * 9.5838e-11 * T**2 
            + 4 * 1.9520e-14 * T**3)

# Método da Bissecção
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

# Método de Newton
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

# Intervalo para o método da bissecção
T_a = 200  # Chute inferior
T_b = 400  # Chute superior

# Chute inicial para o método de Newton
T_initial_guess = 300

# Aplicação dos métodos
T_bisection = bisection_method(f, T_a, T_b)
T_newton = newton_method(f, Cp_prime, T_initial_guess)

print(f"Temperatura usando Bissecção: {T_bisection:.6f} K")
print(f"Temperatura usando Newton: {T_newton:.6f} K")