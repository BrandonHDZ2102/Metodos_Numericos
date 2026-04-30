# Ejercicio 1: Integral de x^2 de 0 a 1
def f(x):
    return x**2

def trapecio_compuesto(a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

a, b, n = 0, 1, 10
resultado = trapecio_compuesto(a, b, n)
print(f"Resultado Trapecio (x^2): {resultado}")
