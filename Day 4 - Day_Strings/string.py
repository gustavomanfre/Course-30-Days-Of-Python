
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

except ValueError:
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
phrase = 'Codificación para todos'
print (phrase[10])

#18-Crear un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
phrase = 'Codificación para todos'
cut_phrase = phrase.split()

acronym = "" # Paso vital: inicializar la variable

for word in cut_phrase:
    acronym += word[0]

print(acronym.upper())

#19-Crear un acrónimo o una abreviatura para el nombre 'Codificación para todos'.
phrase = "Codificación para todos"
cut_phrase = phrase.split()

acronym = "" # Paso vital: inicializar la variable

for word in cut_phrase:
    acronym += word[0]

print(acronym.upper())

#20-Utilice el índice para determinar la posición de la primera ocurrencia de C en Codificación para todos.
phrase = "Codificación para todos"
sub_string = "C"
print(phrase.index(sub_string))

#21- Utilice el índice para determinar la posición de la primera ocurrencia de F en la "Codificación para todos".
phrase = "Codificación para todos"
sub_string = "F"
print(phrase.index(sub_string))

#22-Utilice rfind para determinar la posición de la última ocurrencia de l en Codificación para todas las personas.
phrase = "Codificación para todos"
sub_string = "l"
print(phrase.ridex(sub_string))

#23-Use el índice o encuentre la posición de la primera aparición de la palabra "porque" en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"
phrase = "No se puede terminar una oración con porque porque porque es una conjunción"
sub_string = "porque"
print(phrase.index(sub_string))

#24-Utilice rinex para encontrar la posición de la última aparición de la palabra "porque" en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"
phrase = "No se puede terminar una oración con porque porque porque es una conjunción"
sub_string = "porque"
print(phrase.ridex(sub_string)) 

#25-Cortar la frase 'porque porque' en la siguiente oración: 'No se puede terminar una oración con porque porque es una conjunción'
phrase = 'No se puede terminar una oración con porque porque es una conjunción'
sub_string = 'porque porque'

phrase = phrase.replace(sub_string,"")
# 'No se puede terminar una oración con porque porque es una conjunción'
# 'No se puede terminar una oración con+ Espacio + Espacio+es una conjunción'
phrase = phrase.split("") # Por defecto (cuando los paréntesis están vacíos: .split()), Python no solo busca "un espacio", sino que busca cualquier cantidad de espacios en blanco y los trata como si fueran uno solo.
phrase = phrase.join()
print(phrase)

#strip() no busca una "palabra" o una "frase", busca una colección de caracteres sueltos.
#.strip(): Su única función es eliminar los espacios en blanco (o caracteres que le indiques) que estén al principio y al final de una cadena. No toca nada de lo que esté en medio de las palabras.
#Imagina que strip es como un limpiaparabrisas. Empieza desde afuera y limpia hacia adentro, pero se detiene en seco en cuanto encuentra algo que NO debe borrar.
#   challenge = 'thirty days of pythoonnn'
#   print(challenge.strip('noth')) # 'irty days of py'
#En tu ejemplo de 'noth':
#   Izquierda: Borra t, borra h. Llega a la i. Como la i no está en tu lista 'noth', el guardia de strip dice: "Aquí hay algo importante, no paso de aquí".
#   Derecha: Borra todas las n y o. Llega a la y. Como la y no está en tu lista, se detiene.
#Lo que hay en el medio está protegido por las letras que NO borraste.

#26-Encuentre la posición de la primera aparición de la palabra "porque" en la siguiente oración: "No se puede terminar una oración con porque porque porque es una conjunción"

#index(): Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice de inicio y finalización (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, aumenta un valorError.
#ridex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice de inicio y finalización (predeterminado 0 y longitud de cadena - 1)


#find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentran retornos -1
#rfind(): Devuelve el índice de la última ocurrencia de una subcadena, si no se encuentran retornos -1

phrase = "No se puede terminar una oración con porque porque porque es una conjunción"
print(phrase.find("porque"))

#27- Cortar la frase 'porque porque' en la siguiente oración: 'No se puede terminar una oración con porque porque es una conjunción'
phrase = 'No se puede terminar una oración con porque porque es una conjunción'
sub_string = 'porque porque'

phrase = phrase.replace(sub_string,"")
# 'No se puede terminar una oración con porque porque es una conjunción'
# 'No se puede terminar una oración con+ Espacio + Espacio+es una conjunción'
phrase = phrase.split("") # Por defecto (cuando los paréntesis están vacíos: .split()), Python no solo busca "un espacio", sino que busca cualquier cantidad de espacios en blanco y los trata como si fueran uno solo.
phrase = phrase.join()
print(phrase)

#28- ¿'Coding For All' comienza con una subcadena de "codificación"?
phrase = 'Coding For All'
print(phrase.startswith('codificación'))

#29- ¿La 'codificación para todos' termina con una codificación de subcadena?
phrase = 'Coding For All'
print(phrase.endswith('codificación'))

#30- 'Codificación para todos', retire los espacios de arrastre izquierdo y derecho en la cuerda dada.
phrase = 'Coding For All'
print(phrase.strip())

#31- ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
    # 30DaysOfPython
    # treinta_días_de_python

# Nomnbres NO VALIDOS
    #1- Comenzar con un número, Un identificador puede tener números, pero nunca al principio.
    #2- Contener espacios, Los espacios no están permitidos en medio de un nombre de variable.
    #3- Usar caracteres especiales o símbolos, Cualquier símbolo que no sea el guion bajo (_) hará que devuelva False. Esto incluye guiones medios, puntos, @, $, #, etc
    #4- Cadenas vacías, Una cadena sin caracteres no puede ser un identificador.
            # print("".isidentifier())  # False

#30DaysOfPython = ""
#print(30DaysOfPython.isidentifier()) FALSE
#treinta_días_de_python = ""
#treinta_días_de_python.isidentifier()

# En Python, la regla de oro es el snake_case (usar guiones bajos intermedios: is_movil).
# Aunque isMovil (llamado camelCase) es técnicamente un identificador válido y .isidentifier() devolverá True, no es la forma "correcta" de escribir Python.

#32- La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Botella', 'Pyramid', 'Falcon'].
# Únete a la lista con un hash con la cadena espacial.
language_list = ['Django', 'Flask', 'Botella', 'Pyramid', 'Falcon']
print(" ".join(language_list))

#33- Utilice la nueva secuencia de escape de línea para separar las siguientes oraciones.
        #-I am enjoying this challenge. I just wonder what is next.
print(f"I am enjoying this challenge\nI just wonder what is next")

# \n: nueva línea

#34- Utilice una secuencia de escape de pestañas para escribir las siguientes líneas.
    # Name      Age     Country   City
    # Asabeneh  250     Finland   Helsinki

# \n: nueva línea
# \t: Tab media(8 espacios)

print(f"Name\tAge\tCountry\tCity\n"
      f"Asabeneh\t250\tFinland\tHelsinki")

#35-Utilice el método de formato de cadena para mostrar lo siguiente:
    #radius = 10
    #area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

print (f' radius = 10 \n'
       f'area = 3.14 * radius ** 2\n'
       f'The area of a circle with radius 10 is 314 meters square.'
       )

#36- Haga lo siguiente usando métodos de formato de cadena:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144

# \n: nueva línea

print(f'8+6 = {8+6}\n'
      f'8-6 = {8-6}\n'
      f"8 * 6 = {8 * 6}\n"
      f"8 / 6 = {8 / 6:.2f}\n"# 2f indica dos decimales despues de la coma.
      f"8 % 6 = {8 % 6}\n"
      f"8 // 6 = {8 // 6}\n"
      f"8 ** 6 = {8 ** 6}\n"
      )