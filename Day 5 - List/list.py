#💻 Ejercicios: Día 5

#EJERCICIOS: NIVEL 1

#1-Declarar una lista vacía
list = ()
list1 = []

#2-Declarar una lista con más de 5 artículos
num = [1,2,3,4,5]

#3-Encuentra la longitud de tu lista
print(len(num))

#4- Obtenga el primer elemento, el elemento medio y el último elemento de la lista

print(num[0])
tam = len(num)
print(num[-tam])

# 5- Declarar una lista llamada mixed_data_types, poner su(nombre, edad, altura, estado civil, dirección)

mixed_data_types = ["Emanuel",28, 1.84,"Soltero", " Valle de las heras"]

#6- Declarar una variable de lista llamada it_companies y asignar valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]

#7-Imprimir la lista usando print()
print(it_companies)

#8- Imprimir el número de empresas en la lista
print(len(it_companies))

#9- Imprimir la primera, media y última empresa
tam = len(it_companies)
print(it_companies[0])
print(it_companies[tam//2])
print(it_companies[-1])
print(it_companies[tam-1]) # Cuando usamos el indice directo, se utilizan los indices normales, cuando usamos : no se cuenta el ultimo indice.

#10- Imprime la lista después de modificar una de las empresas
it_companies[1] = ["Meta"]
print(it_companies)

#11- Añadir una empresa de TI a it_companies
it_companies.append("Twitter") # Con insert añadimos elementos en una posicion determinada, con append al final
print(it_companies)

#12- Insertar una empresa de TI en el medio de la lista de empresas
it_companies.insert(tam//2+1,"Intel" )
print(it_companies)

#13- Cambiar uno de los nombres it_companies a mayúsculas (¡IBM excluido!)
it_companies[0] = it_companies[0].upper()
print(it_companies[0])

#14- Únete a it_companies con una cadena '#;'
print(it_companies.append("#"))

#15- Compruebe si existe una determinada empresa en la lista it_companies.
is_boolean = "IBM" in it_companies
print(is_boolean)

#16- Ordenar la lista usando el método sort()
print(it_companies.sort())

#17- Invierta la lista en orden descendente utilizando el método reverse()
it_companies.reverse() #El método reverse() invierte el orden de una lista, 
print(it_companies)    #En Python, los métodos que modifican el objeto original devuelven por defecto None.


#18- Reparte las 3 primeras empresas de la lista
print(it_companies[0:3])

#19- Reduzca la empresa de TI del medio o las empresas de la lista.


#20- Eliminar la primera empresa de TI de la lista
it_companies.pop(0)
print(it_companies)

#Todos modifican la lista original.
#REMOVE
#El método de remove elimina un elemento especificado de una lista. remove(valor): Mutación por búsqueda
#POP
#El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice). pop(índice): Mutación con retorno
#DEL
#La palabra clave del elimina el índice especificado y también se puede utilizar para eliminar elementos dentro del rango de índice. También puede eliminar la lista por completo. del lst[índice]: Destrucción de referencia

#21- Eliminar la mediana empresa de TI o las empresas de la lista.
#La mediana es el valor que separa la mitad superior de la mitad inferior de un conjunto de datos.
tam = len(it_companies)//2
print(it_companies.pop(tam))

#22- Eliminar la última empresa de TI de la lista
print(it_companies.pop())

#23- Eliminar todas las empresas de TI de la lista
del it_companies [:] 
print(it_companies)

#24- Destuir la lista de empresas de TI.
del it_companies

#25- Únete a las siguientes listas:
#Después de unirse a las listas en la pregunta 26. Copie la lista unida y asigne a una variable full_stack, luego inserte Python y SQL después de Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end #Unir dos listas con el operador +, no modifican las listas originales
print(full_stack)                 
lst_copy = full_stack.copy()      # Copiar una lista con el método copy(), lst_copy es una copia de full_stack, si modificamos lst_copy no afecta a full_stack
lst_copy.append("Python")         # Añadir elementos a la lista copiada
lst_copy.append("SQL")           
print(lst_copy)

#El Operador + (Concatenación)
#Comportamiento: Crea un Nuevo Objeto. Cuando haces lista_nueva = lista_a + lista_b

# El Método .extend() 
# # Unir usando el método extend() El método extend() permite añadir la lista en una lista. 

#Comportamiento: Modifica "In-Place" (Mutación). Cuando haces lista_a.extend(lista_b):
#   En el Heap: Python va al bloque de memoria de lista_a.
#    Redimensionamiento (Realloc): Verifica si hay espacio libre al final del bloque de lista_a. Si no lo hay, solicita al sistema operativo agrandar ese mismo bloque.
#   Copia Parcial: Solo copia los punteros de lista_b y los pega al final de lista_a. Los punteros originales de lista_a no se tocan ni se mueven.
#    Resultado: lista_a es ahora más grande. No se creó ningún objeto lista nuevo.
# El método .extend() modifica la lista original "In-place" (en el mismo lugar de la memoria). No crea una lista nueva, sino que expande la que ya existe.  



"""
Ejercicios: Nivel 2

    La siguiente es una lista de 10 estudiantes de edad:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

"""

#Ordenar la lista y encontrar la edad mínima y máxima
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # El método .sort() es una operación "In-place" (en el lugar). Esto significa que modifica la lista original directamente en el Heap y no crea una lista nueva.
num_max = max(ages)
num_min = min(ages)

#Añadir la edad mínima y la edad máxima de nuevo a la lista
ages.append(num_min)
ages.append(num_max)
print(ages)

#Encuentre la edad media (un elemento medio o dos elementos intermedios divididos por dos)
tam = len(ages)
if tam % 2 == 0:
    mediana = ages([tam//2]+ages[tam//2-1])/2
else:
    mediana = ages[tam//2+1]

print(mediana)

#Encuentra la edad promedio (suma de todos los artículos divididos por su número)
promedio = sum(ages)/len(ages)
print(promedio)
#Encuentre el rango de las edades (máximo menos min)
rango = num_max - num_min

#Compare el valor de (min - promedio) y (máximo - promedio), use el método abs()
promedio = sum(ages)/len(ages)
num_max = max(ages)
num_min = min(ages)
distancia_min = abs(num_min - promedio)
distancia_max = abs(num_max - promedio)
print(f"Distancia del mínimo: {distancia_min}")
print(f"Distancia del máximo: {distancia_max}")

# Comparación lógica
if distancia_min > distancia_max:
    print("La edad mínima está más lejos del promedio.")
else:
    print("La edad máxima está más lejos del promedio.")


#Encuentra el(los) país(es) medio(s) en la lista de países.
paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
#            0        1       2          3         4          5          6
tam = len(paises)
mitad = tam // 2

if tam % 2 != 0:
    # Caso IMPAR: El centro exacto es 'mitad'
    print(f"El país medio es: {paises[mitad]}")
else:
    # Caso PAR: Los dos centrales son 'mitad - 1' y 'mitad'
#paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Argentina']
#              0        1      2         3          4          5            6          7

    pais1 = paises[mitad - 1] # 4-1
    pais2 = paises[mitad] # 4
    print(f"Los países medios son: {pais1} y {pais2}")

#Divida la lista de países en dos listas iguales si es incluso si no es un país más para la primera mitad.
paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
# Tam = 7. El corte será (7 + 1) // 2 = 4

tam = len(paises)
corte = (tam + 1) // 2  # Este +1 asegura que el "extra" vaya a la primera mitad

primera_mitad = paises[:corte] # Agarra desde el inicio hasta el corte (sin incluir el índice corte)
segunda_mitad = paises[corte:] # Agarra desde el corte hasta el final

print(f"Primera mitad: {primera_mitad}")
print(f"Segunda mitad: {segunda_mitad}")
# Desempaque los tres primeros países y el resto como países escanédicos.
#['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. 

paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# Desempaquetamos los 3 primeros y el resto en una lista nueva
p1, p2, p3, *scandic_countries = paises

print(f"País 1: {p1}")
print(f"País 2: {p2}")
print(f"País 3: {p3}")
print(f"Países Escandinavos: {scandic_countries}")