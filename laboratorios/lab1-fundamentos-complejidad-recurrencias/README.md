# Laboratorio evaluativo 01 � Fundamentos, complejidad y recurrencias

## 1. Punto 1 — [Analizar el algoritmo antes de comprar hardware]

Muchas veces tendemos a confundir hacer algo bien, algo que dio resultados con la forma en la que se realizó, no se puede negar que casi siempre en nuestra ignorancia no cuestionamos nuestros métodos, al contrario, nos montamos en un pedestal creyendo que somo unos genios, pero en realidad nos falta mucho. Eso pasa con los algoritmos, en este ámbito importa mucho mas la eficiencia que la corrección de una lista o en un caso más práctico ordenar expedientes a mano o cualquier clase de documentación. La eficiencia respecto al tiempo importa mucho porque no siempre vamos a tener las mismas entradas a ordenar, no podemos comparar 50 expedientes con 100.000, son cifras completamente distintas y con esa diferencia, puede pasar de que un algoritmo funcione bien a que funcione, pero se tarde por mucho mas tiempo y no cumpla con los requisitos de negocio. La restricción que el sistema de la plataforma temiza mencionado antes es que anteriormente de trabajaban con 20.000 registros en 4 municipios, actualmente el sistema ya no cumple por la expansión del programa que paso de ser 1.200.000, por ello el sistema ya se desborda en la ventana de 4 horas de 2:00am a 6:00am que tiene de procesamiento. Por esta razón no alcanza a ordenar los registros y les toca trabajar con una lista parcial.
Duplicar el servidor podría reducir considerablemente los tiempos de procesamiento, será un efecto placebo muy reconfortante porque aportará procesamiento a un algoritmo que de por sí ya no cumple con la eficiencia respecto al tiempo requerido, puesto que llevan 3 días sin entregar una lista completa ordenada, pero ahí está la trampa, el sistema mejorará y todo, pero cuando haya más registros, si estos se duplican, el trabajo podría aumentar aproximadamente cuatro veces, y si se triplican, hasta nueve veces, haciendo que el sistema vuelva a quedar por fuera del tiempo disponible para procesar los registros diarios. Esta no es una solución viable en todo el sentido de la palabra, en el sentido de la eficiencia energética y también a largo plazo.
Una empresa que trabaja con pedidos necesita organizar los realizados durante el día. Si tiene 50 pedidos, un método poco eficiente puede funcionar de manera correcta y terminar el proceso en poco tiempo respecto a la necesidad de la operación. Sin embargo, si la empresa empieza a crecer y comienza a recibir 100.000 pedidos diarios, el mismo método puede tardar más tiempo o incluso no terminar dentro del tiempo disponible. Aunque el algoritmo siga cumpliendo el objetivo correctamente de los pedidos, deja de ser útil porque no cumple con los tiempos requeridos. En este caso, aumentar la capacidad del servidor podría reducir temporalmente el tiempo de ejecución, pero no solucionaría el problema de fondo si el algoritmo tiene una complejidad elevada. Lo adecuado sería buscar un algoritmo más eficiente que pueda manejar el crecimiento de los datos sin que el tiempo de procesamiento aumente de forma excesiva.

---

## 2. Punto 2 — [Responsabilidad ambiental y ética de la implementación]

El tiempo de ejecución en el proceso nocturno sí afecta mucho y podría aumentar en el futuro, puesto que, al haber cada vez más registros, esto significaría más procesamiento por parte del servidor. Si sumamos el hecho de que no se le va a hacer un análisis detallado al algoritmo empleado para este proceso, porque funciona bien y la única solución más sencilla es sumar capacidad de procesamiento para este proceso, vemos que esto requiere un mayor consumo energético por los nuevos recursos que tiene el servidor y aún más con el aumento de los registros, lo que supone un mayor consumo a largo plazo. Por ello, la forma más viable es atacar el problema de raíz: el algoritmo, y establecer uno mejor.
La primera forma en la que la lentitud o una falla en el sistema podría perjudicar a alguien, alguien que tenga serios problemas cardiovasculares y que los datos se carguen directamente desde el portal web, es decir que estén desordenados los registros. Este caso con un sistema lento perjudicaría mucho a un usuario con alto riesgo, porque en este contexto un/a paciente podría presentar problemas del corazón que pongan en riesgo su vida y el sistema apenas estaría ordenando los registros de acuerdo con el riesgo. El costo lo asumiría el equipo de desarrollo porque son los encargados de automatizar este proceso tan importante en la empresa. La segunda manera es que el sistema no alcance a organizar las pruebas en orden de riesgo y que use esa lista como base para el proceso y que no haya una prioridad a la hora de atender a los pacientes y por lo tanto se descuiden otros pacientes que tienen mas riesgo por el algoritmo tan ineficiente, en este caso el costo lo asumiría la secretaria por la mala metodología que se implementa a la hora de hacer las llamadas.
La obligación adicional aparte del tiempo es la reputación que se puede ganar o perder ya dependiendo del servicio, porque expone la salud de las personas que corren el riesgo de tener problemas del corazón que les pueda costar la vida. Esto no lleva a que el tiempo de procesamiento no es solo un capricho, esto define que perciben por algo que hace un equipo de desarrollo, ejemplo: si yo voy a un ecommerce a realizar una compra online, la pagina le falla de alguna manera, no carga, no procesa la compra, miles de cosas pueden pasar, lo que genera desconfianza entre los usuarios. El criterio del orden importa mucho, no es justo que alguien tenga menos riesgo que otro pueda ser priorizado después de otra persona que no tiene tanto riesgo de perder la vida. Si se contacta primero a alguien que tiene menos riesgo a alguien que tiene bastantes problemas, como consecuencia, sea contactado después. Por lo tanto, la eficiencia es importante para procesar todos los registros dentro del tiempo disponible, pero la corrección es fundamental para garantizar que la priorización sea justa y segura para los pacientes.

---

## 3. Punto 3 — [Peor caso, mejor caso y caso promedio, demostrados en Python]

### 3.1 [Explicación de los 3 casos]

| **Escenario**         | **Canal de origen**                                    | **Cómo llega el lote de registros**                                                                                                                            |
| --------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A — Aleatorio**     | Cargue directo desde el portal web de los laboratorios | Los registros quedan en el orden en que cada laboratorio los subió: sin ninguna relación con el índice de riesgo.                                              |
| **B — Casi ordenado** | Reproceso sobre la lista del día anterior              | El 98 % del lote es la lista de ayer, que ya quedó ordenada por riesgo; el 2 % restante son los resultados nuevos del día, que se anexan al final sin ordenar. |
| **C — Orden inverso** | Migración desde el sistema legado de historia clínica  | El sistema anterior exporta los registros del índice de riesgo **menor al mayor**, es decir, exactamente al revés de lo que Tamiza necesita.                   |

Cuando hablamos de algoritmos siempre ahí que estimar de que base partimos para el desarrollo de una tarea, esto nos condiciona a que dependamos de una base sobre la cual se debe trabajar. Así mismo definimos 3 posibilidades cuando se trata de ordenamiento de un que hace un algoritmo siempre el peor caso va a ser el que esta en orden inverso, puesto que le toca mover casi todos y ordenarlos, si es un caso promedio el cual esta de forma aleatoria, no va a estar inverso si no que solo va a estar menos ordenado, si esta casi ordenado, va a tomar menos tiempo porque no va haber la necesidad de ordenar tanto.

Para decidir si el algoritmo de Tamiza puede entrar en producción, utilizaría principalmente el peor caso, debido a que la ventana de cuatro horas es estricta. Aunque el algoritmo pueda funcionar rápidamente en la mayoría de las situaciones, debe garantizar que incluso ante la entrada que genere el mayor costo pueda procesar el lote dentro del tiempo disponible. El caso promedio también se podria utilizar para conocer el comportamiento habitual del sistema pero no garantiza que el algoritmo pueda evidenciar que no supere la ventana tan estricta de 4 horas, como si se podria tener en cuenta en el orden inverso(peor caso).

Para Insertion Sort, mi predicción antes de realizar las mediciones es:
| Escenario             | Situación de los datos                                                 | Predicción        |
| --------------------- | ---------------------------------------------------------------------- | ----------------- |
| **A — Aleatorio**     | Registros sin un orden determinado                                     | **Caso promedio** |
| **B — Casi ordenado** | 98 % ordenado y 2 % nuevo al final                                     | **Mejor caso**    |
| **C — Orden inverso** | Registros ordenados de menor a mayor, cuando se necesita mayor a menor | **Peor caso**     |

### 3.2 [Demostración experimental]

Descripción breve de lo realizado.

---

## 4. Punto 4 — [Nombre del punto]

### 4.1 [Subpunto]

Descripción breve de lo realizado.

### 4.2 [Subpunto]

Descripción breve de lo realizado.

### 4.3 [Subpunto]

Descripción breve de lo realizado.

---

## Tecnologías utilizadas

* [Tecnología 1]
* [Tecnología 2]
* [Tecnología 3]
* [Tecnología 4]

## Requisitos

* [Requisito 1]
* [Requisito 2]
* [Requisito 3]

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Entrar al proyecto
cd [NOMBRE_DEL_PROYECTO]

# Instalar dependencias
[COMANDO]

# Ejecutar
[COMANDO]
```

## Autores

* [Jhon Fernando Sánchez Álvarez]


