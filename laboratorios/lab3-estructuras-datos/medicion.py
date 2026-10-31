
"""Experimentos de rendimiento para listas enlazadas y tablas hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


CANTIDAD_BUSQUEDAS = 200
SEMILLA = 7

CARPETA = Path(__file__).parent
CARPETA_GRAFICAS = CARPETA / "graficas"
CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion."""
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Determina si un numero es primo."""
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Encuentra el numero primo mas cercano al valor recibido."""
    distancia = 0

    while True:
        inferior = numero - distancia
        superior = numero + distancia

        if es_primo(inferior):
            return inferior

        if es_primo(superior):
            return superior

        distancia += 1


def generar_guias(
    cantidad: int,
    semilla: int = SEMILLA
) -> tuple[list[int], list[str]]:
    """Genera guias unicas y sus estados de envio."""
    azar = random.Random(semilla)

    guias = azar.sample(
        range(10**9, 10**10),
        cantidad
    )

    estados = [
        azar.choice([
            "en bodega",
            "en reparto",
            "entregado"
        ])
        for _ in range(cantidad)
    ]

    return guias, estados


def construir_estructuras(
    guias: list[int],
    estados: list[str],
    m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista enlazada y la tabla hash."""
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int]
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados."""
    muestra = guias[:min(100, len(guias))]

    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia)


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int]
) -> float:
    """Mide el tiempo promedio de busqueda en segundos."""
    inicio = time.perf_counter()

    for guia in consultas:
        estructura.buscar(guia)

    fin = time.perf_counter()

    return (fin - inicio) / len(consultas)


def experimento_a() -> tuple[list[int], list[float], list[float]]:
    """Compara los tiempos de busqueda de ambas estructuras."""
    valores_n = [100, 500, 1000, 5000, 20000, 30000]

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in valores_n:
        print(f"\nExperimento A: n = {n}")

        # Generar datos antes de medir.
        guias, estados = generar_guias(n, SEMILLA + n)

        existentes = set(guias)

        consultas = generar_guias_inexistentes(
            existentes,
            CANTIDAD_BUSQUEDAS,
            SEMILLA
        )

        # Elegir un primo cercano a n / 2.
        m = primo_cercano(n // 2)

        # Construir las estructuras fuera del cronometro.
        lista, tabla = construir_estructuras(
            guias,
            estados,
            m
        )

        # Verificar que ambas estructuras sean equivalentes.
        verificar_estructuras(lista, tabla, guias)

        # Medir el promedio de las busquedas fallidas.
        tiempo_lista = medir_busquedas(lista, consultas)
        tiempo_tabla = medir_busquedas(tabla, consultas)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(f"Casillas de la tabla: {m}")
        print(f"Factor de carga: {tabla.factor_carga():.2f}")
        print(
            f"Lista enlazada: "
            f"{tiempo_lista * 1_000_000:.2f} µs/busqueda"
        )
        print(
            f"Tabla hash: "
            f"{tiempo_tabla * 1_000_000:.2f} µs/busqueda"
        )

    return valores_n, tiempos_lista, tiempos_tabla


def graficar_experimento_a(
    valores_n: list[int],
    tiempos_lista: list[float],
    tiempos_tabla: list[float]
) -> None:
    """Genera la grafica de lista enlazada frente a tabla hash."""
    plt.figure(figsize=(10, 6))

    plt.plot(
        valores_n,
        [t * 1_000_000 for t in tiempos_lista],
        marker="o",
        label="Lista enlazada"
    )

    plt.plot(
        valores_n,
        [t * 1_000_000 for t in tiempos_tabla],
        marker="s",
        label="Tabla hash"
    )

    plt.title("Experimento A: Lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo promedio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(
        CARPETA_GRAFICAS / "lista_vs_tabla.png",
        dpi=300
    )
    plt.close()

    print("\nGrafica A guardada correctamente.")


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide el efecto del factor de carga en una tabla hash."""
    n = 20000

    factores_objetivo = [0.5, 1, 4, 10]

    # Generar los mismos datos para todas las tablas.
    guias, estados = generar_guias(n, SEMILLA)

    existentes = set(guias)

    consultas = generar_guias_inexistentes(
        existentes,
        CANTIDAD_BUSQUEDAS,
        SEMILLA
    )

    # Construir una lista de referencia para verificar resultados.
    lista = ListaEnlazada()

    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)

    factores_reales: list[float] = []
    tiempos: list[float] = []

    for alfa in factores_objetivo:
        # Calcular m para aproximarse al factor deseado.
        m = primo_cercano(round(n / alfa))

        # Construir la tabla fuera del cronometro.
        tabla = TablaHash(m)

        for guia, estado in zip(guias, estados):
            tabla.insertar(guia, estado)

        # Verificar que la tabla devuelva los mismos estados.
        verificar_estructuras(lista, tabla, guias)

        factor_real = tabla.factor_carga()

        # Medir exclusivamente las busquedas.
        tiempo = medir_busquedas(tabla, consultas)

        factores_reales.append(factor_real)
        tiempos.append(tiempo)

        print(f"\nExperimento B: alfa = {factor_real:.4f}")
        print(f"Casillas: {m}")
        print(
            f"Tiempo promedio: "
            f"{tiempo * 1_000_000:.2f} µs/busqueda"
        )

    return factores_reales, tiempos


def graficar_experimento_b(
    factores: list[float],
    tiempos: list[float]
) -> None:
    """Genera la grafica del tiempo frente al factor de carga."""
    plt.figure(figsize=(10, 6))

    plt.plot(
        factores,
        [t * 1_000_000 for t in tiempos],
        marker="o",
        label="Tabla hash"
    )

    plt.title("Experimento B: Efecto del factor de carga")
    plt.xlabel("Factor de carga (alfa)")
    plt.ylabel("Tiempo promedio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(
        CARPETA_GRAFICAS / "tiempo_vs_alfa.png",
        dpi=300
    )
    plt.close()

    print("\nGrafica B guardada correctamente.")


def main() -> None:
    """Ejecuta los experimentos y genera las graficas."""
    print("INICIANDO EXPERIMENTOS")

    valores_n, tiempos_lista, tiempos_tabla = experimento_a()

    graficar_experimento_a(
        valores_n,
        tiempos_lista,
        tiempos_tabla
    )

    factores, tiempos = experimento_b()

    graficar_experimento_b(factores, tiempos)

    print("\nTodos los experimentos finalizaron correctamente.")
    print(f"Graficas guardadas en: {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
