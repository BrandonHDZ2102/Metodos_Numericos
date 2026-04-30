# Ejercicio 2: Función con Seno
# f(x) = sin(x) - 0.5
import math

def f(x):
    return math.sin(x) - 0.5

def biseccion(a, b, tol):
    # Intervalo entre 0 y pi/2 para encontrar 30 grados (0.5235 rad)
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(f"Raíz de sin(x) - 0.5: {biseccion(0, 1.5, 0.0001)}")
