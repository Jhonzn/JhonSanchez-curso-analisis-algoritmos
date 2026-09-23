"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente el algoritmo contando cada comparacion
    # entre dos elementos de la lista.
    
    lista = datos.copy()
    comparaciones = 0

    # Recorre desde el segundo elemento (indice 1) hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]          # elemento que se va a insertar
        j = i - 1                 # ultimo indice de la parte ya ordenada

        # Compara elementos mientras sean menores que 'clave'
        while j >= 0:
            comparaciones += 1

            if lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break

        lista[j + 1] = clave      # inserta 'clave' en su lugar correcto

    return lista, comparaciones

def merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Mezcla dos listas ordenadas en orden descendente. 
        
    No modifica las listas recibidas: construye una nueva lista con los elementos ordenados. 
        
    Args: 
        izquierda: Primera lista ordenada. derecha: Segunda lista ordenada. 
        
    Returns: 
        Una tupla con la lista mezclada y el número total de comparaciones entre elementos 
        realizadas durante el proceso. 
    """
    resultado = []
    i = 0
    j = 0
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente dividir, conquistar y combinar, contando
    # cada comparacion realizada dentro de la mezcla.
    lista = datos.copy()

    if len(lista) <= 1:
        return lista, 0

    mitad = len(lista) // 2

    izquierda, comparaciones_izquierda = merge_sort(lista[:mitad])
    derecha, comparaciones_derecha = merge_sort(lista[mitad:])

    lista, comparaciones_mezcla = merge(izquierda, derecha)

    total_comparaciones = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_mezcla
    )

    return lista, total_comparaciones