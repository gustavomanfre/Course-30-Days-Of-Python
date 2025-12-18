#💻 EJERCICIOS - DIA 3

#1-Declare su edad como variable entera ✅
edad = 20

#2-Declara tu altura como una variable de flotación ✅
altura = 1.84

#3-Declarar una variable que almacena un número complejo ✅
complex_number = 1 + 1j

#4-Escriba un script que incite al usuario a ingresar la base y la altura del triángulo y calcular un área de este triángulo (área = 0.5 x b x h).✅
b = float(input('Ingresar la base del triangulo')) #Enter base: 20, input devuelve un str, por eso es necesario castearlo a float.
h = float(input('Ingresar la altura')) #Enter height: 10, input devuelve un str, por eso es necesario castearlo a float.
area = 0.5 * b * h #The area of the triangle is 100
print(area)

#5-Escriba un script que incite al usuario a ingresar el lado a, el lado b y el lado c del triángulo. Calcular el perímetro del triángulo (perímetro = a + b + c).✅
a = float(input('Ingresar la base del triangulo')) #Enter side a: 5, input devuelve un str, por eso es necesario castearlo a float.
b = float(input('Ingresar la altura')) # Enter side b: 4, input devuelve un str, por eso es necesario castearlo a float.
c = float(input('Ingresar la altura')) # #Enter side c: 3, input devuelve un str, por eso es necesario castearlo a float.
perimetro = a + b + c #The perimeter of the triangle is 12
print(perimetro)

#6-Obtenga la longitud y el ancho de un rectángulo usando prompt. Calcular su área (área = longitud x anchura) y perímetro (perímetro = 2 x (longitud + ancho)) ✅
    #Python, en su forma básica, está diseñado para funcionar en la Consola o Terminal. No trae "ventanas" o "pop-ups" integrados de forma nativa como un navegador web.
    #En Python (Consola): La interacción es un flujo de texto. print envía texto hacia afuera y input detiene todo para esperar texto hacia adentro.
        # input(): Es la función específica de Python que te permite crear ese prompt y capturar el valor que el usuario introduce.
        # Prompt (o Incitación): Es el concepto. Se refiere al mensaje que se muestra al usuario (como 'Ingresar la base del triangulo') para incitarlo a introducir un valor dentro del input.
a = float(input("Ingresar la longitud del rectangulo"))
b = float(input("Ingresar el ancho de un rectangulo"))
area = a * b
perimetro = 2 * (a * b)

print(area)
print(perimetro)

#7-Obtenga el radio de un círculo usando prompt. Calcule el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14. ✅
        # Constantes: No existe un comando estricto (como const) que "cierre" una variable e impida que cambie. En Python, el concepto de "constante" es un poco diferente al de otros lenguajes.
        # En su lugar, utilizamos una convención social entre programadores. Para declarar una constante, escribimos el nombre de la variable completamente en MAYÚSCULAS (usando guiones bajos para separar palabras).

        # Exponentiation(**): a ** b

PI = 3.14 #Constante
r = float(input("Ingresar el radio del circunferencia"))
area = PI * r * r
a= PI * r **r
c = 2 * PI * r

#8-Calcula la pendiente, x-intercept e y-intercept de y = 2x-2 ✅
m = float(input('Ingresar la pendiente (m): '))
b = float(input('Ingresar el y-intercepto (b): '))

#Calcular x-intercept x = b/m
x = b/m

#Calcular y_intercept y = -b
y = -b

print (x)
print(x)
print(y)

#9-La pendiente es (m = y2-y1/x2-x1). Encuentra la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)
        # El Orden de Operaciones PEMDAS es fundamental en matemáticas y programación, ya que le dice a la computadora qué parte de una expresión debe resolverse primero.
        # PEMDAS: Paréntesis (Paréntesis, corchetes, llaves), Exponentes, Multiplicación, División, Adición (Suma), Sustracción (Resta).
        # Multiplicación y División: Tienen la misma prioridad. Debes resolverlas de izquierda a derecha tal como aparecen en la expresión.
        # Adición y Sustracción: Tienen la misma prioridad. Debes resolverlas de izquierda a derecha tal como aparecen en la expresión.
x1, y1 = 2, 2
x2, y2 = 6, 10

# Pendiente
m = (y2-y1)/(x2-x1)
print(m)

#Distancia Euclidiana: d= √(x2​−x1​)2+(y2​−y1​)2​
import math

# Calculamos las diferencias al cuadrado, exponencial **, la opercacion esponencial x**y

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(d)

#10-Compare las pendientes en las tareas 8 y 9.
        # == (Igualdad de Valor 🤝): Este operador pregunta: "¿Tienen el mismo contenido?"Compara los valores (el contenido) de los objetos.
        #is (Identidad de Objeto 🧠): Este operador pregunta: "¿Son exactamente el mismo objeto en la memoria de la computadora?" Compara las direcciones de memoria (la identidad única) de los objetos.
print((2 == (y2-y1)/(x2-x1)))

#11-Calcular el valor de y (y = x^2 + 6x + 9). Trate de utilizar diferentes valores de x y averiguar en qué valor de x y va a ser 0.
for x in range (-10,11):
   y = x**2 + 6*x + 9

   if y == 0:
      print(f"Se encontró el cero en x = {x}")
      break
   else:
        print("La solucion no se encontro en el valor actual")


#12-Encuentre la longitud de 'pythón' y 'dragón' y haga una declaración de comparación falsa.
p = 'python'
d = 'dragon'

l1 = len(p)
l2 = len(d)

resultado = l1 > l2 

print(f"Longitud de '{p}': {l1}")
print(f"Longitud de '{d}': {l2}")
print(f"¿Es la longitud de '{p}' mayor que la de '{d}'?: {resultado}")

#13-Utilizar operador "and" para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'


#Espero que este curso no esté lleno de jerga. Utilice en el operador para comprobar si la jerga está en la oración.

#No hay un "encendido" tanto en el dragón como en la pitón

#Encuentre la longitud de la pitón de texto y convierta el valor en flotar y conviértalo en cadena

#Incluso los números son divisibles por 2 y el resto es cero. ¿Cómo comprobar si un número está incluso o no usando python?

#Compruebe si la división de piso de 7 por 3 es igual al valor de conversión int de 2.7.

#Compruebe si el tipo de '10' es igual al tipo de 10

#Compruebe si int('9.8') es igual a 10

#Escriba un script que le incite al usuario a ingresar horas y tarifa por hora. ¿Calcular el sueldo de la persona?

        #Enter hours: 40
        #Enter rate per hour: 28
        #Your weekly earning is 1120

#Escriba un script que le incite al usuario a ingresar el número de años. Calcula el número de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años

#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.

    #Escriba un script de Python que muestre la siguiente tabla

'''
        1 1 1 1 1
        2 1 2 4 8
        3 1 3 9 27
        4 1 4 16 64
        5 1 5 25 125
'''

