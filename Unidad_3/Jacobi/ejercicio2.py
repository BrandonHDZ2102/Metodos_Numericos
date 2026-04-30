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

# Datos Ejercicio 2 (Diagonal Dominante)
A = np.array([[5, 1, 1], [1, 4, 1], [1, 1, 3]])
b = np.array([7, 6, 5])
x0 = np.zeros(3)

sol, it = jacobi(A, b, x0, 1e-5, 50)
print(f"Solución Ejercicio 2: {sol}")
