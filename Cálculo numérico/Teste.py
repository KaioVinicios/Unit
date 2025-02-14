import numpy as np


def is_diagonal_dominant(A):
    for i in range(len(A)):
        row_sum = sum(abs(A[i][j]) for j in range(len(A)) if i != j)
        if abs(A[i][i]) <= row_sum:
            return False
    return True


def gauss_seidel(A, b, x0, precisao=1e-5, max_iter=1000):
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_j = sum(A[i][j] * x_new[j] for j in range(i)) + \
                sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_j) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < precisao:
            return x_new

        x = x_new

    raise ValueError(
        "O método não convergiu após o número máximo de iterações")


A = np.array([
    [12, 3, -6],
    [7, -15, 4],
    [3, 8, 10]
], dtype=float)
b = np.array([16, 7, 25], dtype=float)
x0 = np.zeros_like(b)


if is_diagonal_dominant(A):
    print("A matriz é diagonal dominante. Procedendo com os métodos iterativos.\n")
else:
    print(
        "A matriz não é diagonal dominante. Métodos iterativos podem não convergir. \n")

sol_seidel = gauss_seidel(A, b, x0)
print(sol_seidel)
