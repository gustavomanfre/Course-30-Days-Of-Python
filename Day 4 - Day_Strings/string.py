
#💻 Ejercicios - Día 4

#1-Concatenar la cadena 'Treinta', 'Días', 'De', 'Python' a una sola cadena, 'Treinta Días de Python'.
print('Treinta'+' '+ 'Días'+ ' '+ 'De'+' '+'Python')

a,b,c,d = 'Treinta', 'Días', 'De', 'Python'
phrase = '{} {} {} {}' .format(a,b,c,d)
print(phrase)

#2- Concatenar la cadena 'Codificación', 'Para', 'Todos' a una sola cadena, 'Codificación para todos'.
print('Codificación'+' '+'Para'+' '+'Todos')
a,b,c = 'Codificación', 'Para', 'Todos'
print(f'{a}+{b}+{c}')


#3- Declarar una variable llamada empresa y asignarla a un valor inicial "Codificación para todos".
empresa = "Codificación para todos"

#4- Imprimir la empresa variable usando print().
print(empresa)

#5- Imprimir la longitud de la cadena de la empresa utilizando el método len() y print().
print(len(empresa))

#6-Cambie todos los caracteres a letras mayúsculas usando el método upper().
print(empresa.upper())

#7-Cambie todos los caracteres a letras minúsculas utilizando el método de la parte inferior ().
print(empresa.lower())

#8- Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Codificación para todos.
#capitalize(): Convierte el primer carácter de la cadena en mayúscula
#title(): Busca los espacios en blanco. Después de cada espacio, la siguiente letra se convierte en mayúscula.
#swapcase(): Es como un interruptor de luz. Si la letra está en "on" (mayúscula), la pasa a "off" (minúscula).


print(empresa.capitalize()) # "Codificación para todos"
print(empresa.title()) #"Codificación Para Todos"
print(empresa.swapcase()) # "cODIFICACION PARA TODOS"

#9- Corte (rebanar) la primera palabra "Codificación" para toda la cadena.
empresa = "Codificación para todos"
i = empresa.find('Codificación')
phrase_slice = empresa[i+len("Codificación")+1: ]
print(phrase_slice)

#En tu código usaste empresa[i+len("Codificación")+1: ]. Si por alguna razón "Codificación" fuera la última palabra de la frase, ese +1 podría darte un error o un string vacío.

'''
FOR CON ENUMERATE (VALOR E INDICE).
A veces necesitas el objeto, pero también saber en qué posición está (el índice).
enumerate() toma tu lista y la convierte en un generador de tuplas. En cada vuelta del bucle, te entrega un par de datos: (índice, valor).

nombres = ["Ana", "Luis"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

'''
phrase = empresa.split(' ')
word = 'Codificación'
resultado = []
for i , w in enumerate(phrase):
    if word != w:
        resultado.append(w)

print(' '.join(resultado))

################################################################################################################################################################################

print(empresa.replace('Codificación',"").strip())

#10- Compruebe si la cadena "Coding For All" contiene una palabra Coding utilizando el índice de método, encontrar u otros métodos.
phrase = "Coding For All"

try:
    phrase.index('Coding')

except ValueError
    print('No se encontro en la frase')


state = True if phrase.find("Coding") != -1 else False

"""
1. La Comparación (phrase.find(...) != -1)
Es una expresión lógica. Su única misión es responder a una pregunta de "sí o no".
    Resultado: Siempre será un Booleano (True o False).
    Uso: Ideal para filtros rápidos o condiciones directas.

2. El Operador Ternario (A if condicion else B)
Es una estructura de decisión. Su misión es elegir entre dos opciones cualesquiera.
    Resultado: Puede ser cualquier cosa (un string, un número, una lista, una función, o un booleano).
    Uso: Cuando quieres transformar el resultado de la comparación en algo más "humano" o útil para tu programa.

"""

#MEJORANDOLO
state = phrase.find("Coding") != -1 

#Solucion

state = "Coding" in phrase

#11- Reemplace la palabra codificación en la cadena 'Codificación para todos' a Python.
phrase = phrase.replace("Coding", "python")
print(f'La frase es {phrase}')

"""
1. El error de Inmutabilidad
En Python, los strings son inmutables. Esto significa que métodos como .replace() no modifican la variable original, sino que crean una copia nueva con el cambio aplicado.
    Lo que pasa en tu código: Python hace el reemplazo en memoria, pero como no guardas ese resultado en ninguna parte, el cambio se "pierde" inmediatamente después de ejecutarse.
    La solución: Debes asignar el resultado de nuevo a la variable phrase o a una nueva.

"""

#12- Cambiar "Python para todos" a "Python para todos" usando el método de reemplazo u otros métodos.

phrase = "Python para todos"
phrase = phrase.replace("todos","todxs")

#13- Dividir la cadena 'Codificación para todos' usando el espacio como el separador (split()) .
phrase = 'Codificación para todos'
print(phrase.split(" "))


#14-"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" dividieron la cadena en la coma.
phrase = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(phrase.split(","))

#15- ¿Cuál es el carácter en el índice 0 en la cadena "Codificación para todos".
phrase = 'Codificación para todos'
print(phrase[0])

#16-¿Cuál es el último índice de la cadena "Codificación para todos"?
phrase = 'Codificación para todos'
print(phrase[len(phrase)-1])

#17-¿Qué carácter está en el índice 10 en la cadena "Codificación para todos".

#18-Crear un acrónimo o una abreviatura para el nombre 'Python For Everyone'.



'''

Crear un acrónimo o una abreviatura para el nombre 'Codificación para todos'.
Utilice el índice para determinar la posición de la primera ocurrencia de C en Codificación para todos.
Utilice el índice para determinar la posición de la primera ocurrencia de F en la codificación para todos.
Utilice rfind para determinar la posición de la última ocurrencia de l en Codificación para todas las personas.
Use el índice o encuentre la posición de la primera aparición de la palabra "porque" en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"
Utilice ridsex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"
Cortar la frase 'porque porque' en la siguiente oración: 'No se puede terminar una oración con porque porque es una conjunción'
Encuentre la posición de la primera aparición de la palabra "porque" en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"
Cortar la frase 'porque porque' en la siguiente oración: 'No se puede terminar una oración con porque porque es una conjunción'
¿'Coding For All' comienza con una subcadena de codificación?
¿La 'codificación para todos' termina con una codificación de subcadena?
' Codificación para todos ' , retire los espacios de arrastre izquierdo y derecho en la cuerda dada.
¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():

    30DaysOfPython
    treinta_días_de_python

La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Botella', 'Pyramid', 'Falcon']. Únete a la lista con un hash con la cadena espacial.
Utilice la nueva secuencia de escape de línea para separar las siguientes oraciones.

I am enjoying this challenge.
I just wonder what is next.

Utilice una secuencia de escape de pestañas para escribir las siguientes líneas.

Name      Age     Country   City
Asabeneh  250     Finland   Helsinki

    Utilice el método de formato de cadena para mostrar lo siguiente:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

    Haga lo siguiente usando métodos de formato de cadena:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

'''