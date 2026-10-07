## Autores
* [Jhon Fernando Sánchez Álvarez]

# Laboratorio evaluativo 02 - Dividir y vencer

## 1. Recurrencia y análisis de complejidad

### Recurrencia de `subarreglo_maximo`

El algoritmo `subarreglo_maximo` utiliza la estrategia de **divide y vencerás**. Primero divide el arreglo en dos partes aproximadamente iguales y después resuelve el problema de forma recursiva para cada mitad.

En cada llamada se realizan las siguientes operaciones:

1. Se divide el problema en **dos subproblemas**, uno correspondiente a la mitad izquierda y otro a la mitad derecha.
2. Cada subproblema tiene aproximadamente un tamaño de `n/2`.
3. Se calcula el mejor subarreglo que cruza el punto medio mediante `suma_cruzada`.
4. Finalmente, se comparan los tres resultados obtenidos: el mejor de la izquierda, el mejor de la derecha y el mejor que cruza el punto medio.

La función `suma_cruzada` recorre la mitad izquierda desde el punto medio hacia el inicio y la mitad derecha desde el punto medio hacia el final. En conjunto, recorre una cantidad de elementos proporcional a `n`, por lo que su costo es:

$$
\Theta(n)
$$

Por lo tanto, la recurrencia del algoritmo es:

$$
T(n)=2T\left(\frac{n}{2}\right)+\Theta(n)
$$

con el caso base:

$$
T(1)=\Theta(1)
$$

### Resolución mediante el método maestro

La forma general del método maestro es:

$$
T(n)=aT\left(\frac{n}{b}\right)+f(n)
$$

Para nuestra recurrencia:

$$
a=2
$$

porque se generan dos subproblemas.

$$
b=2
$$

porque cada subproblema tiene aproximadamente la mitad del tamaño.

Y:

$$
f(n)=\Theta(n)
$$

porque corresponde al trabajo realizado para encontrar el subarreglo que cruza el punto medio.

Calculamos:

$$
n^{\log_b a}
=
n^{\log_2 2}
=
n
$$

Por lo tanto:

$$
f(n)=\Theta(n)
=
\Theta\left(n^{\log_2 2}\right)
$$

Esto corresponde al **caso 2 del método maestro**, ya que:

$$
f(n)=\Theta\left(n^{\log_b a}\log^k n\right)
$$

con:

$$
k=0
$$

Aplicando el resultado del caso 2:

$$
T(n)=\Theta\left(n^{\log_b a}\log^{k+1}n\right)
$$

Entonces:

$$
T(n)=\Theta(n\log n)
$$

Por lo tanto, la complejidad temporal de `subarreglo_maximo` es:

$$
\boxed{\Theta(n\log n)}
$$

### Complejidad de la fuerza bruta

El algoritmo `subarreglo_fuerza_bruta` utiliza dos ciclos anidados. El ciclo exterior recorre las posiciones iniciales del subarreglo y el ciclo interior extiende el subarreglo desde esa posición.

La cantidad de iteraciones puede expresarse como:

$$
n+(n-1)+(n-2)+\cdots+1
$$

Esta suma corresponde a:

$$
\frac{n(n+1)}{2}
$$

que pertenece a:

$$
\Theta(n^2)
$$

Dentro del ciclo interno se utiliza una suma acumulada:

```python
suma_actual += valores[fin]
```

Esto es importante porque permite que cada iteración tenga un costo constante, $$\Theta(1)$$, en lugar de volver a calcular la suma completa de cada subarreglo.

Por esta razón, la complejidad de la fuerza bruta es:


$$
\boxed{\Theta(n^2)}
$$


### Comparación de los algoritmos

| Algoritmo | Análisis | Complejidad |
|---|---|---|
| Fuerza bruta | Dos ciclos anidados | $$\Theta(n^2)$$ |
| Divide y vencerás | $$2T(n/2)+\Theta(n)$$ | $$\Theta(n\log n)$$ |

En conclusión, el algoritmo de **divide y vencerás** tiene una menor complejidad asintótica que la solución por fuerza bruta. Esto se debe a que divide el problema en dos partes y realiza un recorrido lineal adicional para encontrar el mejor subarreglo que cruza el punto medio, obteniendo una complejidad de $$\Theta(n\log n)$$, frente a $$\Theta(n^2)$$ de la fuerza bruta.
