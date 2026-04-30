# f(x) = x^3 + 2x^2 + 10x - 20

def f(x):
    return x**3 + 2*x**2 + 10*x - 20

def secante(x0, x1, tol, n):
    for i in range(n):
        if abs(f(x1) - f(x0)) < 1e-10: break # Evitar división por cero
        
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

print(f"Raíz ejercicio 1: {secante(1, 2, 0.0001, 20)}")
