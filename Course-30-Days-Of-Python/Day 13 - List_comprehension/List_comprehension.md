Listas por Comprension

#Filtre solo negativo y cero en la lista usando la comprensión de la lista
numbers = [-4,-3,-2,-1,0,2,4,6]

positive_numbers = [i for i in numbers if i >= 0 ]
print(positive_numbers)

Para entenderlo mejor, piensa en la comprensión de listas como una frase con tres partes:

[Resultado      Bucle       Condicion]

Desglose de [i for i in numbers if i >= 0]

    -for i in numbers: Es el motor. Recorre la lista numbers y en cada vuelta llama al elemento actual i.

    -if i >= 0: Es el filtro. Si la condición se cumple, pasamos a la siguiente parte.

    -La primera i: Es lo que finalmente se escribe en la nueva lista.

¿Para qué sirve esa primera i si puedo cambiarla?

Esa i es donde puedes transformar el dato antes de que llegue a la lista final. Por ejemplo:

    Si quieres elevarlos al cuadrado: [i**2 for i in numbers if i >= 0]

        Resultado: [0, 4, 16, 36]

    Si quieres convertirlos a texto: [str(i) for i in numbers if i >= 0]

        Resultado: ['0', '2', '4', '6']

    Si quieres un valor fijo (como "OK"): ["OK" for i in numbers if i >= 0]

        Resultado: ['OK', 'OK', 'OK', 'OK']

_______________________________________________________________________________________________________________

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for sublist_externa in list_of_lists for sublist_interna in sublist_externa for number in sublist_interna]

flattened_list = []
for sublist_externa in list_of_lists:        # Nivel 1: saca [[1, 2, 3]]
    for sublist_interna in sublist_externa:  # Nivel 2: saca [1, 2, 3]
        for number in sublist_interna:       # Nivel 3: saca 1, luego 2...
            flattened_list.append(number)    # Guarda el resultado

La lógica de la Comprensión de Listas

En Python, la regla de oro para las comprensiones anidadas es: 
El orden de los for en la línea única es el mismo orden en que aparecen en el código tradicional (de arriba hacia abajo).

    number: Es lo que queremos al final. Siempre va al principio de todo.
    for sublist_externa in list_of_lists: Es el primer nivel (las cajas grandes).
    for sublist_interna in sublist_externa: Es el segundo nivel (las cajas medianas).
    for number in sublist_interna: Es el nivel final donde están los números sueltos.

¿Cómo recordarlo siempre?

Imagina que estás entrando en una casa:

    Primero pasas por la Puerta Principal (for sub1 in total).
    Luego entras a una Habitación (for sub2 in sub1).
    Luego abres un Cajón (for item in sub2).
    Y finalmente agarras el Objeto (item).

_______________________________________________________________________________________________________________