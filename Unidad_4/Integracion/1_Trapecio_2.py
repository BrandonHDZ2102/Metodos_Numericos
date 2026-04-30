import math

# Ejercicio 2: Integral de sin(x) de 0 a pi
def f(x):
    return math.sin(x)

def trapecio_compuesto(a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

a, b, n = 0, math.pi, 20
resultado = trapecio_compuesto(a, b, n)
print(f"Resultado Trapecio (sin x): {resultado}")
