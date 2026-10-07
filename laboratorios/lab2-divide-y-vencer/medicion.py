"""Medicion de los algoritmos de subarreglo maximo."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta
from subarreglo import subarreglo_maximo


TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000]
NUM_EJECUCIONES = 10
SEMILLA = 42


def generar_datos(tamano: int) -> list[int]:
    """Genera una lista reproducible de variaciones diarias.

    Args:
        tamano: cantidad de elementos de la lista.

    Returns:
        Lista de enteros entre -100 y 100.
    """
    generador = random.Random(SEMILLA)

    return [
        generador.randint(-100, 100)
        for _ in range(tamano)
    ]


def medir_fuerza_bruta(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de fuerza bruta.

    Args:
        valores: lista de valores de entrada.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()

    subarreglo_fuerza_bruta(valores)

    fin = time.perf_counter()

    return fin - inicio


def medir_divide_venceras(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de divide y venceras.

    Args:
        valores: lista de valores de entrada.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()

    subarreglo_maximo(
        valores,
        0,
        len(valores) - 1,
    )

    fin = time.perf_counter()

    return fin - inicio


def calcular_promedio(tiempos: list[float]) -> float:
    """Calcula el promedio de una lista de tiempos.

    Args:
        tiempos: tiempos de ejecucion medidos.

    Returns:
        Tiempo promedio en segundos.
    """
    return sum(tiempos) / len(tiempos)


def ejecutar_experimento() -> None:
    """Ejecuta las mediciones y genera la grafica."""
    mediciones_fuerza = []
    mediciones_divide = []

    promedios_fuerza = []
    promedios_divide = []

    for tamano in TAMANOS:
        valores = generar_datos(tamano)

        # Verificar que ambos algoritmos encuentren
        # la misma suma maxima.
        resultado_fuerza = subarreglo_fuerza_bruta(valores)

        resultado_divide = subarreglo_maximo(
            valores,
            0,
            len(valores) - 1,
        )

        assert resultado_fuerza[2] == resultado_divide[2], (
            f"Resultados diferentes para n={tamano}: "
            f"{resultado_fuerza[2]} != "
            f"{resultado_divide[2]}"
        )

        tiempos_fuerza = []
        tiempos_divide = []

        for ejecucion in range(NUM_EJECUCIONES):
            tiempo_fuerza = medir_fuerza_bruta(valores)
            tiempo_divide = medir_divide_venceras(valores)

            tiempos_fuerza.append(tiempo_fuerza)
            tiempos_divide.append(tiempo_divide)

            print(
                f"n={tamano:5d} | "
                f"ejecucion={ejecucion + 1:2d} | "
                f"fuerza bruta={tiempo_fuerza:.6f} s | "
                f"divide y venceras="
                f"{tiempo_divide:.6f} s"
            )

        promedio_fuerza = calcular_promedio(
            tiempos_fuerza
        )

        promedio_divide = calcular_promedio(
            tiempos_divide
        )

        mediciones_fuerza.append(tiempos_fuerza)
        mediciones_divide.append(tiempos_divide)

        promedios_fuerza.append(promedio_fuerza)
        promedios_divide.append(promedio_divide)

        print(
            f"   PROMEDIO n={tamano}: "
            f"fuerza bruta={promedio_fuerza:.6f} s | "
            f"divide y venceras="
            f"{promedio_divide:.6f} s\n"
        )

    generar_grafica(
        mediciones_fuerza,
        mediciones_divide,
        promedios_fuerza,
        promedios_divide,
    )


def generar_grafica(
    mediciones_fuerza: list[list[float]],
    mediciones_divide: list[list[float]],
    promedios_fuerza: list[float],
    promedios_divide: list[float],
) -> None:
    """Genera la grafica con ejecuciones y promedios.

    Args:
        mediciones_fuerza: tiempos de las diez ejecuciones
            de fuerza bruta para cada tamaño.
        mediciones_divide: tiempos de las diez ejecuciones
            de divide y venceras para cada tamaño.
        promedios_fuerza: tiempos promedio de fuerza bruta.
        promedios_divide: tiempos promedio de divide y venceras.
    """
    carpeta = Path("graficas")
    carpeta.mkdir(exist_ok=True)

    plt.figure(figsize=(11, 7))

    # Mostrar las ejecuciones individuales.
    for indice, tamano in enumerate(TAMANOS):
        plt.plot(
            [tamano] * NUM_EJECUCIONES,
            mediciones_fuerza[indice],
            marker="o",
            linestyle="",
            alpha=0.35,
        )

        plt.plot(
            [tamano] * NUM_EJECUCIONES,
            mediciones_divide[indice],
            marker="x",
            linestyle="",
            alpha=0.35,
        )

    # Curva de promedio de fuerza bruta.
    plt.plot(
        TAMANOS,
        promedios_fuerza,
        marker="o",
        linewidth=3,
        label="Fuerza bruta - promedio",
    )

    # Curva de promedio de divide y venceras.
    plt.plot(
        TAMANOS,
        promedios_divide,
        marker="o",
        linewidth=3,
        label="Divide y venceras - promedio",
    )

    plt.title(
        "Tiempo de ejecucion para 10 ejecuciones "
        "y promedio"
    )

    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        carpeta / "tiempo_vs_n.png",
        dpi=150,
    )

    plt.close()

    print(
        "\nGrafica guardada en: "
        "graficas/tiempo_vs_n.png"
    )


if __name__ == "__main__":
    ejecutar_experimento()