def calcular_errores(real, aprox):
    err_absoluto = abs(real - aprox)
    err_relativo = err_absoluto / abs(real)
    err_porcentual = err_relativo * 100
    
    print(f"Error Absoluto:   {err_absoluto}")
    print(f"Error Relativo:   {err_relativo}")
    print(f"Error Porcentual: {err_porcentual}%")

valor_real = 3.141592
valor_aprox = 3.14
calcular_errores(valor_real, valor_aprox)
