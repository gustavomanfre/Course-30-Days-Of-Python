#EJERCICIOS - DIA 2

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicios: Nivel 1

#   Dentro de 30DaysOfPython crear una carpeta llamada day_2. Dentro de esta carpeta crear un archivo llamado variables.py.✅

#   Escriba un comentario de python diciendo 'Día 2: 30 días de programación de python'✅
'''Dia 2: 30 dias de programacion de Python'''

#    Declarar una variable de nombre y asignarle un valor.✅
nombre = 'Gustavo' # Tipo de dato str

#    Declarar una variable de apellido y asignarle un valor.✅
apellido = 'Manfredi' #Tipo de dato str

#    Declarar una variable de nombre completo y asignarle un valor.✅
nombre_completo = 'Gustavo Manfredi'

#    Declarar una variable de país y asignarle un valor.✅
pais= 'Argentina'

#    Declarar una variable de ciudad y asignarle un valor.✅
ciudad = 'Mendoza'

#    Declarar una variable de edad y asignarle un valor.✅
edad = 30

#    Declarar una variable de un año y asignarle un valor.✅
año = 1995

#    Declarar una variable is_married y asignarle un valor.✅
is_married = False

#    Declarar una variable is_true y asignarle un valor.✅
is_true = True

#    Declarar una variable is_light_on y asignarle un valor.✅
is_light_on = True

#    Declarar varias variables en una línea.✅
a,b,c,d,e = 1,2,3,4,5

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicios: Nivel 2

#    Compruebe el tipo de datos de todas sus variables utilizando la función integrada type().✅
print(type(nombre)) #string
print(type(apellido)) #string
print(type(nombre_completo))#string
print(type(pais))#string
print(type(ciudad))#string
print(type(edad))# int
print(type(is_married))#boolean
print(type(is_true ))#boolean
print(type(is_light_on))#boolean
print(type(a), type(b), type(c), type(d), type(e))#int

#    Usando la función integrada len(), encuentra la longitud de tu nombre.✅
print(len(nombre))

#    Compara la longitud de tu nombre y tu apellido.✅
are_equal = len(nombre)== len(apellido)

#    Declarar 5 como num_one y 4 como num_two.✅
num_one = 5
num_two = 4

#    Añadir num_one y num_two y asignar el valor a una variable total.✅
total = num_one + num_two

#    Restar num_two de num_one y asignar el valor a una variable diff.✅
diff = num_one - num_two

#    Multiplicar num_two y num_one y asignar el valor a un producto variable.✅
producto = num_one*num_two

#    Divida num_one por num_two y asigne el valor a una división variable.✅
division = num_one/num_two

#    Utilice la división de módulos para encontrar num_two dividido por num_one y asignar el valor a una variable restante.✅
restante = num_one%num_two

#    Calcular num_one a la potencia de num_two y asignar el valor a una variable exp.✅
exp = num_one**num_two

#    Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division.✅
floor_division = num_one // num_two

#    El radio de un círculo es de 30 metros.
#    i.Calcular el área de un círculo y asignar el valor a un nombre variable de area_of_circle.✅
area_of_circle = 3.14 * (30**2)

#    ii.Calcula la circunferencia de un círculo y asigna el valor a un nombre variable de circum_of_circle.✅
circum_of_circle = 2*3.14*30

#    iii.Tome el radio como entrada del usuario y calcule el área.✅
radio_str = input('Ingresar radio del circulo: ')
radio = float(radio_str) # Convertir la cadena a un número decimal
area_of_circle = 3.14 * (radio ** 2)

#    Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variable correspondientes.✅

nombre = input(('nombre')) #string
apellido = input(('apellido')) #string
nombre_completo = input(('nombre_completo'))#string
pais = input(('pais'))#string
ciudad = input(('ciudad'))#string
edad = int(input('Ingresa tu edad: '))
respuesta_matrimonio = input('¿Estás casado? (si/no): ')
is_married = (respuesta_matrimonio.lower() == 'si') # Devuelve True o False

#    Ejecute help('keywords') en Python shell o en su archivo para comprobar si hay palabras o palabras clave reservadas de Python.✅
'PYTHON SHELL'
'Desktop:~$ /usr/bin/python3'
'help '('keywords')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#