import time
import matplotlib.pyplot as plt

from pathlib import Path
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso
from algoritmos import insertion_sort

CARPETA = Path(__file__).parent
CARPETA_GRAFICAS = CARPETA / "graficas"

CARPETA_GRAFICAS.mkdir(exist_ok=True)

def main() -> None:
    """Punto de entrada del script."""

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    comparaciones_aleatorio = []
    comparaciones_casi_ordenado = []
    comparaciones_inverso = []

    tiempos_aleatorio = []
    tiempos_casi_ordenado = []
    tiempos_inverso = []

    for n in tamanos:
        # Generar datos
        aleatorio = generar_aleatorio(n)
        casi_ordenado = generar_casi_ordenado(n)
        inverso = generar_inverso(n)

        # Escenario aleatorio
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(aleatorio)
        fin = time.perf_counter()

        comparaciones_aleatorio.append(comparaciones)
        tiempos_aleatorio.append(fin - inicio)

        # Escenario casi ordenado
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(casi_ordenado)
        fin = time.perf_counter()

        comparaciones_casi_ordenado.append(comparaciones)
        tiempos_casi_ordenado.append(fin - inicio)

        # Escenario inverso
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(inverso)
        fin = time.perf_counter()

        comparaciones_inverso.append(comparaciones)
        tiempos_inverso.append(fin - inicio)

    # Mostrar resultados
    print("\nCOMPARACIONES")
    print("-" * 60)

    for i, n in enumerate(tamanos):
        print(
            f"n={n}: "
            f"Aleatorio={comparaciones_aleatorio[i]}, "
            f"Casi ordenado={comparaciones_casi_ordenado[i]}, "
            f"Inverso={comparaciones_inverso[i]}"
        )

    # Crear gráfica de comparaciones
    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanos,
        comparaciones_aleatorio,
        marker="o",
        label="Aleatorio"
    )

    plt.plot(
        tamanos,
        comparaciones_casi_ordenado,
        marker="o",
        label="Casi ordenado"
    )

    plt.plot(
        tamanos,
        comparaciones_inverso,
        marker="o",
        label="Inverso"
    )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel(r"Número de comparaciones ($\times 10^7$)")
    plt.title("Insertion Sort - Comparaciones")
    plt.ticklabel_format(axis="y", style="scientific", scilimits=(0, 0))
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_comparaciones.png", dpi=300)
    plt.close()


    # Crear gráfica de tiempo
    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanos,
        tiempos_aleatorio,
        marker="o",
        label="Aleatorio"
    )

    plt.plot(
        tamanos,
        tiempos_casi_ordenado,
        marker="o",
        label="Casi ordenado"
    )

    plt.plot(
        tamanos,
        tiempos_inverso,
        marker="o",
        label="Inverso"
    )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Insertion Sort - Tiempo de ejecución")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_tiempo.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    main()