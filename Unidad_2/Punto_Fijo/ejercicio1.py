import math
# Para resolver x^2 - x - 2 = 0
# g(x) = sqrt(x + 2)

def g(x):
    return math.sqrt(x + 2)

def punto_fijo(x0, tol, n):
    print(f"{'i':<5} | {'xi':<12} | {'Error':<12}")
    for i in range(n):
        x1 = g(x0)
        error = abs(x1 - x0)
        print(f"{i:<5} | {x1:<12.6f} | {error:<12.6e}")
        if error < tol:
            return x1
        x0 = x1
    return x0

print("Ejercicio 1:")
punto_fijo(1.5, 0.0001, 15)
