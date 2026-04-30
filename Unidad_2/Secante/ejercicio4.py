import math
# f(x) = tan(x) - x - 1

def f(x):
    return math.tan(x) - x - 1

def secante(x0, x1, tol):
    # Se recomienda puntos cercanos a 1 para evitar asíntotas
    for _ in range(100):
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

print(f"Raíz ejercicio 4: {secante(1, 1.2, 1e-5)}")
