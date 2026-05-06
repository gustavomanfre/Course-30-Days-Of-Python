Set es una colección de elementos distintos NO ORDENADOS y NO INDEXADOS.
En el conjunto de Python se utiliza para almacenar artículos únicos, y es posible encontrar la unión, intersección, diferencia, diferencia simétrica, subconjunto, súper conjunto y conjunto de disjuntos entre los conjuntos.

1. La Regla de Oro: Unicidad
A diferencia de las listas (donde los elementos se apilan uno tras otro en el Heap), los Sets están diseñados para representar conjuntos matemáticos. Un elemento está o no está.
Si haces esto:

it_companies = {'Facebook', 'Google'}
it_companies.add('Facebook') # Ya existe

El tamaño (len) seguirá siendo 2. Python no lanza un error, simplemente no realiza ninguna acción de escritura en la memoria para ese elemento.

2. ¿Qué pasa en la Memoria? (Hashing)

A bajo nivel, los Sets no usan un bloque contiguo de punteros como las listas. Usan una Hash Table (Tabla Hash):
    Cuando intentas agregar 'Facebook', Python calcula su valor Hash (una firma numérica única).
    Busca en la tabla si ya existe esa firma.
    Si la encuentra y el valor es el mismo, aborta la operación.

Por eso los Sets son extremadamente rápidos para comprobar si algo existe (in), pero no permiten duplicados.

Una Tabla Hash es una estructura de memoria diseñada para la velocidad. 
A diferencia de una lista, donde tienes que recorrer elemento por elemento (O(n)), una tabla hash permite encontrar un elemento casi instantáneamente (O(1)).

1. El Array de Slots (Celdas)

En memoria, una tabla hash comienza como un bloque contiguo de "slots" o celdas vacías. Cada celda no guarda el objeto directamente, sino que guarda tres cosas (en CPython):

    El Hash (la firma numérica).

    La Llave (puntero al objeto llave).

    El Valor (puntero al objeto valor, o simplemente el objeto en un Set).

2. El Proceso de Guardado (Paso a Paso)

Imagina que ejecutas it_companies.add('Google'):

    Hashing: Python pasa el string 'Google' por una función hash. Supongamos que el resultado es 54321.

    Cálculo del Índice: Para saber en qué celda meterlo, Python usa el operador módulo con el tamaño de la tabla (ej. 8 celdas):

    54321(mod8)=1.

    Almacenamiento: Python va al índice 1 de la tabla. Si está vacío, guarda ahí el puntero a 'Google'.

3. Gestión de Colisiones

¿Qué pasa si dos palabras diferentes dan el mismo índice? (Ejemplo: 'Apple' también da índice 1). Esto se llama Colisión.

Python usa una técnica llamada Open Addressing (Direccionamiento Abierto):

    Si la celda 1 está ocupada, Python aplica un algoritmo (probeta cuadrática) para buscar "el siguiente lugar disponible" (ej. el índice 4).

    No crea una lista dentro de la celda (eso sería Chaining), sino que busca otro espacio libre en la misma tabla.

4. Administración y Redimensionamiento (Resizing)

Una tabla hash funciona bien solo si tiene espacio vacío. Si la tabla está muy llena, las colisiones aumentan y la velocidad cae.

    Load Factor (Factor de carga): Python mantiene la tabla llena hasta un 66% aproximadamente.

    Resizing: Cuando superas ese límite, Python hace lo siguiente:

        Reserva un nuevo bloque de memoria mucho más grande (normalmente el doble o cuádruple).

        Re-hashea todos los elementos: vuelve a calcular sus índices para la nueva tabla.

        Borra la tabla vieja (Garbage Collection).