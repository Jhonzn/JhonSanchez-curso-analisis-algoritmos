lista = [1, 2, 3, 4, 5]
def calcular_promedio(lista: list) -> float:
    """Determina el promedio de una lista de numeros.
 
    Args:
        lista: lista a calcular el promedio.
 
    Returns:
        El promedio de la lista como número flotante.
    """
    s = 0
    for x in lista:
        s = s + x
    return s / len(lista)


def main() -> None:
    """Punto de entrada del script."""
    print(calcular_promedio(lista))
 
 
if __name__ == "__main__":
    main()

