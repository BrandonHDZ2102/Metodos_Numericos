import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)
    for i in range(n):
        for j in range(i+1, n):
            factor = Ab[j,i] / Ab[i,i]
            Ab[j,i:] -= factor * Ab[i,i:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i,-1] - np.dot(Ab[i,i+1:n], x[i+1:n])) / Ab[i,i]
    return x

# Datos Ejercicio 3
A = np.array([[2, 1, 1], [-1, 1, -1], [1, 2, 3]])
b = np.array([4, 2, 1])

print(f"Resultado Ejercicio 3: {eliminacion_gaussiana(A, b)}")
