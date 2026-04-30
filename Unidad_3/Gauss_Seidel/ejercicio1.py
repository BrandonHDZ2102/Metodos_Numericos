import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            # Aquí está la clave: usamos los valores de x[j] actualizados
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
            
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1
    return x, max_iter

# Datos Ejercicio 1
A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
b = np.array([6, 25, -11])
x0 = np.zeros(3)

sol, it = gauss_seidel(A, b, x0, 1e-4, 50)
print(f"Solución Gauss-Seidel: {sol} en {it} iteraciones")
