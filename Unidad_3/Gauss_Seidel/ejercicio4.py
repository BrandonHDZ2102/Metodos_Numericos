import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1
    return x, max_iter

# Datos Ejercicio 4 (4x4)
A = np.array([[10, 2, 1, 0], [1, 10, 2, 1], [2, 1, 10, 2], [0, 1, 2, 10]])
b = np.array([13, 14, 15, 13])
x0 = np.zeros(4)

sol, it = gauss_seidel(A, b, x0, 1e-5, 50)
print(f"Solución Ejercicio 4: {sol}")
