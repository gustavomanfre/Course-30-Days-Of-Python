#Ejercicios: Día 17

nombres = ['Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Islandia', 'Estonia', 'Rusia']

#1- Desempaque los primeros cinco países y guárdelos en una variable nordic_countries, almacene Estonia y Rusia en es, y ru respectivamente.

#📝 Ejercicio 1: La Calculadora Segura

#Imagina que quieres crear una función que divida dos números que el usuario ingresa por teclado.
 # El problema: Si el usuario ingresa un 0 como divisor, el programa lanzará un ZeroDivisionError. 
 # Si ingresa una letra, lanzará un ValueError.

 # Tu reto: Escribe un bloque try-except que solicite dos números. 
 # Si ocurre un error de división por cero, debe imprimir "No puedes dividir por cero". 
 # Si el error es de valor (letras), debe decir "Por favor, introduce solo números".

def calculator():
    try:
        a = int(input('Ingresar el numero a'))
        b = int(input('Ingresar el numero b'))# Si ingresamos 'Hola', Aca salta el ValueError
        result = a/b # Si ingresamos 'Hola', No llega a saltar el error TypeError, Si salta ZeroDivisionError al ingresar 0
    except ZeroDivisionError:
        print('No puedes dividir por cero')
    except ValueError:
        print('Por favor, introduce solo números')
    else:
        print(result)

#📝 Ejercicio 2: El Buscador de Frutas

#Tienes la lista de tus apuntes: fruits = ['banana', 'orange', 'mango']. 
#Queremos pedirle al usuario un índice (un número) para mostrarle la fruta correspondiente.

#El problema: Si el usuario pide el índice 10, Python lanzará un IndexError porque la lista es pequeña.
#Tu reto: Escribe un código que intente imprimir fruits[indice]. 
# Usa un bloque except específico para capturar el error de índice y mostrar un mensaje amigable como "Esa fruta no existe en nuestra lista".


def index_fruits():
    fruits = ['banana', 'orange', 'mango']
    try:
        i = int(input('Ingresar el numero i'))
        print(fruits[i])
    except IndexError:
        print('Esa fruta no existe en nuestra lista')

#____________________________________________________________________________________________________________________________________________________________#

#📝 Ejercicio 3: El equipo de expedición (Desempaquetado de Listas)
# Vamos a usar el operador * para capturar el "resto" de una lista. 🏔️
# Tu reto: Tienes la lista equipo = ['Guía', 'Médico', 'Explorador 1', 'Explorador 2', 'Cocinero']. 
# Escribe una sola línea de código que asigne:
#        El primer nombre a la variable lider.
#        El segundo nombre a la variable soporte.
#        Todos los demás a una lista llamada resto_equipo.

lider, soporte,*resto_equipo = equipo = ['Guía', 'Médico', 'Explorador 1', 'Explorador 2', 'Cocinero']

#📝 Ejercicio 4: Suma infinita (Embalaje con *args)
#A veces no sabemos cuántos números querrá sumar el usuario. 
#Usamos *args para recibir cualquier cantidad de argumentos. 🔢
#   Tu reto: Crea una función llamada sumar_todos que reciba *args. 
#   Dentro de la función, usa un bucle o la función sum() para devolver la suma total de todos los números que se le pasen.
#        Ejemplo de uso: sumar_todos(1, 2, 3, 4) debería devolver 10.

def sumar_todos (*args):
    s = 0
    for i in args:
        s+=i
    return s


suma_infinita = sumar_todos(1,2,3,4)

#📝 Ejercicio 5: Ficha de Personaje (Embalaje con **kwargs)
#Los diccionarios se "embalan" usando dos asteriscos **. 
#Esto nos permite pasar argumentos con nombre (como nombre="Juan"). 👤
#    Tu reto: Crea una función llamada crear_perfil que reciba **kwargs. 
#    La función debe imprimir cada clave y valor del diccionario resultante.
#    Ejemplo de uso: crear_perfil(nombre="Aragorn", clase="Guerrero", nivel=20)

def crear_perfil (**kwargs):
    for key in kwargs:
        print(f' {key}:{kwargs[key]}')

crear_perfil(nombre="Aragorn", clase="Guerrero", nivel=20)



#____________________________________________________________________________________________________________________________________________________________#
#📝 Ejercicio 6: El Inventario Combinado Imagina que tienes dos listas separadas: una con nombres de objetos y otra con sus cantidades.
#Tu reto: Usa la función zip() dentro de un bucle for para imprimir mensajes como: "Tienes 5 Pociones", "Tienes 50 Flechas", etc. 🏹
 
objetos = ['Pociones', 'Flechas', 'Escudos'] 
cantidades = [5, 50, 2]
inventario = []
cadena =''

for i,j in zip(objetos,cantidades):
    inventario.append({i:j})
    cadena += f"Tienes {j} {i}"
print(cadena)


#📝 Ejercicio 7: Buscador de Tesoros con Índice Tenemos una lista de cofres: cofres = ['Vacío', 'Vacío', 'Diamante', 'Vacío'].
#Tu reto: Usa enumerate() para recorrer la lista y, cuando encuentres el 'Diamante', imprime: "¡Diamante encontrado en el cofre número [índice]!". 💎

for i, j in enumerate(cofres):
    if j == 'Diamante':  # Comprobamos si el contenido es el Diamante
        print(f"¡Diamante encontrado en el cofre número {i}! 💎")

