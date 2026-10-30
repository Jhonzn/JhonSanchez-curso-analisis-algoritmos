
"""Pruebas para listas enlazadas y tablas hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista_enlazada():
    """Verifica búsquedas exitosas e infructuosas en una lista."""
    lista = ListaEnlazada()

    lista.insertar(100, "en bodega")
    lista.insertar(200, "en reparto")
    lista.insertar(300, "entregado")

    # Búsqueda exitosa
    assert lista.buscar(200) == "en reparto"

    # Búsqueda infructuosa
    assert lista.buscar(999) is None

    print("Pruebas de lista enlazada: OK")


def probar_tabla_hash():
    """Verifica búsquedas exitosas e infructuosas en la tabla."""
    tabla = TablaHash(7)

    tabla.insertar(100, "en bodega")
    tabla.insertar(200, "en reparto")
    tabla.insertar(300, "entregado")

    # Búsqueda exitosa
    assert tabla.buscar(200) == "en reparto"

    # Búsqueda infructuosa
    assert tabla.buscar(999) is None

    print("Pruebas de tabla hash: OK")


def probar_colisiones():
    """Verifica el encadenamiento de tres guías en una casilla."""
    tabla = TablaHash(7)

    guias = (10, 24, 17)

    for guia in guias:
        tabla.insertar(guia, "en bodega")

    # Las tres guías deben caer en la casilla 3
    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    # Verificar que las tres guías se pueden buscar
    for guia in guias:
        assert tabla.buscar(guia) == "en bodega"

    # Verificar la longitud de la lista de la casilla 3
    assert tabla.casillas[3].tamano == 3

    # Verificar el factor de carga
    assert tabla.factor_carga() == 3 / 7

    print("Pruebas de colisiones: OK")


def probar_colecciones_aleatorias():
    """Compara las búsquedas de ambas estructuras en 20 colecciones."""
    random.seed(42)

    for numero_prueba in range(20):

        lista = ListaEnlazada()
        tabla = TablaHash(17)

        # Generar entre 20 y 50 guías únicas
        cantidad = random.randint(20, 50)

        guias = random.sample(
            range(1_000_000_000, 1_000_001_000),
            cantidad
        )

        # Insertar las mismas guías en ambas estructuras
        for guia in guias:
            estado = random.choice([
                "en bodega",
                "en reparto",
                "entregado"
            ])

            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # Comparar búsquedas de guías existentes
        for guia in guias:
            resultado_lista = lista.buscar(guia)
            resultado_tabla = tabla.buscar(guia)

            assert resultado_lista == resultado_tabla
            assert resultado_lista is not None

        # Generar guías inexistentes
        inexistentes = random.sample(
            range(1_500_000_000, 1_500_001_000),
            10
        )

        # Comparar búsquedas infructuosas
        for guia in inexistentes:
            resultado_lista = lista.buscar(guia)
            resultado_tabla = tabla.buscar(guia)

            assert resultado_lista == resultado_tabla
            assert resultado_lista is None

    print("Pruebas aleatorias (20 colecciones): OK")


def ejecutar_pruebas():
    """Ejecuta todas las pruebas del proyecto."""
    probar_lista_enlazada()
    probar_tabla_hash()
    probar_colisiones()
    probar_colecciones_aleatorias()

    print("\nTodas las pruebas fueron superadas correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
