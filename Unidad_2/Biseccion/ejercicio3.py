# Ejercicio 3: Función Exponencial
# f(x) = e^x - 3x
import math

def f(x):
    return math.exp(x) - 3*x

def biseccion(a, b, tol):
    # Buscando raíz entre 0 y 1
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(f"Raíz de e^x - 3x: {biseccion(0, 1, 0.0001)}")
