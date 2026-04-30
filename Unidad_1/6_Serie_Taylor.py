import math

def serie_taylor_exponencial(x, iteraciones):
    valor_real = math.exp(x)
    aproximacion = 0
    
    print(f"{'Iteración':<12} | {'Aproximación':<15} | {'Error Absoluto':<18} | {'Error Relativo':<18}")
    print("-" * 70)
    
    for n in range(iteraciones):
        termino = (x**n) / math.factorial(n)
        aproximacion += termino
        
        error_abs = abs(valor_real - aproximacion)
        error_rel = error_abs / valor_real
        
        print(f"{n:<12} | {aproximacion:<15.6f} | {error_abs:<18.6e} | {error_rel:<18.6e}")

# Parámetros del ejercicio
valor_x = 1
num_iteraciones = 10

print(f"Aproximación de e^{valor_x} usando Serie de Taylor:\n")
serie_taylor_exponencial(valor_x, num_iteraciones)
