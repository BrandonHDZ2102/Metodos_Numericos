def decimal_a_binario(n):
    return bin(n).replace("0b", "")

numero = 25
print(f"El número decimal {numero} en binario es: {decimal_a_binario(numero)}")
