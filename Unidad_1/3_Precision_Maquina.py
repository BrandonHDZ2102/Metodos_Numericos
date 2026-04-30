# Cálculo del Épsilon de la máquina
epsilon = 1.0
while (1.0 + epsilon) > 1.0:
    epsilon /= 2.0

epsilon *= 2.0
print(f"El Épsilon de la máquina es: {epsilon}")
