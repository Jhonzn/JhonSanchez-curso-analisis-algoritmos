"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    # TODO: implemente la lógica usando if / elif / else.
    
    if anio % 400 == 0:
        return True
    elif anio % 4 == 0 and not anio % 100 == 0:
        return True
    else:
        return False
            
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    # TODO: implemente la lectura y validación.
    anios = input("Por favor ingrese los años que desee saber si son bisiestos (2001, 2032, ...): ")

    bisiestos = []
    no_bisiestos = []

    try:
        lista_anios = anios.split(",")

        for i in lista_anios:
            anio = int(i)

            if es_bisiesto(anio):
                bisiestos.append(anio)
            else:
                no_bisiestos.append(anio)
        
        print("Años ingresados:", lista_anios)
        print("Años bisiestos:", bisiestos)
        print("Años no bisiestos:", no_bisiestos)
        print("Cantidad de años bisiestos:", len(bisiestos), " de ", len(lista_anios))

    except ValueError:
        print("Debe ingresar años separados por comas.")
 
 
def main() -> None:
    """Punto de entrada del script."""
    # TODO: use leer_anios(), filtre los años bisiestos con una
    # comprensión de listas, e imprima un resumen que incluya al menos
    # la lista de años bisiestos y cuántos hay.
    leer_anios()
 
 
if __name__ == "__main__":
    main()