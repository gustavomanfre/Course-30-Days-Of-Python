#💻 Ejercicios: Día 10
#____________________________________________________________________________________________________________________________________________________________

#EJERCICIOS: NIVEL 1

#1- "Itera del 0 al 10 usando un bucle for, haz lo mismo usando un bucle while."

for i in range(11):
    print(i)

i = 0
while 10 >= i:
    print(i)
    i+=1

#2- "Itera del 10 al 0 usando un bucle for, haz lo mismo usando un bucle while.".

for i in range(10,-1,-1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i-=1


#3- "Escribe un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:"

for i in range(1,8):
    print('#'*i)

  #
  ##
  ###
  ####
  #####
  ######
  #######


# 4- Utilice bucles anidados para crear lo siguiente:

for i in range(1,9):
    print ('#'*8)

for i in range(8):
    for j in range(8): 
        print('#', end=' ')  # 'end' evita que salte de línea después de cada #
    print()  # Este print vacío hace el salto de línea al terminar cada fila
    
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

#5- Imprimir el siguiente patrón:


for i in range(11):
    print(f'{i}*{i} = {i*i}')
    
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

#6-Iterar a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle para e imprimir los elementos.
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

#7-Úselo loop for para iterar de 0 a 100 e imprimir solo números pares.

for i in range(0,101,2):
    print(i)


#8-Úselo para loop para iterar de 0 a 100 e imprimir solo números impares.
for i in range(0,101):
    if i%2 == 1:
        print(i)

for i in range(1, 101, 2):
    print(i)
#____________________________________________________________________________________________________________________________________________________________

#EJERCICIOS: NIVEL 2

#1-Utilice para el bucle para iterar de 0 a 100 e imprimir la suma de todos los números.

#2-The sum of all numbers is 5050.

#3-Úselo para loop para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todas las probabilidades.

#4-The sum of all evens is 2550. And the sum of all odds is 2500.

#____________________________________________________________________________________________________________________________________________________________

#Ejercicios: Nivel 3

#1-Vaya a la carpeta de datos y utilice el archivo countries.py. Atravese los países y extraiga todos los países que contengan la palabra tierra.
#2-Esta es una lista de frutas, ['banano', 'naranja', 'mango', 'limón'] invertir el orden usando el bucle.
#3-Vaya a la carpeta de datos y utilice la countries_data.py Archivo.
#4-¿Cuál es el número total de idiomas en los datos
#5-Encuentra los diez idiomas más hablados a partir de los datos
#6;Encuentra los 10 países más poblados del mundo

