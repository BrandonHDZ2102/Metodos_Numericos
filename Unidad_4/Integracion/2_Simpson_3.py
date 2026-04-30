import math

# Ejercicio 3: Integral de cos(x) de 0 a pi/2
def f(x):
    return math.cos(x)

def simpson_13(a, b, n):
    if n % 2 != 0: n += 1
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        peso = 4 if i % 2 != 0 else 2
        suma += peso * f(a + i * h)
    return (h / 3) * suma

a, b, n = 0, math.pi/2, 10
resultado = simpson_13(a, b, n)
print(f"Resultado Simpson 1/3 (cos x): {resultado}")
