import math

def serie_exp(x, n):
    # Aproximación de e^x usando n términos
    suma = 0
    for i in range(n):
        suma += (x**i) / math.factorial(i)
    return suma

x_val = 1
exacto = math.exp(x_val)
aprox = serie_exp(x_val, 3) # Truncado a 3 términos

print(f"Valor exacto e^{x_val}: {exacto}")
print(f"Valor truncado (3 térm): {aprox}")
print(f"Error de truncamiento: {abs(exacto - aprox)}")
