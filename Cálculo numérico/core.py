import math

def funcao(x):
    return 2*x*(math.e**x) - 3

def derivada(x):
    return 2*(math.e**x) + 2*x * math.e**x


def bisseccao(xa, xb, precisao):  # OK
    # if not(funcao(xa) * funcao(xb) < 0):  
    #     xa = float(input('Digite um novo valor para Xa: '))
    #     xb = float(input('Digite um novo valor para Xb: '))

    if funcao(xa) * funcao(xb) > 0:
        print('\nATENÇÃO! f(Xa) * f(Xb) > 0\nO intervalo [Xa, Xb] fornecido PODE ou NÃO conter uma raiz segundo o teorema de Bolzano.\n')

    while abs(xb - xa) >= precisao:  
        xm = (xa + xb) / 2
        if abs(funcao(xm)) < precisao:  
            return print(f'Raiz = {xm};')
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
    return print(f'Raiz encontrada: {xm};')


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:  
            break
        x = x_novo  
    print(f'Raiz encontrada: {x}')


def secante(x, x1, precisao):
    while abs(funcao(x1)) > precisao:  
        x_novo = x1 - (funcao(x1) * (x1 - x)) / (funcao(x1) - funcao(x))
        if abs(x_novo - x1) < precisao:
            break
        x, x1 = x1, x_novo  
    print(f'Raiz encontrada: {x1}')



def gauss_jacobi_equations(equations, x0, precisao=1e-4, max_iter=1000):
    n = len(equations)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            left_side, right_side = equations[i](x)
            x_new[i] = right_side / left_side

        # Verifica se a convergência foi atingida
        if max(abs(x_new[i] - x[i]) for i in range(n)) < precisao:
            return x_new, _

        x = x_new

    raise ValueError(
        "O método não convergiu após o número máximo de iterações")

# Definindo as equações diretamente


def equation1(x): return 3, 7.85 + 0.1 * x[1] + 0.2 * x[2]
def equation2(x): return 7, -19.3 - 0.1 * x[0] + 0.3 * x[2]
def equation3(x): return 10, 71.4 - 0.3 * x[0] + 0.2 * x[1]


equations = [equation1, equation2, equation3]
x0 = [0, 0, 0]  # Aproximação inicial

sol, iters = gauss_jacobi_equations(equations, x0)
print(f'Equações jacobi: solução encontrada: {sol} em {iters} iterações')
# 4 iterações

def gauss_seidel_equations(equations, x0, precisao=1e-4, max_iter=1000):
    n = len(equations)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            left_side, right_side = equations[i](x_new)
            x_new[i] = right_side / left_side

        # Verifica se a convergência foi atingida
        if max(abs(x_new[i] - x[i]) for i in range(n)) < precisao:
            return x_new, _

        x = x_new

    raise ValueError(
        "O método não convergiu após o número máximo de iterações")

# Definindo as equações diretamente


def equation1(x): return 3, 7.85 + 0.1 * x[1] + 0.2 * x[2]
def equation2(x): return 7, -19.3 - 0.1 * x[0] + 0.3 * x[2]
def equation3(x): return 10, 71.4 - 0.3 * x[0] + 0.2 * x[1]


equations = [equation1, equation2, equation3]
x0 = [0, 0, 0]  # Aproximação inicial

sol, iters = gauss_seidel_equations(equations, x0)
print(f'Equações seidel: solução encontrada: {sol} em {iters} iterações')
# 3 iterações

import numpy as np


def gauss_jacobi(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_j = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, _

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Exemplo de uso
A = np.array([[3, - 0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype=float)
b = np.array([7.85, -19.3, 71.4], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_jacobi(A, b, x0)
print(f'Matriz jacobi: solução encontrada: {sol} em {iters} iterações')
# 4 iterações

import numpy as np


def gauss_seidel(A, b, x0, precisao=1e-4, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_j = sum(A[i][j] * x_new[j] for j in range(i)) + \
                sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Verifica se a convergência foi atingida
        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new, _

        x = x_new
    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


# Exemplo de uso
A = np.array([[3, - 0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype=float)
b = np.array([7.85, -19.3, 71.4], dtype=float)
x0 = np.zeros_like(b)

sol, iters = gauss_seidel(A, b, x0)
print(f'Matriz seidel: solução encontrada: {sol} em {iters} iterações')
# 3 iterações

# bisseccao(xa=3, xb=10, precisao=0.00001)
# newton(3, 0.00001)
# secante(2, 1, precisao=0.00001)
