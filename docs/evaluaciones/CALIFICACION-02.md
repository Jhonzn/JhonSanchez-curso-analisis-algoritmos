# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Jhon Sánchez Álvarez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `142ca5b`

Buen trabajo: el laboratorio funciona y está bien encaminado; con los ajustes de abajo quedará aún más sólido.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 14 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 19 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **81 / 100** |
| **Nota (0–5)** | **4.05** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Explica que con n = 10 la fuerza bruta es un poco más rápida y por qué (el costo extra de las llamadas recursivas), y que desde n = 50 gana divide y vencerás.
- En la pregunta del máximo de un arreglo muestra que dividir no mejora: ambas formas son `Θ(n)`.
- Recomienda divide y vencerás y estima el tiempo para 1.000.000 de registros, declarando que es una estimación y no una medición.

**Lo que puede mejorar:**
- En la pregunta del máximo falta decir explícitamente que combinar cuesta solo una comparación, `Θ(1)`, y por eso dividir no ayuda.
- Las cifras de la estimación salen de un valor (n = 4000) que no coincide con lo que muestra su gráfica (ver punto 4).

## 2. Calidad de la explicación teórica (14 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y la resuelve como `Θ(n log n)`.
- Justifica la fuerza bruta con la suma `n(n+1)/2` y menciona la suma acumulada.

**Lo que puede mejorar:**
- No explica de dónde sale cada término: por qué 2 subproblemas, por qué de tamaño n/2 y por qué el caso cruzado cuesta `Θ(n)`.
- No verifica la condición del método maestro: debía comparar `f(n)` con `n^(log_2 2) = n`, decir qué caso es y por qué aplica.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en 30 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función modifica la lista recibida.
- Tiene tipos y documentación en cada función, y el código cumple PEP 8.

**Lo que puede mejorar:**
- Dejó los comentarios `TODO` de la plantilla dentro del código ya terminado; conviene borrarlos.

## 4. Calidad del análisis de las gráficas (19 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños. Se ve en el informe.
- Calcula el factor de crecimiento al duplicar n (500 a 1000) para los dos algoritmos y lo compara con lo esperado.

**Lo que puede mejorar:**
- Las cifras del informe no coinciden con su gráfica publicada: en n = 4000 el informe dice 0.314 s para fuerza bruta, pero la curva promedio de la gráfica está cerca de 0.29 s; en n = 1000 dice 0.021 s y la gráfica marca cerca de 0.018 s.
- Con la gráfica, el salto de 500 a 1000 en fuerza bruta se ve cercano a 3 veces, no 2.6. La explicación de por qué no coincide con la teoría ("variaciones del computador") es muy general; probar otro par, como 2000 a 4000, habría dado una lectura más clara.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab2-divide-y-vencer/` con todos los archivos pedidos, y el informe sigue el orden pedido con la gráfica visible.
- Hay instrucciones de reproducción y 4 commits sobre el laboratorio.

**Lo que puede mejorar:**
- Ninguna parte enlaza su código: faltan enlaces a `subarreglo.py` y `pruebas.py` al inicio de la Parte 1, y a `medicion.py` al inicio de la Parte 2.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos soluciones dan siempre la misma suma (también en mis pruebas con listas aleatorias) y `medicion.py` se ejecuta y genera la gráfica.

## Para el próximo laboratorio
- Enlace en el informe cada archivo de código al inicio de la parte donde se usa.
- Explique cada término de la recurrencia y verifique la condición del método maestro, nombrando el caso.
- Copie las cifras del informe desde la gráfica o la tabla que publica, para que coincidan.
- Calcule el factor de crecimiento con varios pares de tamaños y explique con datos las diferencias con la teoría.
- Borre los comentarios de la plantilla (`TODO`) antes de entregar.
