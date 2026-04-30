import math
# g(x) = e^-x

def g(x):
    return math.exp(-x)

def punto_fijo(x0, tol):
    it = 0
    while True:
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        it += 1
        if it > 100: break
    return x1

print(f"Raíz ejercicio 3: {punto_fijo(0, 0.0001)}")
