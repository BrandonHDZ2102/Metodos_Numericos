import math

# Ejercicio 3: Integral de e^(x^2) de 0 a 1 (No tiene primitiva elemental)
def f(x):
    return math.exp(x**2)

def trapecio_compuesto(a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

a, b, n = 0, 1, 50
resultado = trapecio_compuesto(a, b, n)
print(f"Resultado Trapecio (e^x^2): {resultado}")
