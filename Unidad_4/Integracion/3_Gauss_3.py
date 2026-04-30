import math

# Ejercicio 3: Integral de ln(x) de 1 a 2
def f(x):
    return math.log(x)

def cuadratura_gaussiana_2pts(a, b):
    t = [-1/math.sqrt(3), 1/math.sqrt(3)]
    w = [1, 1]
    integral = 0
    for i in range(2):
        x_mapped = ((b - a) * t[i] + (a + b)) / 2
        integral += w[i] * f(x_mapped)
    return (b - a) / 2 * integral

a, b = 1, 2
resultado = cuadratura_gaussiana_2pts(a, b)
print(f"Resultado Cuadratura (ln x): {resultado}")
