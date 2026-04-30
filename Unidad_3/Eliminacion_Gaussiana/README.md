# 📉 Eliminación Gaussiana

Este método directo transforma un sistema de ecuaciones lineales en una matriz triangular superior mediante operaciones elementales. Posteriormente, utiliza la **sustitución hacia atrás** para encontrar el valor de cada incógnita.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Tamaño | Enlace Directo |
| :--- | :--- | :--- | :--- |
| 1 | **Sistema Base 3x3** | $3 \times 3$ | [Ver Código](./ejercicio1.py) |
| 2 | **Matriz de Coeficientes A** | $3 \times 3$ | [Ver Código](./ejercicio2.py) |
| 3 | **Aplicación en Estructuras** | $3 \times 3$ | [Ver Código](./ejercicio3.py) |
| 4 | **Sistema 4x4** | $4 \times 4$ | [Ver Código](./ejercicio4.py) |
| 5 | **Análisis de Precisión** | $3 \times 3$ | [Ver Código](./ejercicio5.py) |

---

## ⚙️ Pasos del Algoritmo
1. **Fase de eliminación:** Se eliminan las incógnitas de las filas inferiores para crear ceros debajo de la diagonal principal.
2. **Sustitución hacia atrás:** Se resuelve la última ecuación (que ya solo tiene una incógnita) y se sustituye el valor hacia arriba.

---
[Volver a Unidad 3](../)
