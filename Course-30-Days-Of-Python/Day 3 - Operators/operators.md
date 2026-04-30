# Booleanos y Operadores en Python

bool es un tipo de dato que solo puede tener dos valores: **True** o **False**. 
En Python, a diferencia de JavaScript, la primera letra es siempre mayúscula.

print(True)    # True
print(False)   # False

Lo que no es obvio hasta que trabajas con código real es que bool en Python es una subclase de int. Esto tiene consecuencias concretas:

print(True + True)    # 2  — True vale 1 como entero
print(True + False)   # 1
print(False + False)  # 0
print(True * 5)       # 5

Esto no es una curiosidad: aparece en código real cuando necesitas contar cuántos elementos de una lista cumplen una condición.

Object
├── Numbers
│   ├── Int (20)    
│   │   ├─── Bool (True, False)
│   ├── Float (35.75)
│   └── complex (1+3j)
├── Set ({2, 4, 6})
├── Dict ({1:'a', 2:'b'})
└── Sequence
    ├── String ('Jessa')
    ├── List ([2, 'a', 5.7])
    └── Tuple ((3, 4.5, 'b'))

numbers = [1, -2, 3, -4, 5]
positives = sum(x > 0 for x in numbers)   # sum() suma los True como 1
print(positives)                          # 3

# Valores truthy y falsy
Todo objeto en Python puede evaluarse como booleano. Los siguientes valores evalúan como False:

bool(0)      # False  — el entero cero
bool(0.0)    # False  — el float cero
bool('')     # False  — string vacío
bool([])     # False  — lista vacía
bool({})     # False  — diccionario vacío
bool(())     # False  — tupla vacía
bool(None)   # False  — ausencia de valor

Cualquier otro valor evalúa como True. Esto se usa constantemente en condicionales:
name = input('Nombre: ')

if name:               # equivale a: if name != ''
    print('Hola', name)
else:
    print('No ingresaste nada')

# Operadores

Operadores de asignación
El operador de asignación básico es =. Asigna el valor del lado derecho a la variable del lado izquierdo. No expresa igualdad matemática.
Los operadores de asignación compuestos combinan una operación aritmética con la asignación. Son shorthand: escriben menos y hacen lo mismo:
pythonx = 10

x += 3     # equivale a: x = x + 3  → x es 13
x -= 3     # equivale a: x = x - 3  → x es 10
x *= 2     # equivale a: x = x * 2  → x es 20
x /= 4     # equivale a: x = x / 4  → x es 5.0  (siempre devuelve float)
x //= 2    # equivale a: x = x // 2 → x es 2    (división entera)
x %= 3     # equivale a: x = x % 3  → x es 2    (resto)
x **= 3    # equivale a: x = x ** 3 → x es 8    (potencia)

# Operadores aritméticos
Python tiene siete operadores aritméticos. La mayoría son intuitivos, pero tres merecen explicación detallada.

print('Addition: ', 1 + 2)         # 3  — suma
print('Subtraction: ', 2 - 1)      # 1  — resta
print('Multiplication: ', 2 * 3)   # 6  — multiplicación
print('Division: ', 4 / 2)         # 2.0 — división: SIEMPRE devuelve float en Python 3
print('Division: ', 7 / 2)         # 3.5
print('Division: ', 6 / 2)         # 3.0 — aunque sea exacta, devuelve float
print('Floor division: ', 7 // 2)  # 3   — división entera: descarta el decimal (trunca)
print('Floor division: ', 7 // 3)  # 2
print('Modulus: ', 3 % 2)          # 1   — resto de la división entera
print('Exponentiation: ', 2 ** 3)  # 8   — potencia: 2 * 2 * 2

División / vs división entera //
Este es uno de los cambios más importantes de Python 2 a Python 3. En Python 3, / siempre devuelve float:
pythonprint(4 / 2)     # 2.0  — no 2
print(7 / 2)     # 3.5
print(7 // 2)    # 3    — trunca hacia abajo (floor), no redondea
print(-7 // 2)   # -4   — trunca hacia abajo, no hacia cero
                         # -3.5 truncado hacia abajo es -4, no -3
                         # este comportamiento sorprende si vienes de otros lenguajes
Operador módulo %
Devuelve el resto de la división entera. Sus usos más comunes en código real:
pythonprint(10 % 3)    # 1  — 10 = 3*3 + 1, el resto es 1
print(10 % 2)    # 0  — 10 es divisible por 2, resto 0

# Verificar si un número es par o impar
numero = 7
print(numero % 2 == 0)    # False → es impar
print(numero % 2 != 0)    # True  → es impar

# Verificar divisibilidad
print(15 % 5 == 0)        # True → 15 es divisible por 5
Operador exponente **
print(2 ** 3)     # 8   — 2 elevado a la 3
print(2 ** 0.5)   # 1.4142... — raíz cuadrada: elevar a 0.5 es equivalente
print(10 ** -1)   # 0.1 — potencias negativas también funcionan

# Ejemplos con variables
a = 3    # a es una variable que apunta al entero 3
b = 2    # b es una variable que apunta al entero 2

total        = a + b     # 5  — suma
diff         = a - b     # 1  — resta
product      = a * b     # 6  — multiplicación
division     = a / b     # 1.5 — división, devuelve float
remainder    = a % b     # 1  — resto
floor_division = a // b  # 1  — división entera
exponential  = a ** b    # 9  — 3 elevado a la 2

# Nota: el documento usa 'total' en lugar de 'sum' intencionalmente
# 'sum' es el nombre de una función built-in
# si usas sum = a + b, sobreescribes esa función en tu namespace
# y sum([1,2,3]) dejará de funcionar en ese scope
# esta es una convención importante: nunca uses nombres de built-ins como variables

print('a + b = ', total)          # 'a + b = ' es una etiqueta para identificar la salida
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Aplicaciones prácticas
# Área de un círculo
radius = 10
area_of_circle = 3.14 * radius ** 2    # ** tiene mayor precedencia que *
                                        # Python evalúa radius ** 2 primero (100)
                                        # luego multiplica por 3.14
                                        # resultado: 314.0
print('Area of a circle:', area_of_circle)

# Área de un rectángulo
length = 10
width = 20
area_of_rectangle = length * width     # 200
print('Area of rectangle:', area_of_rectangle)

# Peso de un objeto (Fuerza = masa × gravedad)
mass = 75       # kilogramos
gravity = 9.81  # m/s² — aceleración gravitacional estándar
weight = mass * gravity                # 735.75
print(weight, 'N')                     # 'N' es la unidad (Newtons), se concatena como segundo argumento de print

# Densidad de un líquido (densidad = masa / volumen)
mass = 75        # Kg — reutilizamos el nombre 'mass', apunta a un nuevo objeto
volume = 0.075   # metros cúbicos
density = mass / volume                # 1000.0 Kg/m³
print(density, 'Kg/m^3')              # 'Kg/m^3' es la unidad como string

La nota sobre precedencia de operadores es importante. Python evalúa las operaciones en este orden (de mayor a menor precedencia):

# Orden de precedencia (PEMDAS)
1. Paréntesis ()
2. Exponente **
3. Multiplicación *, División /, //, %
4. Suma +, Resta -

print(2 + 3 * 4)       # 14  — multiplica primero: 2 + 12
print((2 + 3) * 4)     # 20  — paréntesis primero: 5 * 4
print(2 ** 3 + 1)      # 9   — exponente primero: 8 + 1
print(2 ** (3 + 1))    # 16  — paréntesis primero: 2 ** 4
Cuando tengas dudas sobre precedencia, usa paréntesis. Hacen el código más legible y eliminan ambigüedad.

# Operadores de comparación
Los operadores de comparación evalúan una expresión y devuelven True o False. Son la base de toda lógica condicional.

print(3 > 2)      # True  — 3 es mayor que 2
print(3 >= 2)     # True  — 3 es mayor o igual que 2
print(3 < 2)      # False — 3 no es menor que 2
print(2 < 3)      # True  — 2 es menor que 3
print(2 <= 3)     # True  — 2 es menor o igual que 3
print(3 == 2)     # False — 3 no es igual a 2
                           # == compara valores, no es asignación
print(3 != 2)     # True  — 3 es distinto de 2

También se pueden comparar resultados de funciones directamente:

print(len('mango') == len('avocado'))   # False — 5 == 7
print(len('mango') != len('avocado'))   # True  — 5 != 7
print(len('mango') < len('avocado'))    # True  — 5 < 7
print(len('milk') == len('meat'))       # True  — 4 == 4
print(len('tomato') == len('potato'))   # True  — 6 == 6
print(len('python') > len('dragon'))    # False — 6 > 6 es False, son iguales

Y comparar booleanos entre sí:

print(True == True)    # True
print(True == False)   # False
print(False == False)  # True

# OPERADOR "IN"
En Python, el operador in se define técnicamente como un operador de pertenencia (membership operator). 
Su función principal es validar si un objeto (el operando de la izquierda) se encuentra contenido dentro de un iterable o colección (el operando de la derecha). 

1. Operador de Pertenencia (Evaluación Booleana)
En este contexto, in evalúa una expresión y devuelve un valor de tipo bool (True o False). 
Es altamente eficiente para verificar la existencia de datos sin necesidad de iterar manualmente.

    -En Colecciones (Listas, Tuplas, Sets): Compara el objeto contra cada elemento de la colección mediante el operador de igualdad ==.
        items = [10, 20, 30]
        is_present = 20 in items  # True

    -En Cadenas (Strings): Verifica si una subcadena está contenida dentro de otra. A diferencia de las listas, aquí busca una secuencia de caracteres.
        "py" in "python"  # True
    
    -En Diccionarios: Por defecto, in verifica la existencia de llaves (keys), no de valores.
        data = {"id": 1, "name": "Gemini"}
        "id" in data       # True (verifica llaves)
        "Gemini" in data   # False (no verifica valores directamente)

2. Estructura de Control: Bucle for...in
En el ámbito de los bucles, in no actúa como un comparador, sino como un conector lógico que vincula una variable local con un objeto iterable.
    -Bucle for ... in 
        for element in iterable:
            # Bloque de código

Aquí, in instruye al intérprete para llamar al método interno _iter_() del objeto y asignar secuencialmente cada valor a la variable definida hasta agotar la secuencia

3. Comprensión de Listas (List Comprehensions)
    # Genera una lista de cuadrados solo para números pares
    cuadrados = [n**2 for n in range(10) if n % 2 == 0]

4. Operador Negado not in
Es la contraparte lógica. Se prefiere por legibilidad sobre la negación manual de la expresión (not x in y).
    -Operador negado "In"
        user_status = "banned"
        if user_status not in ["active", "pending"]:
        print("Acceso denegado")

# is, is not, in, not in
Estos cuatro operadores se ven similares a == y != pero tienen semántica diferente y es importante no confundirlos.

# is e is not: identidad de objeto
== compara valores. is compara identidad: si ambas variables apuntan exactamente al mismo objeto en memoria.
print(1 is 1)       # True  — los enteros pequeños son cacheados por Python
                    # ambos '1' apuntan al mismo objeto en memoria
print(1 is not 2)   # True  — 1 y 2 son objetos distintos

# La distinción entre == e is es crítica:
pythona = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  — tienen los mismos valores
print(a is b)    # False — son objetos distintos en memoria (aunque con igual contenido)
print(a is c)    # True  — c y a apuntan al mismo objeto

En la práctica: usa == para comparar valores. Usa is solo para comparar con None, que es el caso idiomático en Python:

result = None
if result is None:     # correcto — None es un singleton, siempre hay uno solo
    print('Sin resultado')

if result == None:     # funciona pero no es idiomático
    print('Sin resultado')

# in y not in: pertenencia
Verifican si un elemento existe dentro de una secuencia (string, lista, tupla, diccionario, set):
print('A' in 'Asabeneh')          # True  — 'A' existe en el string
print('B' in 'Asabeneh')          # False — no hay 'B' mayúscula
                                            # in en strings es case-sensitive
print('coding' in 'coding for all')   # True  — busca la subcadena completa
print('a' in 'an')                  # True

# En listas
skills = ['Python', 'JavaScript', 'SQL']
print('Python' in skills)         # True
print('Java' in skills)           # False — 'Java' != 'JavaScript'

# En diccionarios: in verifica las keys, no los values
person = {'name': 'Juan', 'age': 30}
print('name' in person)           # True  — 'name' es una key
print('Juan' in person)           # False — 'Juan' es un value, no una key
print(4 is 2 ** 2)    # True — 2**2 evalúa a 4, y 4 es un entero pequeño cacheado

# Operadores lógicos
Python usa palabras en inglés para los operadores lógicos: and, or, not. No usa &&, ||, ! como otros lenguajes.

# and: devuelve True solo si AMBAS condiciones son True
print(3 > 2 and 4 > 3)    # True  — ambas son True
print(3 > 2 and 4 < 3)    # False — la segunda es False
print(3 < 2 and 4 < 3)    # False — ambas son False
print(True and True)       # True

# or: devuelve True si AL MENOS UNA condición es True
print(3 > 2 or 4 > 3)     # True  — ambas son True
print(3 > 2 or 4 < 3)     # True  — la primera es True, alcanza con una
print(3 < 2 or 4 < 3)     # False — ambas son False
print(True or False)       # True

# not: invierte el valor booleano
print(not 3 > 2)     # False — 3 > 2 es True, not True es False
print(not True)      # False
print(not False)     # True
print(not not True)  # True  — doble negación: not(not True) = not False = True
print(not not False) # False — not(not False) = not True = False

# Cortocircuito en and y or
Este es un comportamiento importante que afecta tanto la lógica como el rendimiento. Python evalúa las expresiones de izquierda a derecha y se detiene en cuanto puede determinar el resultado:

- and se detiene en el primer False que encuentra
- or se detiene en el primer True que encuentra

# Con and: si el primero es False, el segundo no se evalúa
print(False and 1/0)    # False — no evalúa 1/0, no lanza ZeroDivisionError

# Con or: si el primero es True, el segundo no se evalúa
print(True or 1/0)      # True  — no evalúa 1/0, no lanza ZeroDivisionError

Esto se aprovecha en patrones comunes:
- Valor por defecto si la variable es falsy

name = input('Nombre: ') or 'Anónimo'

# si input devuelve '' (string vacío, falsy), or evalúa el segundo operando
# si input devuelve algo, or devuelve ese algo sin evaluar el segundo

# Verificación segura antes de acceder a un atributo
user = None
name = user and user['name']    # si user es None (falsy), and devuelve None
                                 # no intenta acceder a user['name'] y no lanza error
Combinar operadores de comparación
Python permite encadenar comparaciones de una forma que otros lenguajes no soportan:
pythonage = 25

# En otros lenguajes necesitas:
print(age >= 18 and age <= 65)    # True

# En Python puedes encadenarlos directamente:
print(18 <= age <= 65)            # True — más legible, equivalente al anterior

x = 5
print(1 < x < 10)                 # True  — x está entre 1 y 10
print(1 < x < 4)                  # False — 5 no es menor que 4

# OPERADOR "==" E "IS"
En Python, "==" e "is" se usan para comparar, operan en niveles diferentes de la realidad de un programa.

    -Operador == (Igualdad) 💰: Compara los valores (el contenido) de los objetos.
    -Operador is (Identidad) 🆔: Compara la identidad u ubicación en memoria. 
     Se pregunta: "¿Estas dos variables apuntan exactamente al mismo objeto físico en la memoria RAM?".
     Aquí Python revisa la identidad (su lugar en la memoria).

_________________________________________________________________________________________________________________________________
# CASTEO DE DATOS.

El "casteo" o conversión de tipos en Python es el proceso de transformar el valor de una variable de un tipo de dato a otro. 
A diferencia de otros lenguajes, en Python esto se hace utilizando las funciones constructoras de los tipos de datos básicos.

Las Funciones de Conversión Principales 🧬

Python tiene funciones integradas para los tipos de datos más comunes:

Función     Descripción                                              Ejemplo
int()       Convierte a un número entero.,                          "int(""10"") ➡️ 10"
float()     Convierte a un número de punto flotante (decimal).      float(5) ➡️ 5.0
str()       Convierte cualquier objeto en una cadena de texto.      "str(100) ➡️ ""100"""
bool()      Convierte a un valor booleano (True o False).           bool(1) ➡️ True

El proceso de "casteo" o conversión de tipos ocurre cuando el intérprete de Python intenta transformar una representación de datos en otra utilizando una función constructora.

En Python, los tipos de datos básicos como int, str o float no son simples etiquetas, sino clases predefinidas que se cargan automáticamente al iniciar el intérprete desde el módulo builtins.

Cuando haces un "casteo", estás realizando una instanciación: creas un nuevo objeto de esa clase. 
Vamos a profundizar en ese camino interno que mencionaste, específicamente en dónde viven esas declaraciones y cómo se decide si el proceso tiene éxito. 🧭

1. ¿Dónde están declaradas estas clases? 🏗️
Estas clases están declaradas en el núcleo de Python (escrito mayoritariamente en C para la implementación estándar CPython).
    -Módulo builtins: Todas las funciones y clases fundamentales como int(), list() o dict() residen aquí. No necesitas importarlas porque Python las pone en el ámbito global por defecto.
    -C-API de Python: Internamente, el constructor de int apunta a una estructura en C llamada PyInt_Type (o PyLong_Type en Python 3), que define cómo se debe crear ese objeto desde diferentes tipos de entrada.

2. El Protocolo de Conversión (El "Contrato") 🤝
El constructor no solo "mira" el dato, sino que busca métodos especiales dentro del objeto que le pasas.
    -Si intentas int(objeto), Python busca si objeto tiene un método llamado __int__.
    -Si intentas str(objeto), busca el método __str__.
Esto permite que la "Verificación de Compatibilidad" que mencionaste sea muy flexible: el objeto de origen es el que suele saber cómo convertirse al tipo de destino.

3. La Memoria: Inmutabilidad en Acción 🧊
Un detalle técnico crucial es que los tipos básicos en Python son inmutables.
    -Cuando haces y = int("45"), Python no transforma la cadena "45".
    -En su lugar, la cadena original permanece intacta y se crea un objeto completamente nuevo en una dirección de memoria diferente para el entero 45.
_________________________________________________________________________________________________________________________________________________________________________________________

# Tipos de Conversión 🔄
Existen dos formas en las que esto sucede:

    -Conversión Implícita (Coerción): Python lo hace automáticamente para evitar pérdida de datos. Por ejemplo, si sumas un entero y un flotante (5 + 2.0), Python convierte el 5 en 5.0 internamente.
    -Conversión Explícita (Casting): Es cuando tú fuerzas el cambio usando las funciones que mencionamos antes (str(), int(), etc.).
_________________________________________________________________________________________________________________________________________________________________________________________

# El Operador Ternario (Condicional en una línea)
        #[valor_si_cierto] if [condición] else [valor_si_falso]
        #"Even": Es el resultado si la condición es verdadera.
        #if ... % 2 == 0: Es la evaluación lógica (si el residuo de la división por 2 es cero).
        #else "Odd": Es el camino de salida si la condición es falsa.
_________________________________________________________________________________________________________________________________________________________________________________________

input("Enter integer: "):
Función: Detiene la ejecución para capturar la entrada del usuario por teclado.
Dato importante: Siempre devuelve un tipo str (cadena de texto), incluso si el usuario escribe un número.

_________________________________________________________________________________________________________________________________________________________________________________________