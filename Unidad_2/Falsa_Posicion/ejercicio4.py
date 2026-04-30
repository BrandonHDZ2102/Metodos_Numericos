def f(x):
    return 2*x**2 - 5*x + 1

def falsa_posicion(a, b, tol):
    # Buscando raíz en el intervalo [2, 3]
    for i in range(20):
        xr = b - (f(b)*(a - b))/(f(a) - f(b))
        if abs(f(xr)) < tol: return xr
        if f(a) * f(xr) < 0: b = xr
        else: a = xr
    return xr

print(f"Raíz ejercicio 4: {falsa_posicion(2, 3, 0.001)}")
