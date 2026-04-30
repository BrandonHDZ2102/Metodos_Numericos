import math
# f(x) = ln(x) + x - 5

def f(x):
    return math.log(x) + x - 5

def secante(x0, x1, tol):
    it = 0
    while it < 50:
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        if abs(f(x2)) < tol:
            return x2
        x0, x1 = x1, x2
        it += 1
    return x1

print(f"Raíz ejercicio 3: {secante(3, 4, 0.001)}")
