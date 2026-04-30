import math

# Ejercicio 3: Derivada de tan(x) con paso h pequeño
def f(x):
    return math.tan(x)

def diferencia_central_5pts(x, h):
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    return numerador / (12 * h)

x_buscado = 0.5 # Radianes
h = 0.001

resultado = diferencia_central_5pts(x_buscado, h)
valor_real = 1 / (math.cos(x_buscado)**2) # sec^2(x)

print(f"Derivada aproximada tan(x): {resultado}")
print(f"Valor real (sec^2): {valor_real}")
