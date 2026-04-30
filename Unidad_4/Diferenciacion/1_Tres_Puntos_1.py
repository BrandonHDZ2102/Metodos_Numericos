import math

# Ejercicio 1: Diferencia Central para sin(x)
def f(x):
    return math.sin(x)

def diferencia_central_3pts(x, h):
    # Fórmula: [f(x+h) - f(x-h)] / (2h)
    derivada = (f(x + h) - f(x - h)) / (2 * h)
    return derivada

x_buscado = math.pi / 4  # 45 grados
h = 0.01

resultado = diferencia_central_3pts(x_buscado, h)
valor_real = math.cos(x_buscado)

print(f"Derivada aproximada (3 pts): {resultado}")
print(f"Valor real (cos): {valor_real}")
print(f"Error absoluto: {abs(valor_real - resultado)}")
