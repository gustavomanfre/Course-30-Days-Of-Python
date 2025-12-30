
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


""""

Reparte las 3 primeras empresas de la lista

Remarca las últimas 3 compañías de la lista

Reduzca la empresa de TI del medio o las empresas de la lista

Eliminar la primera empresa de TI de la lista

Eliminar la mediana empresa de TI o las empresas de la lista

Eliminar la última empresa de TI de la lista

Eliminar todas las empresas de TI de la lista

Destruir la lista de empresas de TI

Únete a las siguientes listas:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

    Después de unirse a las listas en la pregunta 26. Copie la lista unida y asigne a una variable full_stack, luego inserte Python y SQL después de Redux.

Ejercicios: Nivel 2

    La siguiente es una lista de 10 estudiantes de edad:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    Ordenar la lista y encontrar la edad mínima y máxima
    Añadir la edad mínima y la edad máxima de nuevo a la lista
    Encuentre la edad media (un elemento medio o dos elementos intermedios divididos por dos)
    Encuentra la edad promedio (suma de todos los artículos divididos por su número)
    Encuentre el rango de las edades (máximo menos min)
    Compare el valor de (min - promedio) y (máximo - promedio), use el método abs()

    Encuentra el(los) país(es) medio(s) en la lista de países
    Divida la lista de países en dos listas iguales si es incluso si no es un país más para la primera mitad.
    ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desempaque los tres primeros países y el resto como países escanédicos.

"""