# Demostración de error de redondeo
valor_exacto = 1 / 3
valor_redondeado = 0.3333333333
error = abs(valor_exacto - valor_redondeado)

print(f"Valor exacto (1/3): {valor_exacto}")
print(f"Valor redondeado:   {valor_redondeado}")
print(f"Error de redondeo:  {error:.15f}")
