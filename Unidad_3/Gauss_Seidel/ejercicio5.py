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

# Datos Ejercicio 5 (Tolerancia estricta)
A = np.array([[15, 2, 3], [-3, 18, 1], [2, -4, 20]])
b = np.array([40, 50, 60])
x0 = np.zeros(3)

sol, it = gauss_seidel(A, b, x0, 1e-8, 100)
print(f"Solución Ejercicio 5: {sol}")
