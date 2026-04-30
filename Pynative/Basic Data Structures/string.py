# Ejercicio 1. Crear una cadena hecha del primer, medio y último carácter.


'''Propósito del ejercicio: Este ejercicio enseña los fundamentos de la indexación de cadena.
El acceso a posiciones específicas, especialmente el medio que requiere el cálculo de la longitud,
es una habilidad fundamental para el análisis de datos y la manipulación de texto.'''


# Salida esperada: "Jms"


# Versión 1
str1 = "James"
len_str1 = len(str1)
str2 = str1[0]+str1[len_str1 // 2-1]+str1[-1]
print(str2)


# Versión 2 (Final)
str1 = "James"
first = str1[0]
middle = str1[len(str1) // 2]
last = str1[-1]
print(str2)


#---------------------------------------------------------------------------------------------------------------------------------------------------------#


#Ejercicio 2. Crear una cadena hecha de los tres caracteres del medio.
'''Propósito del ejercicio: Esto se basa en la indexación mediante la introducción de corte en cadena.
El corte es una poderosa característica de Python que le permite extraer “trozos” completos de datos de manera eficiente.'''
# Salida Esperada: Dip


#Version 1
middle_index = len(str1)//2
str2 = str1[middle_index]
str3 = str1[middle_index-1]
str4 = str1[middle_index+1]
str5 = str3 + str2 + str4
print(str5)


#Version 2
str1 = "JhonDipPeta"
middle_index = len(str1)//2
str2 = str1[middle_index-1:middle_index+1]
#---------------------------------------------------------------------------------------------------------------------------------------------------------#


#Ejercicio 3. Añada una nueva cadena en medio de una cadena determinada.
# Problema de práctica: Dados dos string, s1 y s2, crear una nueva cadena mediante la adición s2. En medio de s1.
'''Proposito del ejercicio: Este ejercicio introduce la partición y la concatenación de cuerdas.
En la programación, a menudo necesita “inyectar” datos en una plantilla o modificar cadenas en ubicaciones específicas.'''
# Salida: AuKellylt
#   A    U   L   T      => LEN = 4 => 4//2 = 2      Es la cantidad de desplazamientos
#  [0]  [1] [2] [3]
#            2                                      Recordar que en slice indice superior no cuenta.


s1 = "Ault"
s2 = "Kelly"
middle_index = len(s1)//2                           # Resultado:2
str1 = s1[:middle_index]                            # Recordar que aunque deberia ser s1[0:2] en slice no cuenta el indice superior en realidad esta evaluando s1[0:1]
str3 = s1[middle_index:]
str4 = str1 + s2 + str3
print(str4)


#---------------------------------------------------------------------------------------------------------------------------------------------------------#


# Ejercicio 5. Invierta una cadena dada


# Problema de práctica: Escribe un programa para revertir una cadena determinada.
'''Propósito del ejercicio: Revertir una cadena es un ejercicio clásico de construcción lógica.
En Python, esto se hace de manera más eficiente a través de Slicing, lo que demuestra la capacidad del lenguaje para manipular secuencias utilizando “pasos”.
Es un requisito previo para resolver problemas como la detección de palíndromos.'''
# Salida: evitanYP


str1 = "PYnative"
str2 = str1[::-1]


print(str2)                                         # cadena[inicio:fin:paso]


# Porque Python ya entiende que: si el paso es -1, arranca del final automáticamente y termina al principio


#---------------------------------------------------------------------------------------------------------------------------------------------------------#


#Ejercicio 6. Encuentre la última posición de una subcadena determinada


# Problema de práctica: Escriba un programa para encontrar el último índice de la subcadena “Emma” en una cadena determinada.
'''Finalidad del ejercicio:
mientras que el el metodo .find(), busca desde el principio de una cadena,
el metodo rfind() (Reverse Find) localiza desde el final la ocurrencia de un patrón especificado.
Esta funcionalidad es esencial a la hora de analizar rutas de archivo o URL que requieren la identificación del delimitador final.'''


# Salida Esperada: Last occurrence of Emma starts at index 43


str1 = "Emma is a data scientist who knows Python. Emma works at google."
last_index = str1.rfind('Emma')
#---------------------------------------------------------------------------------------------------------------------------------------------------------#


# Ejercicio 7. Dividir una cuerda en guiones


# Problema de práctica: Escriba un programa para dividir una cadena determinada en guiones y mostrar cada subcadena.
'''Objetivo del ejercicio:
Este ejercicio introduce el concepto de tokenización.
Dividir cadenas en componentes más pequeños basados en delimitadores, como comas, espacios o guiones, es una técnica común para procesar archivos CSV, registros y listas ingresadas por el usuario.'''


# Salida Esperada:
# Mostrando cada subcadena:
# ¿Emma
# Es
# a
# Datos
# Científico científico


str1 = "Emma-is-a-data-scientist"
str2 = str1.split('-')
print("Mostrando cada subcadena: ")


#---------------------------------------------------------------------------------------------------------------------------------------------------------#
# Ejercicio 8. Encuentre todas las ocurrencias de una subcadena en una cadena dada ignorando el caso


# Problema de práctica: Escriba un programa para encontrar el recuento total de la subcadena “USA” en una cadena determinada,
#  ignorando el caso (es decir, tanto “usa” como “USA” deben ser contados).


'''Finalidad del ejercicio: Este ejercicio aborda la normalización de los casos.
En la ciencia de datos práctica y las aplicaciones de raspado web, los datos de texto son frecuentemente inconsistentes.
La conversión de todo el texto a minúscula antes del procesamiento se considera una práctica óptima estándar.'''
#Salida Esperada: The USA count is: 2


str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = str1.lower()                             #lower pasa todos los caracteres de la cadena a minusculas
print("The USA count is:", str2.count('usa'))


#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# Ejercicio 9. Prueba de equilibrio de caracteres de cadena

# Problema de práctica: Escribe un programa para comprobar si dos cadenas están equilibradas. 
# Por ejemplo, las cadenas s1 y s2 están equilibrados si todos los caracteres en s1 están presentes en s2. 
# La posición del caracteres no importa.

'''Finalidad del ejercicio: Este ejercicio se centra en las pruebas de membresía. 
Este concepto fundamental se utiliza en la validación de datos, 
como verificar si una contraseña contiene caracteres requeridos o determinar si una consulta de búsqueda coincide con una entrada de base de datos.'''

s1 = "ynf"
s2 = "PyNative"
is_contain = True

s2 = s2.lower()
s1 = s1.lower()

for i in s1:
    if i not in s2:
        is_contain = False
        break
print(is_contain)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# Ejercicio 10. Contador de vocales
# Problema de práctica: Escriba un programa para contar el número total de vocales (a, e, i, o, u) en una cadena determinada.'''
# Salida Esperada: Vowel Count: 3

# Version 1
str1 = "Hello World"

count_vowels = 0
for vowel in str1.lower():
    count_vowels += 'aeiou'.count(vowel)

print('Vowel count:', count_vowels)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
# Ejercicio 11. Prefijo/Comprobación de sufijo

#Problema de práctica: Compruebe si una URL determinada comienza con “https” y termina con “.com”.
'''Finalidad del ejercicio: Este ejercicio enseña la validación booleana. 
Métodos como .startswith() y .endswith() son más limpios y menos propensos a errores que el corte manual para verificar formatos de archivo, protocolos o convenciones de nombres.'''

#Salida Esperada: Is valid URL: True

str1 = "https://google.com"
is_valid_url = str1.startswith('https') and str1.endswith('.com')
print('Is valid URL:', is_valid_url)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicio 12. Caso de swap

#Problema de práctica: Escriba un programa para alternar el caso de todos los caracteres de una cadena (la mayúscula se convierte en minúscula y viceversa).

#Finalidad del ejercicio: Esto demuestra la transformación de casos. Aunque simple, a menudo se utiliza en algoritmos de búsqueda para normalizar datos o en editores de texto para proporcionar la funcionalidad de “Caso de palanca”.

#Insumos dados: str1 = "PyThOn"

#Salida Esperada: pYtHoN

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicio 13. Quitar el espacio en blanco

#Problema de práctica: elimine cada espacio de una cadena determinada, incluidos los espacios entre palabras.

#Propósito del ejercicio: Esto resalta la diferencia entre el recorte y el filtrado. Mientras .strip()Solo se eliminan los espacios de ataque/trasero, .replace()Puede alcanzar dentro de una cadena para eliminar caracteres globalmente.

#Insumos dados: str1 = " P y t h o n "

#Salida Esperada: Python

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicio 14. Eliminación de N-ésimo carácter

#Problema de práctica: Escriba un programa para eliminar el carácter en el índice iDe una cuerda.

#Propósito del ejercicio: Dado que las cadenas de Python son inmutables (no se puede simplemente eliminar un carácter en un índice), este ejercicio le enseña cómo “reconstruir” una cadena saltando una parte específica.

#Insumos dados: str1 = "Python", i = 2

#Salida Esperada:

 #Pyhon(Se eliminó el carácter 't' en el índice 2)


#---------------------------------------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------
# Ejercicio 15. Partición de cuerdas

# Problema:
# Utilizar el método .partition() para dividir una cadena en tres partes:
# 1) la parte antes de un separador
# 2) el separador en sí
# 3) la parte después del separador

# Finalidad:
# Entender que .partition() siempre devuelve una tupla de 3 elementos.
# Es útil cuando necesitamos conservar el separador (ej: emails, key=value, etc).

# Datos de entrada:
# str1 = "username@company.com"
# sep = "@"

# Salida esperada:
# ('username', '@', 'company.com')


# -----------------------------------------------------------------------------------
# Ejercicio 16. Extraer Extensión De Archivo

# Problema:
# Dado un nombre de archivo como string, extraer solo la extensión del archivo.

# Finalidad:
# Practicar análisis de strings y encontrar la última aparición de un carácter (".").
# Importante para archivos con múltiples puntos (ej: archivo.tar.gz).

# Datos de entrada:
# file_name = "report_final_v2.pdf"

# Salida esperada:
# pdf


# -----------------------------------------------------------------------------------
# Ejercicio 17. Minúscula Primero

# Problema:
# Reorganizar una cadena de forma que:
# - primero aparezcan todas las letras minúsculas
# - luego todas las letras mayúsculas

# Finalidad:
# Practicar filtrado de caracteres y reconstrucción de strings.
# Mantener el orden relativo dentro de cada grupo.

# Datos de entrada:
# str1 = "PyNaTive"

# Salida esperada:
# yaivePNT


# -----------------------------------------------------------------------------------
# Ejercicio 18. Contar letras, dígitos y símbolos

# Problema:
# Contar cuántos caracteres de una cadena son:
# - letras
# - dígitos
# - símbolos especiales

# Finalidad:
# Usar métodos como:
# - .isalpha()
# - .isdigit()
# Clasificación típica de datos en validaciones.

# Datos de entrada:
# str1 = "P@#yn26at^&i5ve"

# Salida esperada:
# Chars = 8
# Digits = 3
# Symbols = 4


# -----------------------------------------------------------------------------------
# Ejercicio 19. Cadena mixta con caracteres alternos

# Problema:
# Crear una nueva cadena combinando:
# - primer carácter de s1
# - último carácter de s2
# - segundo carácter de s1
# - segundo desde el final de s2
# ... y así sucesivamente

# Los caracteres sobrantes se agregan al final.

# Finalidad:
# Practicar manejo de índices en dos direcciones:
# - avance (s1)
# - retroceso (s2)

# Datos de entrada:
# s1 = "Abc"
# s2 = "Xyz"

# Salida esperada:
# AzbycX


# -----------------------------------------------------------------------------------
# Ejercicio 20. Suma y promedio de dígitos en una cadena

# Problema:
# Recorrer una cadena y:
# - extraer solo los dígitos
# - calcular su suma
# - calcular su promedio

# Ignorar cualquier otro tipo de carácter.

# Finalidad:
# Combinar:
# - filtrado de datos (extraer números)
# - operaciones matemáticas (suma y promedio)

# Datos de entrada:
# str1 = "PYnative29@#8496"

# Salida esperada:
# Sum is: 38
# Average is: 6.33
