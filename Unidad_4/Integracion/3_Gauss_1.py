import math

# Ejercicio 1: Integral de e^x de 0 a 1
def f(x):
    return math.exp(x)

def cuadratura_gaussiana_2pts(a, b):
    # Nodos y pesos para n=2
    t = [-1/math.sqrt(3), 1/math.sqrt(3)]
    w = [1, 1]
    integral = 0
    for i in range(2):
        # Cambio de variable de t a x
        x_mapped = ((b - a) * t[i] + (a + b)) / 2
        integral += w[i] * f(x_mapped)
    return (b - a) / 2 * integral

a, b = 0, 1
resultado = cuadratura_gaussiana_2pts(a, b)
print(f"Resultado Cuadratura (e^x): {resultado}")
