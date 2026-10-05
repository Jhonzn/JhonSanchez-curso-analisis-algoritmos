# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Jhon Fernando Sánchez Álvarez · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `de05592`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 25 |
| Calidad de la explicación teórica | 16 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **68 / 100** |
| **Nota (0–5)** | **3.40** |

## 1. Corrección conceptual (16 / 25)
**Lo que hizo bien:**
- Explica que el sistema ya no cabe en la ventana de cuatro horas por el crecimiento de 20.000 a 1.200.000 registros.
- Explica bien por qué duplicar el servidor solo da un alivio temporal (si los datos se duplican, el trabajo se multiplica por cuatro).
- Identifica dos perjuicios a pacientes de alto riesgo y dice quién asume el costo en cada uno.

**Lo que puede mejorar:**
- El segundo ejemplo (pedidos de una empresa) es genérico: no es un sistema que usted conozca y no precisa bien qué restricción se incumple.
- Falta explicar con más claridad cómo el tiempo de ejecución se vuelve consumo de energía acumulado al correr todas las madrugadas durante años.
- La obligación adicional que impone el orden de la lista (a quién se llama primero) quedó mezclada con la reputación; faltó centrarse en que el orden debe ser correcto, no solo rápido.

## 2. Calidad de la explicación teórica (16 /25)
**Lo que hizo bien:**
- Justifica bien por qué usaría el peor caso para decidir la entrada a producción.
- Deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando el caso 2.
- Presenta la tabla de complejidades.

**Lo que puede mejorar:**
- Los tres casos no se definen indicando sobre qué conjunto de entradas (y con qué tamaño fijo) se toma el máximo, el mínimo y el promedio.
- El análisis de insertion sort no es línea a línea: usa un pseudocódigo genérico y no cuenta cuántas veces se ejecuta cada línea de su propia implementación.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien, no modifican la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. Merge sort tiene su propia mezcla recursiva.
- Los generadores producen listas con valores distintos y semilla reproducible.

**Lo que puede mejorar:**
- Hay varias faltas de estilo PEP 8 (espacios en blanco al final de línea, falta de líneas en blanco entre funciones, importación antes del docstring del módulo en `datos.py`).
- Los archivos `parte3_casos.py` y `parte4_complejidad.py` no tienen docstring de módulo, y el docstring de `merge` no sigue bien el formato Google.
- En el escenario B, los registros nuevos son todos los de menor riesgo, lo que lo hace más fácil de lo que describe el enunciado.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda.
- La conclusión de 4.2 describe lo que hace cada curva y la relaciona con las complejidades calculadas.
- El concepto técnico recomienda merge sort con datos medidos (n = 6.400), extrapola a 1.200.000 registros declarándolo como estimación y responde a la propuesta del servidor.
- Considera la memoria adicional y el riesgo de que cambie el canal de entrada.

**Lo que puede mejorar:**
- En 3.2 no dice con claridad cuál escenario resultó peor caso, mejor caso y promedio, ni contrasta con evidencia concreta de las gráficas; solo dice "se acertó".
- Los tiempos citados en el informe (0,63 s) no coinciden con lo que muestra la gráfica publicada (cerca de 0,8 s); conviene indicar de qué corrida salen.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Carpeta en una ubicación válida, informe organizado por partes, gráficas visibles y enlaces al código en la Parte 3.
- Seis commits descriptivos.

**Lo que puede mejorar:**
- El enlace de la Parte 4 apunta a `parte4_tiempo.py`, que no existe; el archivo se llama `parte4_complejidad.py`.
- Faltan las instrucciones para reproducir los experimentos (activar el entorno y qué comando ejecutar por parte).
- Su nombre aparece solo al final del informe, no al inicio.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan correctamente (de mayor a menor) en los tres escenarios y se generan las tres gráficas.

## Para el próximo laboratorio
- Defina cada concepto teórico completo (sobre qué se toma el máximo, el mínimo o el promedio) y haga el conteo línea a línea con su propio código.
- Use ejemplos propios y concretos, con cantidad de datos y restricción incumplida.
- Revise que los enlaces del informe apunten a archivos que existan y agregue las instrucciones de reproducción.
- Corrija el estilo (PEP 8) y agregue docstring a todos los archivos y funciones.
- En el análisis de gráficas, diga explícitamente qué se observa en cada escenario y compárelo con su predicción.
