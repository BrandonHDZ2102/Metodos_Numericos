# Ejercicio 1: Derivada de un polinomio x^4 - 2x + 1
def f(x):
    return x**4 - 2*x + 1

def diferencia_central_5pts(x, h):
    # Fórmula: [-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)] / (12h)
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    derivada = numerador / (12 * h)
    return derivada

x_buscado = 1.0
h = 0.1

resultado = diferencia_central_5pts(x_buscado, h)
valor_real = 4*(x_buscado**3) - 2 # 4x^3 - 2

print(f"Derivada aproximada (5 pts): {resultado}")
print(f"Valor real: {valor_real}")
