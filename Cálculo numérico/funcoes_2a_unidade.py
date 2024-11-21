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

def gauss_seidel_or_jacobi(A, b, x0=None, tol=1e-10, max_iter=1000, seidel=True):
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
