import math
# f(x) = e^(-x^2) - x

def f(x):
    return math.exp(-(x**2)) - x

def secante(x0, x1, tol):
    while True:
        denominador = f(x0) - f(x1)
        x2 = x1 - (f(x1) * (x0 - x1)) / denominador
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2

print(f"Raíz ejercicio 2: {secante(0, 1, 1e-6)}")
