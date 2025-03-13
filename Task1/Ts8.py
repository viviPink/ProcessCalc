import numpy as np


def calculate_matrix(A):
    A = np.array(A)
    n = A.shape[0]

    B = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(n):
            submatrix = A[i:, :j + 1]
            B[i, j] = np.sum(submatrix)

    return B

