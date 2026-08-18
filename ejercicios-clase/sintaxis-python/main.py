print("Hola, mundo")

# Declaración de variables

n = 15656
print(type(n))
tiempo = 0.0034
print(type(tiempo))
algoritmo = "algoritmo de ordenamiento"
print(type(algoritmo))
ordenado = True
print(type(ordenado))           
resultado = None
print(type(resultado))

# Estructuras de control, condicional

if tiempo < 0.001:
    categoria = "rapido"
elif tiempo < 0.01:
    categoria = "moderado"
else:
    categoria = "lento"

# Estructuras ciclicas o repetitivas

for i in (2,15,2):
    print(i)
 
intentos = 0
while intentos < 3:
    intentos = intentos + 1
    print(intentos)

# Funciones

def contar_comparaciones(lista):
    comparaciones = 0
    for i in range(1, len(lista)):
        j = i
        while j > 0 and i < 0:
            print("Mensaje")
    return j

# Estructuras de datos nativas de python
# lista: mutable, ordenada, admite duplicados
numeros = [5, 2, 9, 1]
# tupla: inmutable, ordenada, admite duplicados
punto = (10000, 0.0034)
# diccionario: clave -> valor
tiempos = {10000: 0.0034, 1000: 0.0002}
# conjunto: sin orden, sin duplicados
tamanos_probados = {100, 1000, 10000}

"""quieres construir la lista de los cuadrados de los tamaños de entrada que vas a probar: 
[100, 1000, 10000] → [10000, 1000000, 100000000]."""

tamanos = [100, 1000, 10000]
cuadrados = []
for t in tamanos:
    cuadrados.append(t ** 2)

"""Funciona, pero son cuatro líneas para una idea simple: "el cuadrado de cada elemento". 
Python permite expresar exactamente esa idea en una sola línea, con comprensión de listas:"""

cuadrados = [t ** 2 for t in tamanos]
 
# con filtro: solo los tamanos mayores a 500
grandes = [t for t in tamanos if t > 500]

#Manejo de errores humanos
tiempo_total = 1
repeticiones = 0
try:
    promedio = tiempo_total / repeticiones
except ZeroDivisionError:
    print("No se registraron repeticiones; no se puede promediar.")
    promedio = None
#Importación de librerias
import time
from matplotlib import pyplot as plt
 
inicio = time.time()
# ... código a medir ...
duracion = time.time() - inicio