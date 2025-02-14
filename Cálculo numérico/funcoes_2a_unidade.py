import numpy as np

def is_diagonally_dominant(A):
    """
    Verifica se a matriz A é diagonalmente dominante.
    
    Parâmetros:
    A (ndarray): Matriz quadrada dos coeficientes.
    
    Retorna:
    bool: True se a matriz for diagonalmente dominante, False caso contrário.
    """
    n = A.shape[0]
    for i in range(n):
        diagonal_element = abs(A[i, i])
        off_diagonal_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diagonal_element < off_diagonal_sum:
            return False
    return True

def gauss_seidel_or_jacobi(A, b, x0=None, tol=1e-10, max_iter=10000, seidel=True):
    """
    Resolve um sistema de equações lineares utilizando os métodos de Gauss-Jacobi ou Gauss-Seidel.

    Parâmetros:
    A (ndarray): Matriz de coeficientes do sistema (deve ser quadrada).
    b (ndarray): Vetor de termos independentes.
    x0 (ndarray): Vetor inicial para a solução (default: vetor nulo).
    tol (float): Tolerância para critério de convergência.
    max_iter (int): Número máximo de iterações.
    seidel (bool): Se True, utiliza o método de Gauss-Seidel; caso contrário, usa Gauss-Jacobi.

    Retorna:
    ndarray: Aproximação da solução do sistema.
    """
    if not is_diagonally_dominant(A):
        print("\nAviso: A matriz A não é diagonalmente dominante. O método pode não convergir.\n")

    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_ = sum(A[i, j] * (x_new[j] if seidel else x[j]) for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i, i]
        
        # Critério de parada: norma do erro relativo
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Convergiu após {k+1} iterações.")
            return x_new
        x = x_new
    
    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# # Exemplo de uso
# if __name__ == "__main__":
#     A = np.array([[4, 1, 2],
#                   [3, 5, 1],
#                   [1, 1, 3]], dtype=float)
#     b = np.array([4, 7, 3], dtype=float)
#     x0 = np.zeros(len(b))

#     print("Gauss-Jacobi:")
#     try:
#         sol_jacobi = gauss_seidel_or_jacobi(A, b, x0=x0, seidel=False)
#         print("Solução:", sol_jacobi)
#     except ValueError as e:
#         print(e)
    
#     print("\nGauss-Seidel:")
#     try:
#         sol_seidel = gauss_seidel_or_jacobi(A, b, x0=x0, seidel=True)
#         print("Solução:", sol_seidel)
#     except ValueError as e:
#         print(e)


def trapezoidal_rule(f, a, b, n):
    """
    Calcula a integral de uma função usando o método do trapézio.
    
    Parâmetros:
    - f: Função a ser integrada.
    - a: Limite inferior da integração.
    - b: Limite superior da integração.
    - n: Número de subdivisões (deve ser um número inteiro positivo).
    
    Retorno:
    - Aproximação numérica da integral de f entre a e b.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    return integral * h

def simpsons_rule(f, a, b, n):
    """
    Calcula a integral de uma função usando o método de Simpson.
    
    Parâmetros:
    - f: Função a ser integrada.
    - a: Limite inferior da integração.
    - b: Limite superior da integração.
    - n: Número de subdivisões (deve ser par).
    
    Retorno:
    - Aproximação numérica da integral de f entre a e b.
    """
    if n % 2 != 0:
        raise ValueError("O número de subdivisões (n) deve ser par para o método de Simpson.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    # Soma dos termos com coeficiente 4 (índices ímpares)
    for i in range(1, n, 2):
        x_i = a + i * h
        integral += 4 * f(x_i)
    
    # Soma dos termos com coeficiente 2 (índices pares)
    for i in range(2, n, 2):
        x_i = a + i * h
        integral += 2 * f(x_i)
    
    return (h / 3) * integral


A = np.array([[12, 3, -6], [3, 8, 10], [7, -15, 4]], dtype=float)
b = np.array([16, 7, 25], dtype=float)
x0 = np.zeros_like(b)

print(gauss_seidel_or_jacobi(A, b, x0=x0, seidel=True))