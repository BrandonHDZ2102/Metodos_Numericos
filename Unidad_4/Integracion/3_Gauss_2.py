import math

# Ejercicio 2: Integral de 1 / (1 + x^2) de 0 a 1 (Resultado: pi/4)
def f(x):
    return 1 / (1 + x**2)

def cuadratura_gaussiana_2pts(a, b):
    t = [-1/math.sqrt(3), 1/math.sqrt(3)]
    w = [1, 1]
    integral = 0
    for i in range(2):
        x_mapped = ((b - a) * t[i] + (a + b)) / 2
        integral += w[i] * f(x_mapped)
    return (b - a) / 2 * integral

a, b = 0, 1
resultado = cuadratura_gaussiana_2pts(a, b)
print(f"Resultado Cuadratura (1/(1+x^2)): {resultado}")
