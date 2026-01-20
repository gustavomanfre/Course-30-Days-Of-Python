Crear una clase

Para crear una clase necesitamos la clase de palabra clave seguida del nombre y el colon. El nombre de la clase debe ser CamelCase.

# syntax
    class ClassName:
    code goes here

Ejemplo:

    class Person:
    pass
    print(Person)

<__main__.Person object at 0x10804e510>

Vamos a diseccionarlo pieza por pieza:

1. __main__ (El lugar de origen)

Esto le dice a Python dónde está definida esa clase.

    __main__ significa "el script que se está ejecutando actualmente".

    Si hubieras importado la clase desde otro archivo (por ejemplo import modulo_x), diría modulo_x.Person.

    Básicamente dice: "Esta clase vive en este mismo archivo".

2. .Person (El Tipo)

Es el nombre de la Clase (el plano) que usaste para crear este objeto. Python te está diciendo: "Este objeto es del tipo Person".

3. object (La naturaleza)

Te confirma que esto es una instancia (un objeto real creado), no la clase (el plano).

    Nota importante: Para obtener este resultado, el código debió ser print(Person()) (con paréntesis) o crear una variable p = Person() y luego imprimir p. Si solo imprimes print(Person), Python te diría <class '__main__.Person'>.

4. at 0x10804e510 (La dirección de casa)

Esta es la parte más técnica. Es la Dirección de Memoria (RAM).

    0x: Indica que el número que sigue es Hexadecimal (base 16).

    10804e510: Es la ubicación física exacta en la memoria RAM de tu computadora donde Python guardó los datos de este objeto específico.

________________________________________________________________________________________________________
    def mode(self):

        reps_ages = {}
        for edad in self.ages:
            #El método .get() es un seguro de vida:
                #Busca la edad en el diccionario.
                #Si la encuentra, te da el número de repeticiones actual.
                #Si NO la encuentra, en lugar de dar error, te devuelve el valor por defecto que tú pongas después de la coma.
            reps_ages[edad] = reps_ages.get(edad, 0) + 1
        # max(reps_ages), devolvera la clave con el valor mas grande.
        # argumento key= (El "Criterio de Evaluación"):
            #El argumento key es un parámetro que acepta una función. Le dice a max(): 
            #"No compares los elementos directamente; antes de comparar, 
            #pásalos por esta función y compara los resultados que ella te devuelva".
            #Cuando escribes key=reps_ages.get, estás pasando el método .get del diccionario como regla.
        max_key = max(reps_ages, key=reps_ages.get)
        max_value = reps_ages[max_key]

        ¿Qué hace Python internamente en esa línea?

Imagina que reps_ages = {26: 5, 27: 3}:

    Iteración: Python toma la primera llave: 26.
    Transformación: En lugar de usar 26, ejecuta reps_ages.get(26). 
    El resultado es 5. (Python guarda este 5 en una memoria temporal para comparar).
    
    iteración: Toma la segunda llave: 27.
    Transformación: Ejecuta reps_ages.get(27). El resultado es 3.
    Comparación Final: Python compara los resultados transformados: ¿Quién es mayor, 5 o 3?
    Retorno: Como el 5 ganó, max() te devuelve la llave original que produjo ese 5, es decir: 26.
        return {max_key: max_value}


3. La segunda línea: max_value = reps_ages[max_key]

Una vez que max() hizo todo el trabajo sucio y te dio la edad ganadora (max_key), simplemente vas al diccionario y le pides el valor asociado para guardarlo en max_value.

Es mucho más eficiente que hacer un bucle manual porque max() está optimizado a nivel de lenguaje (escrito en C).