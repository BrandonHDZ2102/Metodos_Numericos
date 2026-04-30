import math
# f(x) = x^2 - cos(x)

def f(x):
    return x**2 - math.cos(x)

def secante(x0, x1, tol):
    print(f"{'i':<5} | {'x_next':<12} | {'Error':<12}")
    for i in range(15):
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        error = abs(x2 - x1)
        print(f"{i:<5} | {x2:<12.6f} | {error:<12.6e}")
        if error < tol:
            return x2
        x0, x1 = x1, x2
    return x2

print("\nRaíz ejercicio 5:")
secante(0, 1, 1e-6)
