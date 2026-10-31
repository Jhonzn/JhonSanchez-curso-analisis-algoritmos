# Retroalimentación — Laboratorio 02 Dividir y vencer

**Estudiante:** Jhon Sánchez Álvarez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `d1a2e5f`

Buen trabajo: el código es correcto y el informe sigue la estructura pedida.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 15 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 18 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **83 / 100** |
| **Nota (0–5)** | **4.15** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara bien con el máximo de un arreglo: plantea las dos recurrencias, explica que combinar cuesta solo una comparación y concluye que dividir no mejora nada.
- En la pregunta 5 recomienda divide y vencerás, estima el tiempo para 1.000.000 de registros, dice claramente que es una estimación y no usa una regla de tres lineal.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 3 no dice a partir de qué tamaño divide y vencerás empieza a ganar. Solo dice que con n = 10 no se distinguen y que con n = 500 o más la diferencia es clara.
  → *Cómo corregirlo:* mire sus valores medidos en los tamaños 10, 50, 100 y 500 e indique entre qué dos tamaños cambia cuál algoritmo es más rápido; si no hay cambio en su rango, dígalo y explique por qué.

## 2. Calidad de la explicación teórica (15 / 20)
**Lo que hizo bien:**
- Plantea la recurrencia `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término, incluido el costo lineal del caso cruzado.
- Resuelve con el método maestro, comprueba la condición del caso 2 y llega a `Θ(n log n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 1 también pedía explicar por qué la fuerza bruta es `Θ(n²)`, y esa explicación no aparece.
  → *Cómo corregirlo:* describa los dos ciclos de `subarreglo_fuerza_bruta`, cuántas veces se repite cada uno según n y qué resulta al sumar el trabajo total.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos (serie de ocho días, un elemento, todo negativo, todo positivo, caso cruzado) y en las 30 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función modifica la lista recibida.
- Tiene *type hints*, *docstrings* con `Args` y `Returns`, y las líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (18 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, y cubre siete tamaños (de 10 a 4000).
- Se ve en el README, mide con `time.perf_counter()`, usa semilla fija, repite 10 veces cada medición y verifica que ambos algoritmos den la misma suma.
- Calcula el factor de crecimiento al duplicar n para los dos algoritmos y lo compara con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- Los números del informe no coinciden con la gráfica publicada. En la Parte 2 y en la pregunta 3 dice que con n = 4000 la fuerza bruta tarda cerca de 0.292 s, que sí se ve en la gráfica. Pero en la pregunta 2 y en la estimación de la pregunta 5 usa 0.314 s para n = 4000 y 0.083 s para n = 2000, mientras que la gráfica muestra cerca de 0.29 s y 0.087 s.
  → *Cómo corregirlo:* elija una sola fuente (los promedios de la gráfica publicada) y use esos mismos valores en todas las preguntas; si vuelve a medir, vuelva a publicar la gráfica para que coincida con el texto.
- Para divide y vencerás (n = 500 y 1000) usa valores "visuales" aproximados, que en esa escala casi no se pueden leer, y el propio informe admite que deben contrastarse con los datos reales.
  → *Cómo corregirlo:* agregue una tabla en el README con los promedios medidos de cada tamaño y calcule los factores a partir de ella.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab2-divide-y-vencer/` con todos los archivos pedidos.
- El README tiene su nombre, instrucciones de reproducción, las partes en orden y enlaces al código en cada parte práctica.
- Hay varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos soluciones coinciden con un cálculo de referencia en listas aleatorias, y `medicion.py` corre completo y genera la gráfica.
