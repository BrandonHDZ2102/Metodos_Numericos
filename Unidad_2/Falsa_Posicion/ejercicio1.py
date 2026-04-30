def f(x):
    return x**3 - 2*x - 5

def falsa_posicion(a, b, tol):
    if f(a) * f(b) >= 0: return None
    while True:
        xr = b - (f(b)*(a - b))/(f(a) - f(b))
        if abs(f(xr)) < tol: return xr
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr

print(f"Raíz ejercicio 1: {falsa_posicion(2, 3, 0.0001)}")
