
1. Diferencia clave: sorted() vs .sort()

sorted(lista): Es una función integrada. No toca la lista original; crea una copia nueva ya ordenada. 
Es más segura si quieres conservar los datos en su orden inicial.

lista.sort(): Es un método de las listas. Modifica la lista original directamente (ordenamiento in-place) y no devuelve nada.

2. Sintaxis básica

La forma más sencilla de usarlo es pasarle solo el objeto que quieres ordenar:
Python

numeros = [5, 2, 8, 1]
numeros_ordenados = sorted(numeros)

print(numeros)           # [5, 2, 8, 1]  <- Sigue igual
print(numeros_ordenados) # [1, 2, 5, 8]  <- Nueva lista

3. Parámetros potentes

sorted() tiene dos argumentos opcionales que lo hacen muy flexible:
    reverse = True: Por defecto, ordena de menor a mayor. Si activas esto, ordena de mayor a menor.
    key: Permite pasar una función para decidir cómo comparar los elementos. Por ejemplo, ordenar palabras por su longitud (len) en lugar de por orden alfabético.

Ejemplo:

# Lista original de nombres
nombres = ["Ana", "Sebastian", "Zoe", "Roberto", "Li"]

# Usamos sorted con los tres elementos:
# 1. La lista: nombres
# 2. key=len: Le dice a Python que use la función len (longitud) para comparar
# 3. reverse=True: Ordena de mayor a menor (descendente)
nombres_ordenados = sorted(nombres, key=len, reverse=True)

print(f"Original: {nombres}")
print(f"Ordenados por longitud (largo a corto): {nombres_ordenados}")

Explicación de los parámetros:

    key=len: Normalmente sorted mira la primera letra ("A" antes que "Z"). Al poner key=len, Python primero mide cada palabra. "Ana" se convierte en 3, "Sebastian" en 9, etc. El orden se basa en esos números.

    reverse=True: Por defecto, sorted va de lo más pequeño a lo más grande (ascendente). Al activar el reverse, invertimos el resultado para que el número más grande (el nombre más largo) sea el primero.

Un ejemplo más avanzado: Ordenar por la "edad" en un diccionario

estudiantes = [
    {'nombre': 'Juan', 'nota': 8},
    {'nombre': 'Maria', 'nota': 10},
    {'nombre': 'Pedro', 'nota': 7}
]

# Ordenamos por la 'nota' de mayor a menor
# Usamos una función "lambda" para decirle: "mira dentro de la clave 'nota'"
top_estudiantes = sorted(estudiantes, key=lambda x: x['nota'], reverse=True)

print(top_estudiantes)
# Resultado: Maria (10), Juan (8), Pedro (7)

# Explicacion Ejemplo
1. La estructura de datos
Tienes una lista llamada estudiantes. Cada elemento dentro de esa lista no es un simple número, sino un diccionario con dos claves: 'nombre' y 'nota'. Si intentaras hacer un sorted(estudiantes) a secas, Python daría error porque no sabe qué comparar: ¿debería comparar los nombres o las notas?

2. El parámetro key y la función lambda
Aquí es donde ocurre la "magia". El parámetro key espera una función que le diga a Python: "De todo este objeto (el diccionario), usa este valor específico para comparar".

    lambda x:: Es una función anónima (sin nombre) muy rápida. La x representa a un solo elemento de la lista (es decir, uno de los diccionarios) mientras Python recorre la lista.
    x['nota']: Le dice a la función: "Toma el diccionario x y extrae el valor que está en la clave 'nota'".

¿Cómo lo ve Python internamente? Imagina que Python crea una lista invisible de "pesos" para decidir el orden:
    Para Juan, extrae el 8.
    Para Maria, extrae el 10.
    Para Pedro, extrae el 7.

3. El parámetro reverse=True
Por defecto, sorted ordena de menor a mayor (7, 8, 10). Al poner reverse=True, le ordenamos a Python que invierta el resultado final para que el valor más alto (la mejor nota) aparezca primero (10, 8, 7).

4. El proceso completo paso a paso
    Entrada: [{'nombre': 'Juan', 'nota': 8}, {'nombre': 'Maria', 'nota': 10}, {'nombre': 'Pedro', 'nota': 7}].
    Extracción (Key): Python mira las notas: 8, 10, 7.
    Ordenamiento: Los ordena según la nota. Gracias al reverse=True, el orden de las notas es 10, luego 8, luego 7.
    Reorganización: Mueve los diccionarios completos a sus nuevas posiciones basadas en ese orden de notas.
    Salida: Una nueva lista donde Maria (10) va primero, Juan (8) segundo y Pedro (7) al final.
=======
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
>>>>>>> b4badcb567a1517f89f83ca97daa919717cc54a2
