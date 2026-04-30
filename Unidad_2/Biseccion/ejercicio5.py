# Ejercicio 5: Evaluación con Tolerancia Estricta
# f(x) = x^3 - x - 2

def f(x):
    return x**3 - x - 2

def biseccion(a, b, tol):
    it = 0
    while (b - a) / 2 > tol:
        it += 1
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    print(f"Iteraciones realizadas: {it}")
    return (a + b) / 2

# Tolerancia de 10^-8
print(f"Raíz con alta precisión: {biseccion(1, 2, 1e-8)}")
