# 🚀 Método de Gauss-Seidel

El método de Gauss-Seidel es un procedimiento iterativo para resolver sistemas de ecuaciones lineales. A diferencia del método de Jacobi, este utiliza los valores actualizados de las incógnitas en cuanto están disponibles, lo que generalmente reduce el número de iteraciones necesarias para alcanzar la convergencia.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Tamaño | Enlace Directo |
| :--- | :--- | :--- | :--- |
| 1 | **Sistema Base 3x3** | $3 \times 3$ | [Ver Código](./ejercicio1.py) |
| 2 | **Convergencia Acelerada** | $3 \times 3$ | [Ver Código](./ejercicio2.py) |
| 3 | **Matriz de Ingeniería** | $3 \times 3$ | [Ver Código](./ejercicio3.py) |
| 4 | **Sistema 4x4** | $4 \times 4$ | [Ver Código](./ejercicio4.py) |
| 5 | **Tolerancia de Precisión** | $3 \times 3$ | [Ver Código](./ejercicio5.py) |

---

## ⚙️ Ventajas sobre Jacobi
* **Velocidad:** Al usar información "fresca" (valores recién calculados), la aproximación mejora más rápido en cada paso.
* **Memoria:** Requiere menos almacenamiento temporal ya que no necesita guardar el vector completo de la iteración anterior por separado.

---
[Volver a Unidad 3](../)
