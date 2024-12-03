from itertools import permutations
import numpy as np


def is_diagonally_dominant(matrix):
    """Check if a matrix is diagonally dominant."""
    return all(
        abs(matrix[i, i]) > sum(abs(matrix[i, j]) for j in range(len(matrix)) if j != i)
        for i in range(len(matrix))
    )


def gauss_seidel(matrix, vector, tolerance=1e-10, max_iterations=1000):
    """
    Solve a linear system using the Gauss-Seidel method.

    Parameters:
        matrix (ndarray): Coefficient matrix.
        vector (ndarray): Constant vector.
        tolerance (float): Convergence tolerance.
        max_iterations (int): Maximum number of iterations.

    Returns:
        solution (ndarray): Solution vector.
        iterations (int): Number of iterations performed.
    """
    n = len(vector)
    solution = np.zeros(n)
    previous_solution = np.zeros(n)

    for iteration in range(max_iterations):
        for i in range(n):
            sum1 = sum(matrix[i, j] * solution[j] for j in range(i))
            sum2 = sum(matrix[i, j] * previous_solution[j] for j in range(i + 1, n))
            solution[i] = (vector[i] - sum1 - sum2) / matrix[i, i]

        # Check for convergence
        if np.linalg.norm(solution - previous_solution, ord=np.inf) < tolerance:
            return solution, iteration + 1

        previous_solution = solution.copy()

    raise ValueError("Gauss-Seidel method did not converge within the maximum number of iterations.")


# Original system
coeff_matrix = np.array([
    [12, -3, 2, -1, 3],
    [9, 14, 1, 2, -1],
    [1, 7, -4, 23, 8],
    [3, 6, 22, 5, 7],
    [-8, -5, 5, 4, 33]
], dtype=float)

rhs_vector = np.array([23, 16, -85, 7, 19], dtype=float)

# Find a permutation that makes the matrix diagonally dominant
best_matrix = None
best_vector = None
row_indices = range(len(coeff_matrix))

for perm in permutations(row_indices):
    permuted_matrix = coeff_matrix[list(perm), :]
    permuted_vector = rhs_vector[list(perm)]
    if is_diagonally_dominant(permuted_matrix):
        best_matrix = permuted_matrix
        best_vector = permuted_vector
        break

if best_matrix is None:
    print("Could not rearrange the matrix to make it diagonally dominant.")
    best_matrix, best_vector = coeff_matrix, rhs_vector

# Solve the system using Gauss-Seidel
try:
    solution, iterations = gauss_seidel(best_matrix, best_vector)
    print(f"Solution found in {iterations} iterations:")
    print(solution)
except ValueError as e:
    print(e)