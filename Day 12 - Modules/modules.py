#💻 Ejercicios: Día 12

#Ejercicios: Nivel 1

#1-Escriba una función que genere un six digit/character random_user_id.

import random #Importemos un módulo aleatorio que nos da un valor aleatorio
import string #Un módulo de cadena es un módulo útil para muchos propósitos. 

def random_user_id():
    # string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # string.digits = '0123456789'
    caracteres = string.ascii_lowercase + string.digits
    
    # Seleccionamos 6 caracteres al azar de ese grupo
    # random.choices devuelve una lista, por eso usamos "".join() para unirla en un texto
    user_id = "".join(random.choices(caracteres, k=6))
    
    return user_id 

print(random_user_id())

 #2- Modificar la tarea anterior. 
 # Declarar una función llamada user_id_gen_by_user. 
 # No toma ningún parámetro, pero se necesitan dos entradas usando input(). 
 # Una de las entradas es el número de caracteres y la segunda entrada es el número de ID que se supone que se generarán.

import random
import string

def user_id_gen_by_user():
    # 1. Obtenemos las entradas del usuario
    # Convertimos a int() porque input() siempre devuelve texto (string)
    n_chars = int(input("¿Cuántos caracteres por ID?: "))
    n_ids = int(input("¿Cuántos IDs quieres generar?: "))
    
    # 2. Definimos el pool de caracteres (letras A-Z, a-z y números 0-9)
    caracteres = string.ascii_letters + string.digits
    
    resultados = []
    
    # 3. Bucle para generar la cantidad de IDs solicitada
    for _ in range(n_ids):
        nuevo_id = "".join(random.choices(caracteres, k=n_chars))
        resultados.append(nuevo_id)
    
    # Unimos todos los IDs con un salto de línea para que el print() final los muestre uno abajo de otro
    return "\n".join(resultados)

# Ejecución
#print(user_id_gen_by_user())
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
#print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

#3- Escriba una función llamada rgb_color_gen. Generará colores rgb (3 valores que van de 0 a 255 cada uno).
import random

def rgb_color_gen():
    # Generamos tres números aleatorios entre 0 y 255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Retornamos el string con el formato solicitado
    # Usamos una f-string para insertar los valores fácilmente
    return f'rgb({r},{g},{b})'

print(rgb_color_gen()) 

# Ejemplo de salida: rgb(125,244,255)

#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

#Ejercicios: Nivel 2

#  Escriba una función list_of_hexa_colors que devuelve cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. 
#  El sistema numérico hexadecimal está hecho de 16 símbolos, 0-9 y las primeras 6 letras del alfabeto, a-f. 
#  Compruebe la tarea 6 para ejemplos de salida).

import random
import string

def list_of_hexa_colors(n):
    # Definimos los símbolos hexadecimales: 0-9 y a-f
    # Usamos string.digits (0-9) y string.ascii_lowercase[:6] (a-f)
    hex_chars = string.digits + "abcdef" 
    
    list_of_colors = []
    
    for _ in range(n):
        # Generamos 6 caracteres aleatorios
        color_code = "".join(random.choices(hex_chars, k=6))
        # Lo agregamos a la lista con el prefijo '#'
        list_of_colors.append(f"#{color_code}")
    
    return list_of_colors

# Ejemplo: Generar 3 colores
print(list_of_hexa_colors(3)) 

# Salida esperada: ['#a3e12f', '#03ed55', '#eb3d21']

#  Escriba una función list_of_rgb_colors que devuelve cualquier número de colores RGB en una lista.
import random

def list_of_rgb_colors(n):
    # Creamos la lista vacía (matriz) donde guardaremos los colores
    colors_list = []
    
    for _ in range(n):
        # Generamos los tres componentes aleatorios entre 0 y 255
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        # Formateamos el color como el string 'rgb(r,g,b)'
        color = f'rgb({r},{g},{b})'
        
        # Agregamos el color a nuestra lista
        colors_list.append(color)
        
    return colors_list

# Ejemplo: Generar una matriz de 4 colores RGB
print(list_of_rgb_colors(4))

#  Escribir una función generar_colors que puede generar cualquier número de colores hexa o rgb.
import random
import string

def generate_colors(tipo, cantidad):
    colores = []
    
    # Opción 1: Generar colores Hexadecimales
    if tipo == 'hexa':
        caracteres_hex = string.digits + 'abcdef'
        for _ in range(cantidad):
            codigo = "".join(random.choices(caracteres_hex, k=6))
            colores.append(f'#{codigo}')
            
    # Opción 2: Generar colores RGB
    elif tipo == 'rgb':
        for _ in range(cantidad):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colores.append(f'rgb({r},{g},{b})')
    
    else:
        return "Error: El tipo debe ser 'hexa' o 'rgb'"
        
    return colores

# Pruebas del ejercicio
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors('rgb', 1))  # ['rgb(33,79,176)']

    #generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
    #generate_colors('hexa', 1) # ['#b334ef']
    #generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
    #generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

#Ejercicios: Nivel 3

# Llame a su función shuffle_list, toma una lista como parámetro y devuelve una lista barajada
import random

def shuffle_list(lista_original):
    # random.sample toma la lista y elige 'k' elementos al azar sin repetición.
    # Si k es igual al largo de la lista, obtenemos la misma lista pero barajada.
    # Esto devuelve una LISTA NUEVA, dejando la original intacta.
    return random.sample(lista_original, len(lista_original))

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
lista_mezclada = shuffle_list(mi_lista)

print("Original:", mi_lista)      # [1, 2, 3, 4, 5]
print("Mezclada:", lista_mezclada) # Ejemplo: [3, 1, 5, 2, 4]
# Escriba una función que devuelve una matriz de siete números aleatorios en un rango de 0-9. Todos los números deben ser únicos.
import random

def siete_numeros_unicos():
    # El rango 0-10 define los números del 0 al 9
    numeros_posibles = range(10)
    
    # Seleccionamos 7 elementos únicos de ese rango
    resultado = random.sample(numeros_posibles, 7)
    
    return resultado

print(siete_numeros_unicos())
# Ejemplo de salida: [5, 2, 0, 9, 7, 1, 3]