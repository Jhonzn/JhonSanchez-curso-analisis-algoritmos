"""Pruebas para los algoritmos de subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta
from subarreglo import subarreglo_maximo


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas del laboratorio."""

    # 1. Serie de ocho dias de la situacion problema.
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == 17
    assert resultado_divide[2] == 17

    # 2. Serie de un solo elemento.
    serie = [7]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == 7
    assert resultado_divide[2] == 7

    # 3. Todos los valores negativos.
    serie = [-8, -3, -10, -2, -7]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == -2
    assert resultado_divide[2] == -2

    # 4. Todos los valores positivos.
    serie = [4, 2, 7, 3, 5]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == 21
    assert resultado_divide[2] == 21

    # 5. Caso donde el mejor tramo cruza el punto medio.
    serie = [-10, 4, 5, -20, 6, 7, -10]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == 13
    assert resultado_divide[2] == 13

    # 6. Listas aleatorias.
    generador = random.Random(42)

    for _ in range(30):
        longitud = generador.randint(1, 30)

        serie = [
            generador.randint(-20, 20)
            for _ in range(longitud)
        ]

        resultado_fuerza = subarreglo_fuerza_bruta(serie)
        resultado_divide = subarreglo_maximo(
            serie,
            0,
            len(serie) - 1,
        )

        assert resultado_fuerza[2] == resultado_divide[2], (
            f"Resultados diferentes para {serie}: "
            f"{resultado_fuerza} != {resultado_divide}"
        )

    print("Todas las pruebas fueron superadas correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()