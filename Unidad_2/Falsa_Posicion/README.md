# 📍 Método de Falsa Posición

El método de la falsa posición es un método iterativo de resolución numérica de ecuaciones no lineales. Combina las características del método de bisección y del método de la secante, utilizando una interpolación lineal para aproximar la raíz de forma más eficiente en ciertos intervalos.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Función Objetivo | Enlace al Código |
| :--- | :--- | :--- | :--- |
| 1 | **Polinómica Grado 3** | $f(x) = x^3 - 2x - 5$ | [Ver Archivo](./ejercicio1.py) |
| 2 | **Trascendental Mixta** | $f(x) = x \cdot \log_{10}(x) - 1.2$ | [Ver Archivo](./ejercicio2.py) |
| 3 | **Exponencial Negativa** | $f(x) = e^{-x} - x$ | [Ver Archivo](./ejercicio3.py) |
| 4 | **Aplicación de Física** | $f(x) = 2x^2 - 5x + 1$ | [Ver Archivo](./ejercicio4.py) |
| 5 | **Análisis de Error** | $f(x) = \cos(x) - x$ | [Ver Archivo](./ejercicio5.py) |

---

### 💡 Nota Técnica
A diferencia de la bisección, este método aprovecha los valores de la función en los extremos para calcular la siguiente aproximación mediante la fórmula:
$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$

---
[Volver a Unidad 2](../)
