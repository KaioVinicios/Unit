import numpy as np
from funcoes_2a_unidade import gauss_seidel_or_jacobi

solution01 = gauss_seidel_or_jacobi(
    A=np.array([[3,4,7,20],
                [20,25,40,50],
                [10,15,20,22],
                [10,8,10,15]], dtype=float),
    b=np.array([504,1970,970,601], dtype=float),
    x0=np.zeros(4),
    seidel=False,
    max_iter=100000000
)

print(solution01)


# 02
solution02 = gauss_seidel_or_jacobi(
    A=np.array([[3, 2, 4], 
                [2, 2, 3], 
                [3, 3, 5]], dtype=float),
    b=np.array([80, 60, 95], dtype=float),
    x0=np.zeros(3),
    seidel=True
)

for n in solution02:
    print (n * 4)
# Não é possível realizar com Jacobi pois a matriz não é diagonalmente dominante,não convergindo dentro do número de iterações.