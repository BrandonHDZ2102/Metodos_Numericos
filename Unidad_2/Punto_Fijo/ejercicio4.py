# Para f(x) = x^2 - 6x + 5 = 0
# g(x) = (x^2 + 5) / 6

def g(x):
    return (x**2 + 5) / 6

def punto_fijo(x0, tol):
    for _ in range(20):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

print(f"Raíz ejercicio 4: {punto_fijo(0, 1e-4)}")
