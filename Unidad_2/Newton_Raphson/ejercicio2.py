import math
# f(x) = cos(x) - x^3
# f'(x) = -sin(x) - 3x^2

f = lambda x: math.cos(x) - x**3
df = lambda x: -math.sin(x) - 3*x**2

def newton(x0, tol):
    x_prev = x0
    while True:
        x_next = x_prev - f(x_prev)/df(x_prev)
        if abs(x_next - x_prev) < tol:
            return x_next
        x_prev = x_next

print(f"Raíz ejercicio 2: {newton(0.5, 1e-6)}")
