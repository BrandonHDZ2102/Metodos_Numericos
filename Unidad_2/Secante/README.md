# 📏 Método de la Secante

El método de la secante es un algoritmo de raíz abierta que evita la necesidad de calcular la derivada de la función (a diferencia de Newton-Raphson). En su lugar, utiliza una aproximación de la pendiente mediante una línea secante que pasa por dos puntos iniciales $x_0$ y $x_1$.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Función Objetivo | Enlace al Código |
| :--- | :--- | :--- | :--- |
| 1 | **Polinomio de Grado 3** | $f(x) = x^3 + 2x^2 + 10x - 20$ | [Ver Archivo](./ejercicio1.py) |
| 2 | **Trascendental Exponencial** | $f(x) = e^{-x^2} - x$ | [Ver Archivo](./ejercicio2.py) |
| 3 | **Función Logarítmica** | $f(x) = \ln(x) + x - 5$ | [Ver Archivo](./ejercicio3.py) |
| 4 | **Función Trigonométrica** | $f(x) = \tan(x) - x - 1$ | [Ver Archivo](./ejercicio4.py) |
| 5 | **Análisis de Oscilación** | $f(x) = x^2 - \cos(x)$ | [Ver Archivo](./ejercicio5.py) |

---

### 💡 Nota Técnica
La fórmula para calcular el siguiente punto es:
$x_{n+1} = x_n - \frac{f(x_n)(x_{n-1} - x_n)}{f(x_{n-1}) - f(x_n)}$

*A diferencia de los métodos cerrados, no requiere que la raíz esté "atrapada" entre los dos puntos iniciales, aunque una buena elección ayuda a la convergencia.*

---
[Volver a Unidad 2](../)
