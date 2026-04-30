import math
def f(x):
    return math.exp(-x) - x

def falsa_posicion(a, b, tol):
    while True:
        xr = b - (f(b)*(a - b))/(f(a) - f(b))
        if abs(f(xr)) < tol: return xr
        if f(a) * f(xr) < 0: b = xr
        else: a = xr

print(f"Raíz ejercicio 3: {falsa_posicion(0, 1, 0.0001)}")
