import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i,i]
        for j in range(n):
            if i != j:
                Ab[j] -= Ab[j,i] * Ab[i]
    return Ab[:,-1]

# Datos Ejercicio 4 (4x4)
A = np.array([[2, 1, 0, 4], [-4, -2, 3, -7], [4, 1, -2, 8], [0, -3, -12, -1]])
b = np.array([2, -9, 2, 2])

print(f"Solución Ejercicio 4: {gauss_jordan(A, b)}")
