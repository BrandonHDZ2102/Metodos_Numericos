# 🔄 Método de Iteración de Punto Fijo

El método de punto fijo es un algoritmo abierto que busca un valor $x$ tal que $x = g(x)$. Para resolver una ecuación $f(x) = 0$, esta se reorganiza algebraicamente para despejar una $x$, y luego se aplica un proceso iterativo partiendo de un valor inicial $x_0$.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Función $g(x)$ | Enlace al Código |
| :--- | :--- | :--- | :--- |
| 1 | **Polinomio Simple** | $g(x) = \sqrt{x + 2}$ | [Ver Archivo](./ejercicio1.py) |
| 2 | **Función Trigonométrica** | $g(x) = \cos(x)$ | [Ver Archivo](./ejercicio2.py) |
| 3 | **Función Exponencial** | $g(x) = e^{-x}$ | [Ver Archivo](./ejercicio3.py) |
| 4 | **Despeje Lineal** | $g(x) = \frac{x^2 + 5}{6}$ | [Ver Archivo](./ejercicio4.py) |
| 5 | **Análisis de Convergencia** | $g(x) = \frac{2}{x-1}$ | [Ver Archivo](./ejercicio5.py) |

---

### 💡 Nota Técnica
Para que el método converja, la derivada de la función de iteración debe cumplir que $|g'(x)| < 1$ en el entorno de la raíz. Si esto no se cumple, el método divergerá y no encontrará la solución.

---
[Volver a Unidad 2](../)
