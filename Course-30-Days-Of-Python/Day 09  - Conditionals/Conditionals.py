#💻 Ejercicios: Día 9
#Ejercicios: Nivel 1

#1-Obtenga la entrada del usuario usando la entrada (“Ingrese su edad:”). 
#Si el usuario tiene 18 años o más, da tu opinión: tienes la edad suficiente para conducir. 
#Si por debajo de 18 da retroalimentación para esperar la cantidad faltante de años. Salida:
edad = int(input("Ingrese su edad:"))

#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

if edad >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')

#2-Compare los valores de my_age y your_age usando if ... else. ¿Quién es mayor (yo o tú)? Use input(“Introducir su edad: ”) para obtener la edad como entrada. 
#Puede usar una condición anidada para imprimir "año" durante 1 año de diferencia de edad, "años" para diferencias más grandes y un texto personalizado si my_age = your_age. 
#Salida:

#Enter your age: 30
#You are 5 years older than me.
mi_edad = int(input("Ingresar edad"))
otra_edad = int(input("Ingresar edad"))

diferencia = int(mi_edad - otra_edad)

if diferencia == 0:
    print("Tenemos la misma edad")
else:
    y = "Año" if abs(diferencia) == 1 else "Años" # Short Hand
    print(f"Tu eres {abs(diferencia)} {y} {"mas joven" if diferencia > 0 else "mas grande"} que yo")

#3-Obtenga dos números del usuario usando el mensaje de entrada. 
# Si a es mayor que b el retorno "a es mayor que b", si a es menor b retorno "a es menor que b", de lo contrario "a es igual a b". 
# Salida:

#Enter number one: 4
#Enter number two: 3
#4 is greater than 3

a = int(input("Ingresar numero"))
b = int(input("Ingresar numero"))

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print("a es igual a b")
#___________________________________________________________________________________________________________________________________________________________

#Ejercicios: Nivel 2

#4-Escriba un código que dé la calificación a los estudiantes de acuerdo con sus puntajes:

#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

calificacion = int(input("Ingresar calificacion"))

if calificacion >= 80 and calificacion <= 100:
    print('A')
elif calificacion >= 70 and calificacion <= 79:
    print('B')

elif calificacion >= 60 and calificacion <= 69:
    print('C')

elif calificacion >= 50 and calificacion <= 59:
    print('D')

elif calificacion >= 0 and calificacion <= 49:
    print('F')



#5-Compruebe si la temporada es otoño, invierno, primavera o verano. 
#Si la entrada del usuario es: Septiembre, octubre o noviembre, la temporada es otoño. Diciembre, enero o febrero, la temporada es invierno. 
#Marzo, abril o mayo, la temporada es primavera Junio, julio o agosto, la temporada es verano

mes = input("Ingresar mes").lower().strip()

if mes == "septiembre" or mes == "octubre" or mes == "noviembre" :
    print('Otoño')
elif mes == "diciembre" or mes == "enero" or mes == "febrero" :
    print('Invierno')

elif mes == "marzo" or mes == "abril" or mes == "mayo" :
    print('Primavera')

elif mes == "junio" or mes == "julio" or mes == "agosto" :
    print('Verano')
else:
    print("Mes ingresado incorrectp")

#La siguiente lista contiene algunas frutas:
fruits = ['banana', 'orange', 'mango', 'lemon']


#Si una fruta no existe en la lista, añade la fruta a la lista e imprime la lista modificada.. 
#Si la fruta existe, imprime('Esa fruta ya existe en la lista')

fruta = input()
if fruits in fruta:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(fruta)
    print(fruits)

#Ejercicios: Nivel 3

#6- Aquí tenemos un diccionario de personas. ¡Siéntase libre de modificarlo!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#Comprueba si el diccionario person tiene la clave skills, si es así, imprime la habilidad central (la del medio) de la lista de habilidades.

# 1. Comprobamos si la clave existe (forma directa y rápida)
if 'skills' in person:
    # 2. Obtenemos la lista de habilidades del Heap
    lista_habilidades = person['skills']
    
    # 3. Calculamos el índice central de la LISTA
    n = len(lista_habilidades)
    indice_medio = n // 2  # División entera (ej: 5 // 2 = 2)
    
    # 4. Imprimimos el elemento en esa posición
    print(f"La habilidad central es: {lista_habilidades[indice_medio]}")
else:
    print("La persona no tiene habilidades registradas.")

# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
#       0           1       2         3          4     = 4 // 2 = 2
#                         Muestra                                    

# ['JavaScript', 'React', 'Node', 'MongoDB']
#       0           1       2         3          3     =  3 // 2 = 1
#                Muestra     

#Comprueba si el diccionario person tiene la clave skills, si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.

    #Si las habilidades de la persona son solo JavaScript y React, imprime ('Es un desarrollador front end'); 
    #si las habilidades incluyen Node, Python y MongoDB, imprime ('Es un desarrollador backend'); 
    #si las habilidades incluyen React, Node y MongoDB, imprime ('Es un desarrollador fullstack'); 
    #de lo contrario, imprime ('título desconocido') — ¡para resultados más precisos se pueden anidar más condiciones!

if 'skills' in person:
    skills_list = person['skills']

    if 'Python' in skills_list:
        print('La habilidad es python')
    
    elif 'JavaScript' in skills_list and 'React' in skills_list :
        print('Es un desarrollador front end')

    elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print('Es un desarrollador front end')

    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print('Es un desarrollador front end')
    else:
        print ('título desconocido')

#Si la persona está casada y si vive en Finlandia, imprime la información en el siguiente formato: Asabeneh Yetayeh vive en Finlandia. Está casado.

if person['is_marred'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh vive en Finlandia. Está casado.')