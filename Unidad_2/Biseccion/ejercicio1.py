# Ejercicio 1: Raíz de una función cuadrática
# f(x) = x^2 - 5

def f(x):
    return x**2 - 5

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo.")
        return None
    
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0: break
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(f"Raíz aproximada de x^2 - 5: {biseccion(2, 3, 0.001)}")
