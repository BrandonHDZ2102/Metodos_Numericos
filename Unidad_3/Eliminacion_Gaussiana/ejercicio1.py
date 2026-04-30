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

# Datos Ejercicio 1
A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
b = np.array([7.85, -19.3, 71.4])

print(f"Resultado Ejercicio 1: {eliminacion_gaussiana(A, b)}")
