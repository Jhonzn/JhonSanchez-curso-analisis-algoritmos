# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Jhon Sánchez Álvarez · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `84b015d`

Buen trabajo: entregó todo lo pedido, con la estructura acordada y resultados que se pueden leer en sus gráficas.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **91 / 100** |
| **Nota (0–5)** | **4.55** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y usa el ejemplo de 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con ventaja y costo de cada uno.
- Justifica que la tabla no sirve para rangos y recomienda tabla hash más árbol equilibrado.
- Declara que los valores a 5.000.000 son una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 solo da la altura y las comparaciones de una búsqueda en el árbol degenerado; no estima cuántas comparaciones cuesta construirlo insertando las 400.000 guías una a una.
  → *Cómo corregirlo:* piense cuántos nodos debe recorrer cada inserción cuando el árbol ya es una "fila", y sume ese costo sobre todas las inserciones; haga lo mismo con el árbol equilibrado y compare.
- En la pregunta 5 la estimación de la lista sale de una sola medición (n = 30.000) y no explica por qué la curva es una recta.
  → *Cómo corregirlo:* apóyese en dos o más puntos de su gráfica y explique por qué, en una búsqueda fallida, el tiempo crece en proporción a n antes de extrapolar. Para la tabla, justifique por qué esperaría un tiempo parecido y qué podría cambiar con tantos datos.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica que la lista cuesta Θ(n) porque hay que revisar todos los nodos.
- Menciona el supuesto de que la función hash reparte las guías de forma pareja.
- Explica que si todas caen en una casilla la tabla se comporta como una lista, Θ(n).

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: búsquedas exitosas e infructuosas correctas, `buscar` con ciclo `while`, la tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren la colisión con m = 7 (casilla 3, longitud 3), `factor_carga() == 3/7` y 20 colecciones aleatorias con guías existentes e inexistentes.
- `estructuras.py` tiene *type hints* y *docstrings* con `Args` y `Returns`.

**Lo que puede mejorar (y cómo corregirlo):**
- Las funciones de `medicion.py` tienen *docstring* de una línea, sin `Args` ni `Returns`.
  → *Cómo corregirlo:* agregue a cada función las secciones `Args:` y `Returns:` al estilo Google, como en `estructuras.py`.
- Las pruebas aleatorias usan siempre la misma tabla de 17 casillas; sería más completo variar `m`.
  → *Cómo corregirlo:* cree la tabla con un `m` distinto en cada colección.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene 6 valores de n con las dos curvas en los mismos ejes y la segunda 4 valores de α.
- Calcula el factor de crecimiento de la lista entre 5.000 y 20.000 guías (≈3,5 veces, frente a 4 de n) y de la tabla (≈1,65 veces) y los relaciona con Θ(n) y Θ(1).
- Describe que el tiempo sube con α y lo relaciona con Θ(1 + α).

**Lo que puede mejorar (y cómo corregirlo):**
- En la gráfica A la tabla pasa de unos 0,79 µs en n = 20.000 a 0,45 µs en n = 30.000, y el informe no lo comenta aunque afirma que la tabla es casi constante.
  → *Cómo corregirlo:* comente esa bajada como ruido de medición y diga cómo la reduciría (por ejemplo, repitiendo la medición varias veces y promediando).
- En la gráfica B el primer punto (α ≈ 0,5) está por encima del segundo (α ≈ 1) y el informe lo llama "ligera variación" sin explicarlo.
  → *Cómo corregirlo:* explique si es ruido y compare el crecimiento entre α = 4 y α = 10 con lo que predice Θ(1 + α).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta `laboratorios/lab3-estructuras-datos/` correcta, con todos los archivos y las dos gráficas.
- El `README.md` tiene su nombre, instrucciones de reproducción, el orden pedido, enlaces al código en cada parte y gráficas incrustadas con ruta relativa que funciona.
- Hay seis commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan todas y la medición corre sin errores y genera las dos gráficas. Lista y tabla devuelven los mismos resultados.
