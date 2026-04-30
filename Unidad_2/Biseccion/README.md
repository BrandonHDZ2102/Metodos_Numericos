# 🔍 Método de Bisección

El método de bisección es un algoritmo de búsqueda de raíces que divide repetidamente un intervalo a la mitad y selecciona el subintervalo donde se encuentra la raíz (basado en el cambio de signo de la función). Es un método cerrado y siempre convergente.

---

### 📋 Ejercicios del Método

| # | Ejercicio / Tipo | Función Objetivo | Enlace al Código |
| :--- | :--- | :--- | :--- |
| 1 | **Función Algebraica** | $f(x) = x^2 - 5$ | [Ver Archivo](./ejercicio1.py) |
| 2 | **Trascendental (Trig)** | $f(x) = \sin(x) - 0.5$ | [Ver Archivo](./ejercicio2.py) |
| 3 | **Exponencial** | $f(x) = e^x - 3x$ | [Ver Archivo](./ejercicio3.py) |
| 4 | **Aplicación de Ingeniería** | $f(x) = x^3 - 9x + 3$ | [Ver Archivo](./ejercicio4.py) |
| 5 | **Tolerancia Estricta** | $f(x) = x^3 - x - 2$ | [Ver Archivo](./ejercicio5.py) |

---

### 💡 Tips de Implementación
* Asegúrate de que el intervalo inicial $[a, b]$ cumpla con $f(a) \cdot f(b) < 0$.
* La precisión aumenta linealmente con el número de iteraciones.

---
[Volver a Unidad 2](../)
