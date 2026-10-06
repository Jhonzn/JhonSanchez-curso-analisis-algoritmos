
"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos y desordenados.
    """
    datos = list(range(1, n + 1))

    random.seed(semilla)
    random.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado (escenario B).

    El lote contiene aproximadamente un 98 % de registros ya ordenados
    de mayor a menor y un 2 % de registros nuevos, con valores de riesgo
    variados, agregados al final sin ordenar.

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98 % ordenado y el 2 % restante agregado al final sin ordenar.
    """
    cantidad_ordenada = int(n * 0.98)
    cantidad_nuevos = n - cantidad_ordenada

    # Registros que ya estaban ordenados de mayor a menor.
    caso_casi_ordenado = list(
        range(n, cantidad_nuevos, -1)
    )

    # Registros nuevos con valores de riesgo variados.
    nuevos = list(range(1, n + 1))

    random.seed(semilla)
    random.shuffle(nuevos)

    # Se seleccionan los registros nuevos y se agregan al final.
    nuevos = nuevos[:cantidad_nuevos]

    caso_casi_ordenado = caso_casi_ordenado[:cantidad_ordenada]
    caso_casi_ordenado.extend(nuevos)

    return caso_casi_ordenado


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: Cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(1, n + 1))
