import math

# Ejercicio 3: Diferencia Regresiva para e^x
def f(x):
    return math.exp(x)

def diferencia_regresiva_3pts(x, h):
    # Fórmula: [3f(x) - 4f(x-h) + f(x-2h)] / (2h)
    derivada = (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2 * h)
    return derivada

x_buscado = 1.0
h = 0.01

resultado = diferencia_regresiva_3pts(x_buscado, h)
valor_real = math.exp(1.0)

print(f"Derivada aproximada (3 pts Regresiva): {resultado}")
print(f"Valor real: {valor_real}")
