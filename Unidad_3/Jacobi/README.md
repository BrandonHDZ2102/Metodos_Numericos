# 🏁 Método de Jacobi

El método de Jacobi es un algoritmo iterativo para resolver sistemas de ecuaciones lineales $Ax = b$. El algoritmo comienza con una aproximación inicial $x^{(0)}$ y genera una secuencia de vectores que, bajo condiciones de dominancia diagonal, converge a la solución exacta.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Tamaño | Enlace Directo |
| :--- | :--- | :--- | :--- |
| 1 | **Sistema Base** | $3 \times 3$ | [Ver Código](./ejercicio1.py) |
| 2 | **Diagonal Dominante** | $3 \times 3$ | [Ver Código](./ejercicio2.py) |
| 3 | **Convergencia Estándar** | $3 \times 3$ | [Ver Código](./ejercicio3.py) |
| 4 | **Sistema 4x4** | $4 \times 4$ | [Ver Código](./ejercicio4.py) |
| 5 | **Análisis de Tolerancia** | $3 \times 3$ | [Ver Código](./ejercicio5.py) |

---

## ⚙️ Condición de Convergencia
Para asegurar que el método de Jacobi converja, la matriz $A$ debe ser **diagonalmente dominante**. Esto significa que en cada fila, el valor absoluto del elemento de la diagonal debe ser mayor que la suma de los valores absolutos de los demás elementos de esa misma fila.

---
[Volver a Unidad 3](../)
