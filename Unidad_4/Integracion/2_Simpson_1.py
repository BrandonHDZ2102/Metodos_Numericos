import math

# Ejercicio 1: Integral de sqrt(x) de 1 a 4
def f(x):
    return math.sqrt(x)

def simpson_13(a, b, n):
    if n % 2 != 0: n += 1  # n debe ser par
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        peso = 4 if i % 2 != 0 else 2
        suma += peso * f(a + i * h)
    return (h / 3) * suma

a, b, n = 1, 4, 10
resultado = simpson_13(a, b, n)
print(f"Resultado Simpson 1/3 (sqrt x): {resultado}")
