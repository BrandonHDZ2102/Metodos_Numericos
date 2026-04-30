# Ejercicio 4: Cálculo de volumen en un tanque
# f(x) = x^3 - 9x + 3

def f(x):
    return x**3 - 9*x + 3

def biseccion(a, b, tol):
    for i in range(20): # Límite de 20 iteraciones
        m = (a + b) / 2
        if abs(f(m)) < tol: return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(f"Raíz aproximada (Ingeniería): {biseccion(0, 1, 1e-5)}")
