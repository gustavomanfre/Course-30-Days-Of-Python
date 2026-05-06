Manejo de excepciones

Python utiliza try y excepto para manejar los errores con gracia. Una salida elegante (o manejo elegante) de errores es un simple lenguaje de programación: un programa detecta una condición de error grave y "sale con gracia", de manera controlada como resultado. A menudo, el programa imprime un mensaje de error descriptivo en un terminal o registro como parte de la salida elegante, esto hace que nuestra aplicación sea más robusta. La causa de una excepción es a menudo externa al programa en sí. Un ejemplo de excepciones podría ser una entrada incorrecta, nombre de archivo incorrecto, incapaz de encontrar un archivo, un dispositivo de IO que funciona mal. El manejo elegante de los errores evita que nuestras aplicaciones se bloqueen.

Hemos cubierto los diferentes tipos de errores de Python en la sección anterior. Si usamos try y excepto en nuestro programa, entonces no generará errores en esos bloques.

try:
    code in this block if things go well
except:
    code in this block run if things go wrong

Ejemplo:

try:
    print(10 + '5')
except:
    print('Something went wrong')

En el ejemplo anterior, el segundo operando es una cadena. Podríamos cambiarlo a flotar o int para añadirlo con el número para que funcione. Pero sin ningún cambio, el segundo bloque, excepto, será ejecutado.

Ejemplo:

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

Something went wrong

En el ejemplo anterior, el bloque de excepciones se ejecutará y no sabemos exactamente el problema. Para analizar el problema, podemos utilizar los diferentes tipos de errores con excepto.

En el siguiente ejemplo, se encargará del error y también nos dirá el tipo de error planteado.

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

Enter your name:Asabeneh
Year you born:1920
Type error occured

En el código anterior, la salida será TypeError. Ahora, vamos a añadir un bloque adicional:

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

Enter your name:Asabeneh
Year you born:1920
You are Asabeneh. And your age is 99.
I usually run with the try block
I alway run.

También se acorta el código anterior de la siguiente manera:

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

1. ¿input() imprime en consola o solo en pantalla?

La función input('Texto') hace ambas cosas, pero con un propósito específico:

    En pantalla: Muestra el mensaje que escribiste entre comillas para que el usuario sepa qué debe escribir.

    En la consola: "Pausa" la ejecución del programa y se queda esperando a que el usuario escriba algo y presione Enter.

    Dato Clave: Todo lo que el usuario escribe, input() lo guarda como un String (texto), incluso si son números.

2. ¿Por qué saltó el TypeError?

El error saltó en esta línea: age = 2019 - year_born

La razón: Como dijimos antes, input() devuelve un texto. Entonces, para Python, tu operación se veía así: age = 2019 - "1920"

No se puede restar un texto de un número entero. Es como intentar restar "Manzana" al número 10. Como los "tipos" de datos son incompatibles, Python lanza un TypeError (Error de Tipo).
3. ¿Qué condición debe cumplirse para que entre en except TypeError?

Para que el programa entre en ese bloque, debe ocurrir una operación inválida entre tipos de datos.

Aquí tienes ejemplos de qué condiciones disparan cada uno en tu código:
Entra en TypeError cuando:

    Intentas restar un texto a un número: 2019 - "1920".

    Intentas sumar una lista con un número: [1, 2] + 5.

Entra en ValueError cuando:

    Si corrigieras tu código usando int(year_born) pero el usuario escribe letras (ej: "Mil novecientos veinte").

    Condición: El tipo de dato es correcto (es un texto), pero el valor no se puede transformar a número.
_____________________________________________________________________________________________________________________________________________________________

Esta es una forma muy común de simplificar el manejo de errores en Python. Al usar Exception as e, estás creando un "atrapalotodo".

Aquí tienes la explicación detallada en formato Markdown (.md):
🛡️ Manejo Genérico de Errores: Exception as e

En lugar de escribir un bloque except para cada tipo de error (TypeError, ValueError, etc.), usamos la clase base de la cual heredan casi todos los errores en Python.
Análisis del código:
Python

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    
    # Aquí ya agregaste int() para evitar el TypeError anterior
    age = 2019 - int(year_born)
    
    print(f'You are {name}. And your age is {age}.')

except Exception as e:
    print(e)

1. ¿Qué es Exception as e?

    Exception: Es la clase "padre". Si ocurre un ValueError, un ZeroDivisionError o cualquier otro, Python dirá: "¿Es esto una Exception?". Como la respuesta es sí, entra en ese bloque.

    as e: Es un alias. Guarda el mensaje de error oficial de Python dentro de la variable e.

2. ¿Qué imprime print(e)?

A diferencia de tus ejemplos anteriores donde tú escribías un texto manual (ej: 'Value error occured'), print(e) mostrará la explicación técnica de Python.

    Si el usuario escribe "Hola" en el año: Imprimirá: invalid literal for int() with base 10: 'Hola'

    Si el usuario presiona Ctrl+C para cancelar: Imprimirá el mensaje correspondiente a la interrupción.

⚖️ Ventajas y Desventajas
Aspecto	Usar Exception as e (Genérico)	Usar varios except (Específico)
Código	Más corto y limpio.	Más largo.
Control	No sabes qué falló exactamente a menos que leas el mensaje.	Puedes dar instrucciones exactas (ej: "Por favor, solo usa números").
Seguridad	Útil para capturar errores inesperados que no previste.	Es la mejor práctica profesional (especificidad).
💡 Un detalle sobre el int(year_born)

Ahora que agregaste int(), el error que verás con más frecuencia no será TypeError, sino ValueError.

    Antes: El programa fallaba al intentar restar.

    Ahora: El programa fallará antes de la resta, justo en el momento en que int() intente convertir el texto. Si el texto no es puramente numérico, saltará directo al except.
____________________________________________________________________________________________________________________________________________________________

🔢 ¿Qué es el objeto range(2, 7)?

En Python 3, range no genera una lista de números inmediatamente en la memoria. En su lugar, crea un generador iterable.

    La instrucción: range(start, stop)

    Los valores: Comienza en 2 y termina justo antes del 7.

    Resultado lógico: Los números generados serían 2, 3, 4, 5, 6.

📝 Lo que verás en consola

Si intentas imprimir la variable directamente:
Python

numbers = range(2, 7)
print(numbers) 

Devuelve: range(2, 7)

Python te devuelve la "promesa" de esos números. No los verás expandidos a menos que los conviertas o los recorras.
🛠️ Cómo ver los números reales

Para "ver" el contenido dentro de la variable numbers, tienes dos formas comunes:
1. Convertirlo a una lista
Python

print(list(numbers)) 
# Devuelve: [2, 3, 4, 5, 6]

2. Usarlo en un bucle for
Python

for n in numbers:
    print(n)
____________________________________________________________________________________________________________________________________________________________

Desempacar
Desembalaje de listas

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

Cuando ejecutamos este código, se plantea un error, porque esta función toma los números (no una lista) como argumentos. Desempaquemos/desestructuramos la lista.

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

También podemos usar el desempaquetado en la función incorporada de gama que espera un inicio y un final.

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

____________________________________________________________________________________________________________________________________________________________

Una lista o una tupla también se puede desempacar así:

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

____________________________________________________________________________________________________________________________________________________________

Desempaquetando diccionarios

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

Embalaje

A veces nunca sabemos cuántos argumentos necesitan ser pasados a una función de Python. Podemos utilizar el método de embalaje para permitir que nuestra función tome un número ilimitado o un número arbitrario de argumentos.
Listas de embalaje

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

Diccionarios de embalaje

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}

Difusión en Python

Como en JavaScript, la difusión es posible en Python. Compruébemoslo en un ejemplo a continuación:

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

Enumerar

Si estamos interesados en un índice de una lista, utilizamos enumerar la función incorporada para obtener el índice de cada elemento de la lista.

for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

The country Finland has been found at index 0.

Cremallera

A veces nos gustaría combinar listas cuando hacemos bucles a través de ellas. Vea el ejemplo a continuación:

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]

____________________________________________________________________________________________________________________________________________________________

🤐 ¿Cómo funciona zip()?

La función zip() recibe su nombre porque actúa como una cremallera. Toma el primer elemento de la lista A y el primero de la lista B y los "abrocha" juntos. Luego el segundo con el segundo, y así sucesivamente.
Análisis del Código
Python

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    # En cada vuelta, creamos un diccionario {} y lo metemos en la lista
    fruits_and_veges.append({'fruit': f, 'veg': v})

    zip(fruits, vegetables): Crea parejas de elementos: ('banana', 'Tomato'), ('orange', 'Potato'), etc.

    for f, v in ...: En cada iteración, la variable f toma el valor de la fruta y v el del vegetal.

    append({...}): Aquí es donde sucede lo que preguntaste. Estamos insertando un diccionario (identificado por las llaves {}) dentro de la lista fruits_and_veges.

📊 Estructura del Resultado

El resultado final es una Lista (corchetes []) que contiene Diccionarios (llaves {}) en su interior:
Python

[
  {'fruit': 'banana', 'veg': 'Tomato'}, 
  {'fruit': 'orange', 'veg': 'Potato'},
  # ... así hasta el final
]

💡 Datos clave para tus apuntes:

    ¿Qué pasa si las listas tienen tamaños diferentes?: zip() es "educado" pero estricto: se detendrá en cuanto la lista más corta se acabe. Si tuvieras 10 frutas pero solo 5 vegetales, el resultado solo tendría 5 parejas.

    ¿Por qué usar diccionarios?: Es una forma excelente de organizar datos relacionados. Si esto fuera una aplicación de cocina, podrías acceder fácilmente a fruits_and_veges[0]['fruit'] para obtener 'banana'.

________________________________________________________________________________________________________________________________________

TypeError ❌ ocurre cuando intentamos hacer algo con un tipo de dato que simplemente no lo permite (como restar un texto de un número). 
TypeError (Error de Tipo): Ocurre cuando intentas hacer algo con un objeto de un tipo que físicamente no permite esa acción. Por ejemplo: 5 + "Hola". Python dice: "No sé cómo sumar un número con un texto, son naturalezas distintas". ❌


ValueError ⚠️ ocurre cuando el tipo de dato es el correcto, pero el contenido (valor) no sirve para la operación.
ValueError (Error de Valor): Ocurre cuando la función sí acepta ese tipo de dato (en este caso, int() acepta textos), pero lo que dice el texto no tiene sentido para la conversión. 🔢