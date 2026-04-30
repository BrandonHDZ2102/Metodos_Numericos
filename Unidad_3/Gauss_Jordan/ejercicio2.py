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

# Datos Ejercicio 2
A = np.array([[1, 1, 1], [2, 3, 4], [3, 4, 9]])
b = np.array([6, 20, 31])

print(f"Solución Ejercicio 2: {gauss_jordan(A, b)}")
