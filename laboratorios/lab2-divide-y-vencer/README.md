# Laboratorio evaluativo 02 - Dividir y vencer

## Autores
* [Jhon Fernando Sánchez Álvarez]

## Tecnologías utilizadas

- Python 3.13
- Git y GitHub
- `time.perf_counter()` para la medición de tiempos
- Matplotlib para la generación de gráficas

## Requisitos

- Python 3.13
- Git
- Matplotlib

## Ejecución

### 1. Activar el entorno virtual

Desde la carpeta del repositorio:

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source .venv/Scripts/activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar las pruebas

```bash
cd laboratorios\lab2-divide-y-vencer
```

```bash
python pruebas.py
```

Este script ejecuta las pruebas de los algoritmos de **fuerza bruta** y **divide y vencerás**, incluyendo casos pequeños, valores negativos, valores positivos, un caso que cruza el punto medio y diferentes listas aleatorias.

Si todas las pruebas son correctas, se mostrará:

```text
Todas las pruebas fueron superadas correctamente.
```

### 4. Ejecutar las mediciones

```bash
python medicion.py
```

Este script ejecuta ambos algoritmos sobre diferentes tamaños de entrada, realiza **10 ejecuciones por cada tamaño**, calcula el promedio de los tiempos y verifica que ambos algoritmos obtengan la misma suma máxima.

También genera la gráfica con las mediciones y los promedios.

La gráfica se guarda automáticamente en:

```text
graficas/tiempo_vs_n.png
```

### 5. Desactivar el entorno virtual

```bash
cd ../..
```
```bash
deactivate
```
# Parte 1 — Verificación de las soluciones

Se verificaron las dos soluciones implementadas para encontrar el subarreglo de suma máxima: **fuerza bruta** y **divide y vencerás**.

Las pruebas incluyeron diferentes situaciones para comprobar que ambas soluciones obtienen la misma suma máxima:

- La serie de 8 días planteada en el problema: `[-3, 5, -2, 8, -6, 3, 9, -4]`, cuyo resultado esperado es `17`.
- Una serie con un solo elemento.
- Una serie donde todos los valores son negativos.
- Una serie donde todos los valores son positivos.
- Una serie en la que el subarreglo óptimo cruza el punto medio, para verificar específicamente la función utilizada por divide y vencerás.
- **30 listas generadas aleatoriamente**, utilizando una semilla fija, para comparar los resultados obtenidos por ambos algoritmos.

Las pruebas se realizaron mediante instrucciones `assert`, comparando principalmente la suma máxima obtenida por cada solución. De esta manera se comprobó que ambas implementaciones producen el mismo resultado para los casos evaluados.

Para reproducir las pruebas:

```bash
python pruebas.py
```

Si todas las pruebas son correctas, se muestra el mensaje:

```text
Todas las pruebas fueron superadas correctamente.
```

# Parte 2 — Medición y gráfica

Para comparar el comportamiento de los algoritmos se utilizaron los siguientes tamaños de entrada:

`10, 50, 100, 500, 1000, 2000 y 4000`

Para cada tamaño de entrada, creamos un conjunto de números enteros aleatorios, con valores entre `-100` y `100`. Usamos una semilla fija, la (`42`), para asegurarnos de que la misma lista se aplicara a ambos algoritmos. Esto permitió una comparación justa, ya que las condiciones eran idénticas.

Repetimos cada prueba **10 veces**s. Después, sacamos el tiempo promedio de todas esas ejecuciones. Es importante destacar que solo medimos el tiempo que tardaba el algoritmo en ejecutarse, sin contar el tiempo que llevaba crear los datos.

Además, en cada tamaño se verificó que ambos algoritmos obtuvieran la misma suma máxima antes de registrar los resultados.

La gráfica resultante muestra las ejecuciones realizadas y el promedio de tiempo para cada algoritmo:

![Tiempo de ejecución](graficas/tiempo_vs_n.png)

Los resultados indican que para entradas pequeñas, las diferentes soluciones son muy parecidas, llegando incluso a ser más rápidas las de fuerza bruta por los gastos extra de las llamadas recursivas en divide y vencerás. No obstante, conforme el tamaño de la entrada crece, la diferencia se vuelve mucho más notoria.

Por ejemplo, para `n = 4000`, la fuerza bruta obtuvo un promedio aproximado de **0.314219 s**, mientras que divide y vencerás obtuvo aproximadamente **0.004455 s**.

Los tiempos de cada ejecución se registraron para obtener el promedio mostrado en la gráfica.

# Parte 3 — Análisis de los resultados

## 3.1. Recurrencia y análisis de complejidad

**Divide y vencerás**

Este algoritmo divide la lista en dos mitades, resuelve cada una de forma recursiva y después encuentra el mejor subarreglo que cruza el punto medio. Como este último cálculo recorre los elementos en tiempo lineal, la recurrencia es:

$$
T(n)=2T(n/2)+\Theta(n)
$$

Aplicando el método maestro, con $a=2$, $b=2$ y $f(n)=\Theta(n)$, se obtiene una complejidad de:

$$
T(n)=\Theta(n\log n)
$$

**Fuerza bruta**

Este algoritmo utiliza dos ciclos anidados para probar todos los subarreglos posibles. La cantidad de iteraciones se representa mediante:

$$
n+(n-1)+(n-2)+\cdots+1=\frac{n(n+1)}{2}
$$

Por lo tanto, su complejidad es:

$$
T(n)=\Theta(n^2)
$$

La suma acumulada evita volver a sumar desde cero los elementos de cada subarreglo. En conclusión, divide y vencerás tiene una mejor complejidad para entradas grandes.

## 3.2. Lo medido contra lo esperado

Al comparar los tamaños $n=500$ y $n=1000$, el tiempo de fuerza bruta pasó de $0.008171$ a $0.021248$ segundos, un aumento aproximado de $2.60$ veces. Teóricamente, al duplicar la entrada se esperaría un crecimiento cercano a:

$$
2^2=4
$$

En divide y vencerás, el tiempo pasó de $0.000837$ a $0.001023$ segundos, aproximadamente $1.22$ veces. Para su complejidad $n\log n$, el crecimiento esperado sería cercano a:

$$
\frac{1000\log_2(1000)}{500\log_2(500)}
\approx 2.20
$$

Los resultados no coinciden exactamente con la teoría, posiblemente por las variaciones del computador y el tamaño de las entradas. Aun así, la gráfica muestra que fuerza bruta aumenta sus tiempos más rápidamente que divide y vencerás.

## 3.3. ¿Qué pasa con los tamaños pequeños?

Con $n=10$, fuerza bruta fue ligeramente más rápida. Esto puede ocurrir porque divide y vencerás necesita realizar llamadas recursivas, dividir el problema y calcular el tramo que cruza el punto medio. Cuando hay pocos elementos, ese trabajo adicional influye en el tiempo total.

Sin embargo, para $n=50$ y $n=100$, divide y vencerás ya presentó mejores resultados. La diferencia fue más evidente con $n=4000$: fuerza bruta tardó $0.314219$ segundos, mientras que divide y vencerás tardó $0.004455$ segundos.

Esto demuestra que ambos métodos funcionan con entradas pequeñas, pero divide y vencerás ofrece una ventaja importante cuando aumenta la cantidad de datos.

## 3.4. ¿Cuándo conviene dividir?

Dividir un problema no siempre mejora su rendimiento. Por ejemplo, para encontrar el valor máximo de una lista basta con recorrerla una sola vez y guardar el mayor elemento encontrado. La recurrencia de este método es:

$$
T(n)=T(n-1)+\Theta(1)
$$

Su complejidad es:

$$
T(n)=\Theta(n)
$$

Si se divide la lista en dos mitades y después se comparan sus máximos, la recurrencia sería:

$$
T(n)=2T(n/2)+\Theta(1)
$$

Este enfoque también tiene complejidad lineal:

$$
T(n)=\Theta(n)
$$

Por lo tanto, dividir no mejora la complejidad en este caso y agrega trabajo adicional. Es más conveniente recorrer la lista una sola vez.

## 3.5. Recomendación para la cooperativa

Para encontrar el subarreglo de suma máxima, recomendaría divide y vencerás frente a fuerza bruta, porque las mediciones muestran que funciona mejor cuando aumenta la cantidad de datos.

Tomando como referencia el tiempo registrado para $n=4000$ y extrapolando según la complejidad de cada algoritmo, para un millón de registros se estiman los siguientes tiempos.

Para fuerza bruta:

$$
0.314219\left(\frac{1\,000\,000}{4\,000}\right)^2
\approx 19\,639\text{ s}
$$

Esto equivale aproximadamente a $5.45$ horas.

Para divide y vencerás:

$$
0.004455
\left(
\frac{1\,000\,000\log_2(1\,000\,000)}
{4\,000\log_2(4\,000)}
\right)
\approx 1.85\text{ s}
$$

| Algoritmo | Complejidad | Tiempo estimado |
|---|---|---:|
| Fuerza bruta | $\Theta(n^2)$ | 5.45 horas |
| Divide y vencerás | $\Theta(n\log n)$ | 1.85 segundos |

Estos valores son estimaciones matemáticas, no mediciones reales para un millón de registros. El tiempo efectivo puede variar según el computador y las condiciones de ejecución.

En conclusión, divide y vencerás es la alternativa más conveniente entre las dos evaluadas, especialmente si la cooperativa necesita analizar grandes cantidades de información.

---

## Autores

- Jhon Fernando Sánchez Álvarez
--- 