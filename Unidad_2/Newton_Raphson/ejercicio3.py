import math
# f(x) = e^-x - x
# f'(x) = -e^-x - 1

f = lambda x: math.exp(-x) - x
df = lambda x: -math.exp(-x) - 1

def newton(x0, tol):
    while abs(f(x0)) > tol:
        x0 = x0 - f(x0)/df(x0)
    return x0

print(f"Raíz ejercicio 3: {newton(0, 0.0001)}")
