# Variables

# Reglas de nomenclatura

# ✅ Nombres válidos

first_name      # Snake_case: estándar en Python para variables y funciones
age             # Pueden comenzar en minusculas, por convencion no deberian comenzar en mayusculas
_if             # Puede iniciar con guión bajo al inicio: convención para usar palabras reservadas como nombre
year_2021       # Puede contener números, pero no empezar con uno.

# ❌ Nombres inválidos

first-name      # Guión medio no está permitido, Python lo interpreta como resta.
first@name      # @ No está permitido en nombres de variables.
1num            # No puede empezar con un número

La convención oficial de Python (PEP 8) para variables y funciones es **snake_case**: Todas las palabras en minúscula separadas por guiones bajos. 
Es la convención adoptada por la comunidad y por todas las librerías estándar.

# ✅ Convención Python (snake_case)
first_name = "Juan"
engine_rotation_speed = 3000

# ❌ Otras convenciones que NO se usan en Python para variables.
firstName = "Juan"      # camelCase: se usa en JavaScript, no en Python
FirstName = "Juan"      # PascalCase: se reserva para nombres de clases en Python
__________________________________________________________________________________________________________________________________________________________________

# ✅ 1. Variables en Python.
En Python, no existen los tipos de datos primitivos en el sentido estricto (como en C o Java). Todos los tipos de datos son objetos.
Una variable en python es un objeto con metodo y propiedades que se almacena en el heap.

╔══════════════════════════════════╗
║            OBJETO                ║
╠══════════════════════════════════╣
║ Identidad (id)                   ║
║ Tipo/clase                       ║
║ Valor interno                    ║
║ Atributos                        ║
║ Métodos                          ║
║ Métodos mágicos (dunder)         ║
║ Diccionario interno (__dict__)   ║
║ Slots internos (si existen)      ║
╚══════════════════════════════════╝

Todo en Python es un objeto: números, funciones, módulos, clases, tipos, listas, excepciones, etc.
obj = [1, 2, 3]

print("Tipo:", type(obj))   #type() → clase del objeto
Tipo: <class 'list'>

print("ID:", id(obj))       #id() → dirección en memoria (o referencia única)
ID: 140045331029264

print("Valor interno:", obj) #Valor interno → lo que contiene el objeto
Valor interno: [1, 2, 3]

print(dir(obj))             #Esto muestra todos los atributos, métodos mágicos, métodos disponibles, etc.
['__add__', '__class__', '__contains__', ..., 'append', 'clear', 'copy', 'extend', ...]

print(obj.__dict__)         #Muchos objetos en Python tienen un diccionario interno donde guardan atributos. Esto es normal: las listas optimizan memoria y no tienen __dict__.
AttributeError: 'list' object has no attribute '__dict__'

help(obj)                   #Esto muestra toda la documentación oficial del tipo.

print(obj.__class__)        # Para ver la clase del objeto, indican que las listas heredan de object.

print(obj.__class__.mro())  #Method Resolution Order (orden de herencia)
[<class 'list'>, <class 'object'>]

import inspect
print(inspect.getmembers(obj)) #muestra todo: métodos, atributos, valores internos, funciones heredadas, funciones mágicas

# Inspeccionar un objeto totalmente.
import inspect

def inspeccionar(o):
    print("=== INSPECCIÓN DE OBJETO ===")
    print("Tipo:", type(o))
    print("ID:", id(o))
    print("Valor interno:", repr(o))
    print("\nAtributos y métodos:")
    print(dir(o))
    print("\nAtributos del objeto (si existen):")
    print(getattr(o, "__dict__", "No tiene __dict__"))
    print("\nMRO (Jerarquía):")
    print(type(o).mro())
    print("\nMétodos:")
    print([m for m in dir(o) if callable(getattr(o, m))])
    print("\nAtributos no llamables:")
    print([a for a in dir(o) if not callable(getattr(o, a))])
obj = [1, 2, 3]
inspeccionar(obj)

# Declaración y asignación
first_name = 'Asabeneh'      # str: cadena de texto
age = 250                    # int: número entero
is_married = True            # bool: valor booleano, True o False con mayúscula inicial
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']   # list: colección ordenada
person_info = {                                     # dict: colección clave-valor
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# ✅ 2. En Python, una variable es simplemente un nombre que referencia un objeto en memoria.
    - Se crea un objeto de tipo int con valor 10.
    - El nombre x apunta a ese objeto.
         x = 10

# ✅ 3. Variables y mapeo en memoria.

Una variable es un nombre que apunta a un objeto almacenado en memoria. En Python, las variables no tienen tipo: el tipo lo tiene el objeto al que apuntan. 
Esto significa que la misma variable puede apuntar a un objeto entero ahora y a un objeto cadena después.

x = 10      # x apunta a un objeto int con valor 10
x = "hola"  # ahora x apunta a un objeto str — esto es válido en Python

Esto contrasta con lenguajes como Java o C donde declaras el tipo de la variable y no puede cambiar.

**Ejemplo** 
x = 10
y = 10
x = y
x = 20

Analicemos paso por paso:

x = 10
x → objeto 10 // x contiene referencia (apuntan) a objeto 10

y = 10
Como los enteros pequeños están internados (“interning”), Python reutiliza el mismo objeto:
y → objeto 10 // x e y contienen referencia (apuntan) al mismo objeto 10

x = 20
Ahora x contiene referencia (apunta) a un nuevo objeto 20, y sigue apuntando a 10.
x → 20
y → 10

_____________________________________________________________________________________________________________________________________________________________________________________________

# El Mapeo de Memoria: Stack vs. Heap 🛠️.

En CPython, la memoria se divide principalmente en dos áreas: 
    - El **Stack** (pila) 
    - El **Heap** (montículo)

Vamos a realizar el mapeo técnico de qué sucede exactamente cuando ejecutas una instrucción simple como x = 5.

# 1. En el Stack (Pila de Llamadas)
El Stack almacena los marcos de referencia (frames). Cuando declaras x, no se guarda el número 5 ahí. 
Se guarda una referencia (un puntero de 8 bytes en sistemas de 64 bits).

    Variable: x
    Contenido: 0x10A2 (Una dirección de memoria que apunta al Heap).

# 2. En el Heap (Montículo de Objetos)

Aquí es donde reside el objeto real. En la dirección 0x10A2, no solo hay un "5", hay una estructura compleja de C llamada PyLongObject (para los enteros).

# Anatomía de un Objeto Entero en el Heap 🧬 

[Ver **Variables en Python.**]

# ¿Por qué esto es relevante para el rendimiento? 🏎️

-Indirección: Cada vez que accedes a x, Python debe:
    -Ir al Stack para buscar la dirección.
    -Saltar al Heap en esa dirección.
    -Leer el ob_type para saber qué operaciones están permitidas.
    -Finalmente, acceder al valor.
    -Esto explica por qué Python es más lento que C (donde el 5 estaría directamente en el Stack).

-Inmutabilidad: Si haces x = x + 1, Python no cambia el valor en el Heap. Crea un nuevo objeto (por ejemplo en 0x20B4) con el valor 6, y actualiza la referencia en el Stack de x para que apunte a la nueva dirección. El objeto viejo (5) reduce su ob_refcnt.

4. Visualización del mapeo Stack-Heap con Métodos
Si tenemos x = [1, 2]:
    -Stack: x -> 0xABC (Dirección en el Heap).
    -Heap (Instancia 0xABC):
        ob_refcnt: 1
        ob_type: 0x999 (Puntero a la clase list).
        ob_item: Puntero a los datos [1, 2].
    -Heap (Clase list en 0x999):
        __add__: Puntero a código binario de suma.
        append: Puntero a código binario de inserción.
        __len__: Puntero a código que lee el tamaño.
____________________________________________________________________________________________________________________________________________________________________________________________

# La Función print(): La Anatomía de la Salida.
La firma técnica es: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

-*objects (Argumentos posicionales): El asterisco significa que puedes pasar N objetos. Python llamará internamente a str(objeto) para cada uno antes de imprimirlos.
-sep (Separador): Lo que se inyecta entre cada objeto. Por defecto es un espacio ' '.
-end (Finalizador): Lo que se inyecta al final de la línea. Por defecto es \n (salto de línea). Si quieres imprimir en la misma línea varias veces, cámbialo a end=''.
-file (El destino): Por defecto es sys.stdout (la pantalla). Pero aquí podrías pasar un archivo abierto. 
        Dato Senior: print es solo un envoltorio elegante sobre el método .write() de cualquier objeto que se comporte como un archivo.
-flush (Vaciado de búfer): Normalmente, Python guarda los caracteres en memoria antes de mandarlos a la pantalla para ahorrar recursos. 
        Si flush=True, obliga al sistema a mostrarlo ahora mismo. Vital para barras de carga.
____________________________________________________________________________________________________________________________________________________________________________________________

# Casting: conversión entre tipos
Casting es convertir un objeto de un tipo a otro. Python no hace conversiones implícitas entre tipos incompatibles, a diferencia de JavaScript. Si intentas sumar un número y un string sin convertir, obtienes un TypeError.
python# int → float
num_int = 10
num_float = float(num_int)      # float() crea un nuevo objeto float a partir del int
print(num_float)                # 10.0 — agrega el decimal para representarlo como float

# float → int
gravity = 9.81
print(int(gravity))             # 9 — trunca la parte decimal, NO redondea
                                # int(9.99) devuelve 9, no 10
                                # si necesitas redondear usa round(gravity)

# int → str
num_int = 10
num_str = str(num_int)          # str() convierte el int al string '10'
print(num_str)                  # '10' — ya no es un número, es texto
print(num_str + '5')            # '105' — concatenación de strings, no suma aritmética

# str → float o int
num_str = '10.6'
num_float = float(num_str)      # float() parsea el string y crea un objeto float
                                # funciona solo si el string representa un número válido
                                # float('hola') lanza ValueError

num_int = int(num_float)        # int() trunca el float a entero
print(num_int)                  # 10

No puedes hacer int('10.6') directamente
int() no puede parsear un string con decimal
debes pasar primero por float: int(float('10.6'))
print(int(float('10.6')))       # 10

# str → list
first_name = 'Asabeneh'
first_name_to_list = list(first_name)   # list() sobre un string itera sobre cada caracter
                                         # y crea una lista con cada uno como elemento
print(first_name_to_list)
# ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

# Errores comunes en casting
int('10.6')         # ValueError: no puede convertir directamente un str con decimal a int
int('hola')         # ValueError: 'hola' no representa un número
float('10,6')       # ValueError: Python usa punto decimal, no coma
bool(0)             # False — en Python, 0, '', [], {}, None son falsy (evalúan a False)
bool(1)             # True  — cualquier valor no vacío y no cero es truthy

El concepto de valores truthy y falsy es importante: Python evalúa como False a 0, 0.0, '', [], {}, None, y como True a cualquier otro valor. 

Esto se usa constantemente en condicionales:

name = input('Nombre: ')
if name:              # equivale a if name != '' — si el usuario escribió algo
    print('Hola', name)
else:
    print('No ingresaste nombre')