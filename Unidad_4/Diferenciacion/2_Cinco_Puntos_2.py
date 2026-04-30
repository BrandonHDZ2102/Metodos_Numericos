import math

# Ejercicio 2: Derivada de cos(x)
def f(x):
    return math.cos(x)

def diferencia_central_5pts(x, h):
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    return numerador / (12 * h)

x_buscado = math.pi / 3 # 60 grados
h = 0.05

resultado = diferencia_central_5pts(x_buscado, h)
valor_real = -math.sin(x_buscado)

print(f"Derivada aproximada cos(x): {resultado}")
print(f"Valor real (-sin): {valor_real}")
