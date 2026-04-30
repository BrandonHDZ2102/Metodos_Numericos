# ⚡ Método de Newton-Raphson

Es un algoritmo eficiente para encontrar aproximaciones de los ceros o raíces de una función real. A diferencia de los métodos de intervalos, este solo requiere un único valor inicial ($x_0$) y utiliza la recta tangente a la función en ese punto para encontrar la siguiente aproximación.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Función Objetivo | Enlace al Código |
| :--- | :--- | :--- | :--- |
| 1 | **Polinomio Clásico** | $f(x) = x^3 - x - 1$ | [Ver Archivo](./ejercicio1.py) |
| 2 | **Función Trigonométrica** | $f(x) = \cos(x) - x^3$ | [Ver Archivo](./ejercicio2.py) |
| 3 | **Función Exponencial** | $f(x) = e^{-x} - x$ | [Ver Archivo](./ejercicio3.py) |
| 4 | **Raíz Cuadrada Manual** | $f(x) = x^2 - 7$ | [Ver Archivo](./ejercicio4.py) |
| 5 | **Convergencia Rápida** | $f(x) = x^{10} - 1$ | [Ver Archivo](./ejercicio5.py) |

---

### 💡 Nota Técnica
La fórmula iterativa de Newton-Raphson es:
$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

*Requiere que la derivada $f'(x_n)$ no sea cero en el punto de evaluación.*

---
[Volver a Unidad 2](../)
