Lo que sucede es que en Python el operador in es polimórfico, lo que significa que sabe adaptarse al tipo de dato con el que está trabajando.

Aquí te explico cómo funciona in cuando lo usas con strings comparado con listas.
1. in en Strings (Búsqueda de subcadenas)

Cuando usas 'land' in country, Python trata al string como una secuencia de caracteres. El operador busca si esa secuencia exacta de letras existe en algún lugar del texto, sin importar si es al principio, al medio o al final.

    Es como un escáner: Python recorre el string country buscando la coincidencia 'l' -> 'a' -> 'n' -> 'd'.

    Ejemplo: En 'Finland', lo encuentra al final. En 'Iceland', en el medio.

2. Diferencia: Listas vs. Strings

Es muy importante entender que, aunque usan la misma palabra, la "regla" de búsqueda cambia:
Contexto,Ejemplo,¿Qué busca?
En Lista,"'land' in ['Finland', 'land']",Busca un elemento idéntico en la lista.
En String,'land' in 'Finland',Busca una parte del texto (subcadena).

Cuidado: Si haces 'land' in ['Finland'] (una lista con un solo elemento), el resultado será False, porque el texto 'land' no es igual al elemento 'Finland'. Pero si haces 'land' in 'Finland', es True.

Es genial que hayas notado esa diferencia. Lo que sucede es que en Python el operador in es polimórfico, lo que significa que sabe adaptarse al tipo de dato con el que está trabajando.

Aquí te explico cómo funciona in cuando lo usas con strings comparado con listas.
1. in en Strings (Búsqueda de subcadenas)

Cuando usas 'land' in country, Python trata al string como una secuencia de caracteres. El operador busca si esa secuencia exacta de letras existe en algún lugar del texto, sin importar si es al principio, al medio o al final.

    Es como un escáner: Python recorre el string country buscando la coincidencia 'l' -> 'a' -> 'n' -> 'd'.

    Ejemplo: En 'Finland', lo encuentra al final. En 'Iceland', en el medio.

2. Diferencia: Listas vs. Strings

Es muy importante entender que, aunque usan la misma palabra, la "regla" de búsqueda cambia:
Contexto	Ejemplo	¿Qué busca?
En Lista	'land' in ['Finland', 'land']	Busca un elemento idéntico en la lista.
En String	'land' in 'Finland'	Busca una parte del texto (subcadena).

    Cuidado: Si haces 'land' in ['Finland'] (una lista con un solo elemento), el resultado será False, porque el texto 'land' no es igual al elemento 'Finland'. Pero si haces 'land' in 'Finland', es True.

3. ¿Qué pasa en la Memoria?

Cuando el procesador ejecuta if 'land' in country:

    Se cargan ambos strings en la memoria caché.

    El intérprete de Python utiliza un algoritmo de búsqueda de patrones (muy optimizado, similar al algoritmo Boyer-Moore) que compara los bytes de los caracteres.

    Si encuentra la secuencia, devuelve inmediatamente un valor booleano True al Stack.

¿Por qué es mejor que .find()?

Como vimos en tu código anterior, find() te devuelve la posición (-1, 0, 5, etc.).

    find() es como preguntar: "¿En qué número de calle vive land?".

    in es como preguntar: "¿Vive land en esta ciudad?".

Para un if, solo necesitamos saber si "vive" ahí (Sí/No), por lo que in es más directo y rápido para el procesador.
Un pequeño truco extra

También puedes usarlo para validar que un carácter sea una vocal de forma muy limpia:
Python

if letra.lower() in 'aeiou':
    print("Es una vocal")
_________________________________________________________________________________________________________________________________________________________________________

El range() con valores negativos puede parecer confuso al principio porque estamos acostumbrados a contar hacia adelante, pero en Python es la herramienta estándar para contar hacia atrás o recorrer estructuras de datos desde el final.

Para que funcione, el range necesita tres argumentos: range(inicio, fin, paso).

1. La anatomía del range negativo

Cuando el paso (step) es negativo, las reglas cambian:

    Inicio: Debe ser mayor que el fin.

    Fin: Es el límite donde se detiene (este número no se incluye).

    Paso: Es un número negativo (ej. -1) que indica cuánto restamos en cada vuelta.

Ejemplo simple:
# Queremos contar de 3 a 1
for i in range(3, 0, -1):
    print(i)
# Salida: 3, 2, 1

2. ¿Por qué el fin es 0 si quiero llegar al 1?

Recuerda que Python siempre se detiene un paso antes del límite.

    En un rango positivo range(0, 3), se detiene en el 2.

    En un rango negativo range(3, 0, -1), se detiene en el 1.

Si quieres llegar hasta el cero, tienes que poner el límite en -1: range(10, -1, -1) → Cuenta del 10 al 0.

3. Uso práctico: Invertir una lista por índice

Este es el uso más común. Si tienes una lista de 4 elementos, sus índices son 0, 1, 2, 3. Para recorrerla al revés, necesitas los índices 3, 2, 1, 0.
fruits = ['banano', 'naranja', 'mango', 'limón']
ultimo_indice = len(fruits) - 1  # Esto es 3

for i in range(ultimo_indice, -1, -1):
    print(fruits[i])

4. ¿Qué pasa en la Memoria?

A diferencia de crear una lista nueva, el objeto range(10, -1, -1) no ocupa espacio para todos los números en el Heap.

    Solo guarda en el Stack tres valores: start=10, stop=-1, step=-1.

    Cada vez que el bucle le pide el siguiente número, el objeto hace la resta en el momento y te entrega el resultado. Es extremadamente eficiente.

El error más común

Si escribes range(0, 10, -1), Python no te dará un error, pero no hará nada. ¿Por qué? 
Porque le estás diciendo: "Empieza en 0 y resta 1 hasta llegar a 10". 
Como 0 ya es menor que 10, Python decide que no hay nada que hacer y el bucle nunca empieza.
_________________________________________________________________________________________________________________________________________________________________________
Para entenderlo, imagina que invert_fruits es una pila de platos o una fila donde siempre dejas colar al nuevo al principio de todo.

fruits = ['banano', 'naranja', 'mango', 'limón']
invert_fruits = []

for fruit in fruits:
    invert_fruits.insert(0, fruit)

print(invert_fruits)

1. Estado Inicial
    fruits: ['banano', 'naranja', 'mango', 'limón']
    invert_fruits: [] (Vacía)

2. Vuelta 1: Entra 'banano'
El código dice: invert_fruits.insert(0, 'banano').
    Traducción: "Pon 'banano' en la posición 0 (al frente)".
    Estado de la lista: ['banano']

3. Vuelta 2: Entra 'naranja'
El código dice: invert_fruits.insert(0, 'naranja').
    Traducción: "Pon 'naranja' en la posición 0".
    ¿Qué pasa con 'banano'?: Como 'naranja' se puso adelante, empuja a 'banano' a la derecha (a la posición 1).
    Estado de la lista: ['naranja', 'banano']

4. Vuelta 3: Entra 'mango'
El código dice: invert_fruits.insert(0, 'mango').
    Traducción: "Pon 'mango' adelante de todos".
    Resultado: Empuja a 'naranja' y a 'banano' hacia atrás.
    Estado de la lista: ['mango', 'naranja', 'banano']

5. Vuelta 4: Entra 'limón'
El código dice: invert_fruits.insert(0, 'limón').
    Traducción: "¡'Limón' va primero!".
    Resultado Final: Todos se mueven un lugar más.
    Estado de la lista: ['limón', 'mango', 'naranja', 'banano']

Analogía de la vida real
Imagina una pila de papeles en un escritorio.
    Pones el papel "Banano" sobre la mesa.
    Luego pones el papel "Naranja" encima del anterior.
    Luego "Mango" encima.
    Luego "Limón" encima.

Si ahora lees la pila desde arriba (índice 0), el orden es: Limón -> Mango -> Naranja -> Banano. ¡Justo al revés de como llegaron!
    