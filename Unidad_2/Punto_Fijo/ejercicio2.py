import math
# g(x) = cos(x)

def g(x):
    return math.cos(x)

def punto_fijo(x0, tol):
    for i in range(50):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

print(f"Raíz ejercicio 2: {punto_fijo(0.5, 1e-5)}")
