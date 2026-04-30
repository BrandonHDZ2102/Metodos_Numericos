import math
def f(x):
    return math.cos(x) - x

def falsa_posicion(a, b, tol):
    i = 0
    while True:
        i += 1
        xr = b - (f(b)*(a - b))/(f(a) - f(b))
        if abs(f(xr)) < tol:
            print(f"Convergió en {i} iteraciones")
            return xr
        if f(a) * f(xr) < 0: b = xr
        else: a = xr

print(f"Raíz ejercicio 5: {falsa_posicion(0, 1, 1e-6)}")
