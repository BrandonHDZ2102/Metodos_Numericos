# g(x) = 2 / (x - 1)
# Este ejercicio muestra cómo se comporta el error paso a paso.

def g(x):
    return 2 / (x - 1)

def punto_fijo(x0, tol):
    print(f"{'Iter':<5} | {'Valor xi':<10}")
    for i in range(10):
        try:
            x1 = g(x0)
            print(f"{i:<5} | {x1:<10.4f}")
            if abs(x1 - x0) < tol:
                return x1
            x0 = x1
        except ZeroDivisionError:
            print("Error: División por cero.")
            return None
    return x0

print("Ejercicio 5 (Primeras 10 iteraciones):")
punto_fijo(3, 0.01)
