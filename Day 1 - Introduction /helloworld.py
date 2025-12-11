#El operador para realizar comentarios es el siguiente #

# Introduction
# Day 1 - 30DaysOfPython Challenge


#Operadores Matematicos


print(3+2)      #Sumatoria (+) -> Imprime 5
print(3-2)      #Resta (-) -> Imprime 1
print(3*2)      #Multiplication (*)-> Imprime 6
print(3/2)      #Division Punto Floatante (2) -> 
print(3**2)     #Exponential (**)
print(3%2)      #Modulus (%)
print (3//2)    #División Entera(//)

#Funcion print(), es una función incorporada (built-in) utilizada para mostrar o imprimir valores en la consola o en una salida estándar.

#Python Tipo de Datos Primitivos.
#Python es un lenguaje de tipo dinámico; por lo tanto, no necesitamos especificar el tipo de la variable mientras la declaramos. Cualquier valor que asignemos a la variable en función de ese tipo de datos se asignará automáticamente.
"""
Python Tipo de Datos Primitivos.
├── Numbers
│   ├── Int (20)
│   ├── Float (35.75)
│   └── complex (1+3j)
├── Bool (True, False)
├── Set ({2, 4, 6})
├── Dict ({1:'a', 2:'b'})
└── Sequence
    ├── String ('Jessa')
    ├── List ([2, 'a', 5.7])
    └── Tuple ((3, 4.5, 'b'))
"""

#Comprobacion de Tipo de Datos

#Numbers
print(type(10))                  # Int : tipo de datos int para representar valores enteros completos. La principal característica del tipo de dato int en Python es que, a diferencia de muchos otros lenguajes de programación (como C, C++ o Java, donde los enteros tienen límites fijos de 32 o 64 bits), los enteros en Python 3 no tienen un límite de tamaño fijo.
id = int(25)                        # Tambien podemos crear una variable entera de la siguiente forma: Usando un int()Clase.
print(type(3.14))                # Float: tipo de datos para representar valores de punto flotante o valores decimales.
num = float(54.75)                  # Tambien podemos crear una variable entera de la siguiente forma: Usando un float()Clase.
print(type(1 + 3j))              # Complex: tipos de datos Complex para representar número complejo es un número con un componente real e imaginario representado como a+bj¿Dónde ay bContienen enteros o valores de punto flotante.

#Sequence
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List: La lista de Python es una colección ordenada (también conocida como una secuencia) de elementos. Los indice 
                                    #ORDENADO: Cada elemento tiene un valor de índice único. Los nuevos elementos se añadirán al final de la lista. 
                                        #El primer elemento siempre tiene el índice 0. lista[i] donde i≥0.
                                        #El último elemento siempre tiene el índice -1. lista[-i] donde i≥1.
                                    #HETEROGÉNEO: La lista pueden contener elementos tipos Numéricos (int, float,complex), tipo de texto (str), Tipo Booleano (bool), tipos de Secuencia (list, tuple, range), tipos de mapeo(dict) ipos de Conjunto(set, frozenset).
                                    #DUPLICADOS: La lista pueden tener dos elementos con los mismos valores.
                                    #MUTABLE: Los elementos de la lista pueden ser modificados. Podemos añadir o eliminar elementos a la lista después de que se haya creado.
print(type((9.8, 3.14, 2.7)))    # Tuple: Las tuplas son colecciones ordenadas de elementos que no son cambiables. El tuple Es lo mismo que el list, excepto que la tupla es inmutable significa que no podemos modificar la tupla una vez creada.

#Dict
print(type({'name':'Asabeneh'})) # Dictionary: Los diccionarios son colecciones no ordenadas de valores únicos almacenados en pares (Key-Value). Utilice un tipo de datos de diccionario para almacenar datos como un par clave-valor.

#Set
print(type({9.8, 3.14, 2.7}))    # Set:  un conjunto es una colección no ordenada de elementos de datos que son únicos. En otras palabras, Python Set es una colección de elementos (o objetos) que no contiene elementos duplicados.

#Boll
print(type(3 == 3))              # Bool: para representar valores booleanos ( Truey False) utilizamos el boolTipo de datos. Los valores booleanos se utilizan para evaluar el valor de la expresión. 
print(type(3 >= 3))              # Bool

#Funcion type() es una función incorporada (built-in), la función devuelve el tipo de datos de la variable
#Funcion isinstance() es una función incorporada (built-in) comprueba si un objeto pertenece a una clase particular.

