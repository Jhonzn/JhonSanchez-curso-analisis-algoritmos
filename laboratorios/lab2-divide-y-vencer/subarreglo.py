"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).
 
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.
 
    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    # TODO: implemente la solucion en Θ(n²): acumule la suma dentro del
    # ciclo en vez de recalcularla desde cero para cada par.
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]

    for inicio in range(len(valores)):
        suma_actual = 0

        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma
 
 
def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    # TODO: barrido lineal desde el punto medio hacia cada lado.
    suma_izquierda = valores[medio]
    suma_actual = 0
    mejor_inicio = medio

    for indice in range(medio, inicio - 1, -1):
        suma_actual += valores[indice]

        if suma_actual > suma_izquierda:
            suma_izquierda = suma_actual
            mejor_inicio = indice

    suma_derecha = valores[medio + 1]
    suma_actual = 0
    mejor_fin = medio + 1

    for indice in range(medio + 1, fin + 1):
        suma_actual += valores[indice]

        if suma_actual > suma_derecha:
            suma_derecha = suma_actual
            mejor_fin = indice

    return mejor_inicio, mejor_fin, suma_izquierda + suma_derecha
 
 
def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    # TODO: caso base, dos llamadas recursivas, caso cruzado y combinar.
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    mejor_izquierda = subarreglo_maximo(
        valores,
        inicio,
        medio,
    )

    mejor_derecha = subarreglo_maximo(
        valores,
        medio + 1,
        fin,
    )

    mejor_cruzada = suma_cruzada(
        valores,
        inicio,
        medio,
        fin,
    )

    mejor = mejor_izquierda

    if mejor_derecha[2] > mejor[2]:
        mejor = mejor_derecha

    if mejor_cruzada[2] > mejor[2]:
        mejor = mejor_cruzada

    return mejor