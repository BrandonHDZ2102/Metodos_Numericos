# f(x) = x^2 - 7 (Encontrar la raíz cuadrada de 7)
# f'(x) = 2x

f = lambda x: x**2 - 7
df = lambda x: 2*x

def newton(x0, tol):
    it = 0
    while abs(f(x0)) > tol:
        x0 = x0 - f(x0)/df(x0)
        it += 1
    print(f"Cálculo completado en {it} iteraciones")
    return x0

print(f"Raíz de 7 es aprox: {newton(2, 1e-5)}")
