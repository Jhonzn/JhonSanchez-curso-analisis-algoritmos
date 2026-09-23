import time
import matplotlib.pyplot as plt

from pathlib import Path
from datos import generar_aleatorio
from algoritmos import insertion_sort, merge_sort

CARPETA = Path(__file__).parent
CARPETA_GRAFICAS = CARPETA / "graficas"

CARPETA_GRAFICAS.mkdir(exist_ok=True)

def main() -> None:
    
    """Punto de entrada del script."""
    
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    
    comparaciones_aleatorio_insertion_sort = []
    comparaciones_aleatorio_merge_sort = []
    
    tiempos_aleatorio_insertion_sort = []
    tiempos_aleatorio_merge_sort = []
    
    for n in tamanos:
        # Generar datos
        aleatorio = generar_aleatorio(n)
        
        # Escenario aleatorio insertion sort
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(aleatorio)
        fin = time.perf_counter()
    
        comparaciones_aleatorio_insertion_sort.append(comparaciones)
        tiempos_aleatorio_insertion_sort.append(fin - inicio)
            
        # Escenario aleatorio merge sort
        inicio = time.perf_counter()
        _, comparaciones = merge_sort(aleatorio)
        fin = time.perf_counter()
                
        comparaciones_aleatorio_merge_sort.append(comparaciones)
        tiempos_aleatorio_merge_sort.append(fin - inicio)
        
    # Mostrar resultados
    print("\nCOMPARACIONES")
    print("-" * 60)
    
    for i, n in enumerate(tamanos):
        print(
            f"n={n}: "
            f"Insertion Sort: "
            f"comparaciones={comparaciones_aleatorio_insertion_sort[i]}, "
            f"tiempo={tiempos_aleatorio_insertion_sort[i]:.6f}s | "
            f"Merge Sort: "
            f"comparaciones={comparaciones_aleatorio_merge_sort[i]}, "
            f"tiempo={tiempos_aleatorio_merge_sort[i]:.6f}s"
        )
        
    # Crear gráfica
    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanos,
        tiempos_aleatorio_insertion_sort,
        marker="o",
        label="Insertion Sort"
    )

    plt.plot(
        tamanos,
        tiempos_aleatorio_merge_sort,
        marker="o",
        label="Merge Sort"
    )

    plt.title("Tiempo de ejecución - Escenario A (Aleatorio)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()