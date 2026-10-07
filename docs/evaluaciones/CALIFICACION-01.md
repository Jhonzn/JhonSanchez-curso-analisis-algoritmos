# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Jhon Sánchez Álvarez · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `40ef08c`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 25 |
| Calidad de la explicación teórica | 17 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (18 / 25)
**Lo que hizo bien:**
- Explica que el proceso ya no cabe en la ventana de cuatro horas porque los registros pasaron de 20.000 a 1.200.000.
- Explica bien por qué duplicar el servidor solo da un alivio pasajero: si los datos se duplican, el trabajo se multiplica por cuatro.
- Relaciona el tiempo extra de cada madrugada con horas de servidor encendido acumuladas en años.
- Plantea muy bien la obligación del orden de la lista: no basta con ser rápido, hay que llamar primero a quien tiene mayor riesgo.

**Lo que puede mejorar:**
- Dice que importa más la eficiencia que la corrección; lo pedido era distinguir las dos y explicar que una no garantiza la otra.
- El segundo ejemplo (pedidos de una empresa) es genérico: no es un sistema que usted conozca ni precisa qué se procesa y cuánto.
- Los dos perjuicios a pacientes quedaron algo confusos, y en el primero asigna el costo al equipo de desarrollo sin explicar por qué no lo asume el paciente.

## 2. Calidad de la explicación teórica (17 / 25)
**Lo que hizo bien:**
- Justifica bien por qué usaría el peor caso para decidir la entrada a producción.
- Deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando la condición del caso 2.
- Presenta la tabla de complejidades.

**Lo que puede mejorar:**
- Los tres casos no se definen diciendo claramente que el peor es el máximo, el mejor el mínimo y el promedio la media, sobre todas las entradas de un mismo tamaño `n`.
- El análisis de insertion sort no es línea a línea: usa un pseudocódigo genérico y no cuenta cuántas veces se ejecuta cada línea de su propia función.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor) en los tres escenarios, no cambian la lista recibida y cuentan comparaciones entre elementos. No usan `sorted()` ni `list.sort()`, y la mezcla de merge sort es propia y recursiva.
- Hay type hints y docstrings en las funciones, y el código es ordenado.

**Lo que puede mejorar:**
- `generar_casi_ordenado` no entrega valores distintos: los registros nuevos se sacan de todo el rango y se repiten con valores de la parte ordenada (con n = 100 solo hay 98 valores distintos).
- Algunos docstrings de las funciones `main` son mínimos y no describen qué hacen ni qué producen.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda.
- En 3.2 identifica con cifras de n = 6.400 cuál escenario es el peor (inverso), el mejor (casi ordenado) y el promedio (aleatorio).
- En 4.2 describe lo que hace cada curva y lo relaciona con Θ(n²) y Θ(n log n).
- El concepto técnico recomienda merge sort, responde a la propuesta del servidor con datos medidos, extrapola a 1.200.000 registros declarándolo estimación (unas 6,19 horas para insertion sort, unos 3 segundos para merge sort) y discute memoria y riesgo de cambio de canal.

**Lo que puede mejorar:**
- Los tiempos citados para n = 6.400 cambian de un párrafo a otro (0,635 y 0,634 s para insertion sort; 0,0106 y 0,0112 s para merge sort); use una sola corrida y dígalo.
- No indica si repitió las mediciones ni explica con datos qué pasa en tamaños pequeños.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta en ubicación válida, con todos los archivos del entregable, informe por partes y nombre al inicio.
- Gráficas visibles y enlaces al código de cada parte, a `algoritmos.py` y a `datos.py`.
- Siete commits descriptivos sobre el laboratorio.

**Lo que puede mejorar:**
- Las instrucciones de reproducción piden activar el entorno y usar `requirements.txt` "desde la carpeta del laboratorio", pero ambos están en la raíz del repositorio.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan correctamente y se generan las gráficas. Solo falla la condición de valores distintos en el escenario casi ordenado.

## Para el próximo laboratorio
- Defina cada caso (peor, mejor, promedio) indicando sobre qué entradas y con qué tamaño se toma, y haga el conteo línea a línea de su propio código.
- Distinga con claridad corrección y eficiencia, y use ejemplos propios con datos y restricción.
- Verifique que los generadores cumplan lo pedido (valores distintos) con una prueba pequeña.
- Cite cifras de una sola corrida y diga cuántas veces repitió cada medición.
- Revise que las instrucciones de reproducción coincidan con la ubicación real de los archivos.
