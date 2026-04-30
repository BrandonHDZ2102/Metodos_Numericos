import math

# Ejercicio 2: Diferencia Progresiva para ln(x)
def f(x):
    return math.log(x)

def diferencia_progresiva_3pts(x, h):
    # Fórmula: [-3f(x) + 4f(x+h) - f(x+2h)] / (2h)
    derivada = (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2 * h)
    return derivada

x_buscado = 2.0
h = 0.01

resultado = diferencia_progresiva_3pts(x_buscado, h)
valor_real = 1 / x_buscado

print(f"Derivada aproximada (3 pts Progresiva): {resultado}")
print(f"Valor real (1/x): {valor_real}")
