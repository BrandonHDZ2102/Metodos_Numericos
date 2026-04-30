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

# Datos Ejercicio 3
A = np.array([[4, 1, 2], [1, 3, 1], [1, 2, 5]])
b = np.array([9, 5, 13])
x0 = np.zeros(3)

sol, it = gauss_seidel(A, b, x0, 1e-4, 50)
print(f"Solución Ejercicio 3: {sol}")
