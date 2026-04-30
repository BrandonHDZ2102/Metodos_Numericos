# f(x) = x^10 - 1
# f'(x) = 10x^9

f = lambda x: x**10 - 1
df = lambda x: 10*x**9

def newton(x0, tol):
    # Newton es muy sensible al punto inicial en potencias altas
    for i in range(50):
        x0 = x0 - f(x0)/df(x0)
        if abs(f(x0)) < tol:
            return x0
    return x0

print(f"Raíz ejercicio 5: {newton(0.5, 1e-7)}")
