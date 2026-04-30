import math
def f(x):
    return x * math.log10(x) - 1.2

def falsa_posicion(a, b, tol):
    xr_viejo = 0
    for _ in range(100):
        xr = b - (f(b)*(a - b))/(f(a) - f(b))
        if abs(xr - xr_viejo) < tol: return xr
        xr_viejo = xr
        if f(a) * f(xr) < 0: b = xr
        else: a = xr
    return xr

print(f"Raíz ejercicio 2: {falsa_posicion(2, 3, 0.001)}")
