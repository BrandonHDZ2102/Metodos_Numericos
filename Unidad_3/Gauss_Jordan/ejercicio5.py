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

# Datos Ejercicio 5
A = np.array([[2, 4, 6], [4, 5, 6], [3, 1, -2]])
b = np.array([18, 24, 4])

print(f"Solución Ejercicio 5: {gauss_jordan(A, b)}")
