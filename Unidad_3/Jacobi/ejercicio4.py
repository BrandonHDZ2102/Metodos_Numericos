import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iter

# Datos Ejercicio 4 (4x4)
A = np.array([[10, 2, 1, 0], [1, 10, 2, 1], [2, 1, 10, 2], [0, 1, 2, 10]])
b = np.array([13, 14, 15, 13])
x0 = np.zeros(4)

sol, it = jacobi(A, b, x0, 1e-5, 50)
print(f"Solución Ejercicio 4: {sol}")
