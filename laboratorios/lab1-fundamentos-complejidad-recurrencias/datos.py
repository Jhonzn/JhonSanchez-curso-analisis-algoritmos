import random

"""Generadores de lotes de registros para los escenarios de Tamiza.""" 
  
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]: 
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    # TODO: implemente el escenario A. 

    datos = list(range(1, n + 1))

    random.seed(semilla)
    random.shuffle(datos)

    return datos 
  
  
def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]: 
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """ 
    # TODO: implemente el escenario B. 

    cantidad_ordenada = int(n * 0.98)

    # 98% ya viene ordenado de mayor a menor
    caso_casi_ordenado = list(range(n, n - cantidad_ordenada, -1))

    # 2% de registros nuevos
    nuevos = list(range(n - cantidad_ordenada, 0, -1))

    # Se desordenan los registros nuevos
    random.seed(semilla)
    random.shuffle(nuevos)

    # Se agregan al final
    caso_casi_ordenado.extend(nuevos)

    return caso_casi_ordenado
  
  
def generar_inverso(n: int) -> list[int]: 
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """ 
    # TODO: implemente el escenario C.
    return list(range(1, n + 1))
