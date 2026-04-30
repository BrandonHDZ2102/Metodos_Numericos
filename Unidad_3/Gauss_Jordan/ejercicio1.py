import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)
    
    for i in range(n):
        # Escalar la fila para que el pivote sea 1
        Ab[i] = Ab[i] / Ab[i,i]
        # Hacer ceros en toda la columna i
        for j in range(n):
            if i != j:
                Ab[j] -= Ab[j,i] * Ab[i]
                
    return Ab[:,-1]

# Datos Ejercicio 1
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

print(f"Solución Ejercicio 1: {gauss_jordan(A, b)}")
