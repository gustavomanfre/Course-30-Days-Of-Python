# Introduction.
# Day 1 - 30Days Of Python Challenge

# Comentarios
El operador para realizar comentarios es el siguiente # en el codigo.

# Python Tipo de Datos Primitivos.
Python es un lenguaje de tipo dinámico; por lo tanto, no necesitamos especificar el tipo de la variable mientras la declaramos. Cualquier valor que asignemos a la variable en función de ese tipo de datos se asignará automáticamente.

Object
├── Numbers
│   ├── Int (20)
│   ├── Float (35.75)
│   └── complex (1+3j)
├── Bool (True, False)
├── Set ({2, 4, 6})
├── Dict ({1:'a', 2:'b'})
└── Sequence
    ├── String ('Jessa')
    ├── List ([2, 'a', 5.7])
    └── Tuple ((3, 4.5, 'b'))


# Tipos de datos secuencia.

Para que Python considere algo una secuencia, debe cumplir estas reglas:
    - Orden Posicional: Los elementos tienen un lugar fijo (primero, segundo, tercero).
    - Indexación Numérica: Puedes acceder a ellos usando un número entero (índice), como datos[0].
    - Slicing (Slices): Puedes pedir un "rango" de elementos, como datos[1:4].

Por eso el String, la Lista y la Tupla son secuencias: en las tres importa quién va primero y quién después.

# Tipos No secuenciales.

**Diccionario (dict)**
Es un tipo Mapping (clave:valor), no una secuencia.
    - La razón: No accedes a los datos por su posición (0, 1, 2), sino por una clave (key).
    - Si intentas hacer mi_diccionario[0], Python buscará una clave que sea literalmente el número 0, no el primer elemento guardado. 
    Aunque en versiones modernas de Python los diccionarios mantienen el orden de inserción, su lógica interna sigue siendo de "etiquetas", no de "posiciones".

**Conjunto (set)**
Es una Colección Desordenada.
    - La razón: Un set es como una bolsa de canicas. No hay un "primer" o "último" elemento de forma garantizada.
    - No admite índices ni cortes (slicing). 
    - Su función es guardar elementos únicos y permitir operaciones matemáticas como la unión o intersección, pero no le importa el orden.

**Booleano (bool)**
Es un tipo Escalar (un solo valor).
    - La razón: Para ser una secuencia, necesitas ser un contenedor de múltiples elementos. 
    - El booleano es simplemente un estado lógico: True o False (1 o 0). 
    - No puedes pedir "el primer elemento de un True", porque no hay nada adentro; el valor es el dato en sí.

# Comprobacion de Tipo de Datos

# Numbers
print(type(10))                  **Int**: tipo de datos int para representar valores enteros completos.
                                 - La principal característica del tipo de dato int en Python es que, a diferencia de muchos otros lenguajes de programación (como C, C++ o Java, donde los enteros tienen límites fijos de 32 o 64 bits), los enteros en Python3 no tienen un límite de tamaño fijo.
id = int(25)                     - Tambien podemos crear una variable entera de la siguiente forma: Usando un casteo  de clase int().
                                - TAMAÑO: Dinámico. En Python 3, los enteros tienen una precisión arbitraria. Ocupan un mínimo de 28 bytes y crecen según el tamaño del número.
                                - RANGO: No tiene un límite fijo (está limitado solo por la memoria RAM disponible de tu computadora).

print(type(3.14))               **Float**: tipo de datos para representar valores de punto flotante o valores decimales.
num = float(54.75)              - Tambien podemos crear una variable numero decimal de la siguiente forma: Usando un float()Clase.
                                - TAMAÑO: Generalmente 24 a 32 bytes como objeto de Python.
                                - RANGO: Sigue el estándar IEEE 754 (64 bits). Aproximadamente de ±2.23×10−308 a ±1.80×10308.

print(type(1 + 3j))              **Complex**: tipos de datos Complex para representar número complejo es un número con un componente real e imaginario        
                                - Representado como a+b, dónde a y b contienen enteros o valores de punto flotante.
                                - TAMAÑO: Aproximadamente 32 bytes (almacena dos floats internamente).
                                - RANGO: El mismo que el de dos floats combinados.

# Sequence
print(type('Asabeneh'))          **String**: El string es una secuencia de caracteres (letras, números, símbolos o espacios) que se utiliza para representar texto.
                                    - SINTAXIS: 'xxx', "xxx" o '''xxxx''' (las comillas triples se usan para textos de varias líneas).
                                    - ORDENADO: Al ser una secuencia, cada carácter tiene un índice único basado en su posición.
                                        El primer carácter es cadena[0].
                                        El último carácter es cadena[-1].
                                        Permite slicing (extraer trozos), por ejemplo: cadena[0:4].
                                    - HOMOGÉNEO: A diferencia de las listas, un string solo contiene caracteres. 
                                        Aunque pongas un número dentro ("123"), para Python sigue siendo un carácter de texto, no un tipo numérico.
                                    - DUPLICADOS: Puede tener caracteres repetidos sin ninguna restricción (ejemplo: "aaaaa").
                                    - INMUTABLE: No puedes modificar un carácter individual una vez creado el string.
                                    - TAMAÑO: Depende de la longitud y la codificación. Python usa optimización (PEP 393), donde cada carácter puede ocupar 1, 2 o 4 bytes. 
                                        Un string vacío ocupa unos 49-50 bytes.
                                    - RANGO: Limitado por la RAM. Puedes tener strings de millones de caracteres si tienes memoria.

                                    Ejemplo: Si tienes nombre = "Asabeneh", no puedes hacer nombre[0] = "B". Para cambiarlo, tendrías que generar un string totalmente nuevo.

print(type([1, 2, 3]))           **List**: La lista de Python es una colección ordenada (también conocida como una secuencia) de elementos.
                                    SINTAXIS: [xxx,xxxx,xxx]
                                    -ORDENADO: Cada elemento tiene un valor de índice único. Los nuevos elementos se añadirán al final de la lista. 
                                        El primer elemento siempre tiene el índice 0. lista[i] donde i≥0. 
                                        El último elemento siempre tiene el índice -1. lista[-i] donde i≥1.
                                    - HETEROGÉNEO: La lista pueden contener elementos tipos Numéricos (int, float,complex), tipo de texto (str), Tipo Booleano (bool), tipos de Secuencia (list, tuple, range), tipos de mapeo(dict) tipos de Conjunto(set, frozenset).
                                    - DUPLICADOS: La lista pueden tener dos elementos con los mismos valores.
                                    - TAMAÑO: Variable. Una lista vacía ocupa unos 56 bytes. Cada nuevo elemento añade 8 bytes (el puntero al objeto) más el tamaño del objeto en sí.
                                    - RANGO: Hasta 263−1 elementos en sistemas de 64 bits.
                                    - MUTABLE: Los elementos de la lista pueden ser modificados. Podemos añadir o eliminar elementos a la lista después de que se haya creado.
                                    - TAMAÑO: Variable. Una lista vacía ocupa unos 56 bytes. Cada nuevo elemento añade 8 bytes (el puntero al objeto) más el tamaño del objeto en sí.
                                    - RANGO: Hasta 263−1 elementos en sistemas de 64 bits.
                                    
print(type((9.8, 3.14, 2.7)))    **Tuple**: Las tuplas son colecciones ordenadas de elementos que no son cambiables.
                                    SINTAXIS: (xxx, xxxx, xxx) o incluso sin paréntesis xxx, xxxx.
                                    - ORDENADO: Al igual que las listas, cada elemento tiene un índice único y definido.
                                        El primer elemento siempre tiene el índice 0: tupla[0].
                                        El último elemento siempre tiene el índice -1: tupla[-1].
                                    - HETEROGÉNEO: Las tuplas pueden almacenar cualquier tipo de dato: numéricos (int, float), cadenas (str), booleanos (bool), e incluso otras colecciones como listas u otras tuplas.
                                    - DUPLICADOS: Permiten tener múltiples elementos con el mismo valor sin restricciones.
                                    - INMUTABLE: Es su característica principal. Una vez creada, no se pueden cambiar, añadir ni eliminar elementos. 
                                    Esto las hace más rápidas (eficientes en memoria) y seguras para proteger datos que no deben ser alterados durante la ejecución del programa.
                                    El tuple es lo mismo que el list, excepto que la tupla es inmutable significa que no podemos modificar la tupla una vez creada.
                                    - TAMAÑO: Menor que la lista. Una tupla vacía ocupa unos 40 bytes. Al ser inmutable, Python no necesita reservar espacio extra para "crecimiento".
                                    - RANGO: Igual que la lista, limitado por la memoria y el direccionamiento del sistema.

                                    Nota: Para crear una tupla de un solo elemento, se debe incluir una coma: (elemento,).

# Mapa clave-valor
print(type({'name':'Asabeneh'}))  **Dictionary**: Los diccionarios son colecciones no ordenadas de valores únicos almacenados en pares (Key-Value). 
                                    Utilice un tipo de datos de diccionario para almacenar datos como un par clave-valor funciona como mapa.
                                    SINTAXIS: {clave1: valor1, clave2: valor2}.
                                    - MAPEADO (No indexado): No se accede a los elementos por su posición (0, 1, 2...), sino por su Clave. Ejemplo: persona['name'].
                                    - HETEROGÉNEO:
                                        Claves: Deben ser de un tipo inmutable (usualmente str o int).
                                        Valores: Pueden ser cualquier cosa (listas, otros diccionarios, funciones, etc.).
                                    DUPLICADOS: Las Claves deben ser únicas (si repites una clave, el último valor sobreescribe al anterior). Los Valores sí pueden estar repetidos en diferentes claves.
                                    - MUTABLE: Se pueden añadir nuevos pares clave-valor, modificar los valores existentes o eliminar entradas en cualquier momento.
                                    - TAMAÑO: Significativamente mayor debido a la tabla hash para búsqueda rápida. Un dict vacío empieza en unos 64 bytes y crece rápidamente.
                                    - RANGO: Limitado por la RAM. Las claves deben ser objetos hashables (inmutables).

# Conjunto set
print(type({9.8, 3.14, 2.7}))     **Set**: Un conjunto es una colección no ordenada de elementos de datos que son únicos. 
                                    En otras palabras, Python Set es una colección de elementos (o objetos) que no contiene elementos duplicados.
                                    SINTAXIS: {xxx, xxxx, xxx}.
                                    - DESORDENADO: Los elementos no tienen una posición fija. No puedes acceder a ellos mediante un índice (no existe set[0]). 
                                        Al imprimirlo, el orden puede variar.
                                    - HETEROGÉNEO: Puede contener diferentes tipos de datos, pero con una condición: los elementos deben ser inmutables (puedes meter strings, números o    tuplas, pero no listas dentro de un set).
                                    - SIN DUPLICADOS: No permite elementos repetidos. Si intentas añadir un valor que ya existe, Python simplemente lo ignora.
                                    - MUTABLE: Puedes añadir o eliminar elementos del conjunto, pero los elementos individuales dentro de él no se pueden modificar (tienes que borrarlos y añadir nuevos).
                                    - TAMAÑO: Elevado (similar al diccionario) porque también utiliza tablas hash para asegurar que no haya duplicados y que las búsquedas sean instantáneas.
                                    - RANGO: Limitado por la RAM.
                                    
                                    Nota: Para crear un set vacío, se debe usar set(), ya que {} crea un diccionario vacío.
# Booleanos
print(type(3 == 3))              **Bool**: para representar valores booleanos ( Truey False) utilizamos el boolTipo de datos. 
                                    Los valores booleanos se utilizan para evaluar el valor de la expresión. 
                                    - TAMAÑO: Aproximadamente 24 a 28 bytes. Aunque solo representen un bit de información, en Python son objetos completos que heredan de los enteros.
                                    - RANGO: Solo dos valores posibles: True (valor entero 1) y False (valor entero 0).
                                    
                                     Nota:  Una curiosidad técnica: ¿Sabías que bool es una subclase de int? Por eso puedes hacer operaciones como True + True y obtener 2.
print(type(3 >= 3))              **Bool**


Un detalle importante: en Python, todo es un objeto, por lo que incluso un número pequeño ocupa más que en lenguajes como C, debido a la "envoltura" (metadata) que Python le pone.

# Metodos Built-in.

- Funcion type()
Funcion type() es una función incorporada (built-in), la función devuelve el tipo de datos de la variable

- Funcion isinstance()
Funcion isinstance() es una función incorporada (built-in) comprueba si un objeto pertenece a una clase particular.
______________________________________________________________________________________________________________________________________________________________________________________
# Operadores Matematicos

print(3+2)      # Sumatoria (+) -> Imprime 5
print(3-2)      # Resta (-) -> Imprime 1
print(3*2)      # Multiplication (*)-> Imprime 6
print(3/2)      # Division Punto Floatante (2) -> 
print(3**2)     # Exponential (**)
print(3%2)      # Modulus (%)
print (3//2)    # División Entera(//)

# Operadores Matematicos son polimórficos
Todos estos operadores son polimórficos. En Python, un operador no tiene un comportamiento fijo, sino que delega en el objeto mediante métodos especiales (dunder methods), es decir
los operadores no “son” polimórficos por sí mismos, sino que activan comportamiento polimórfico porque delegan en métodos del objeto.

Código fuente:   3 + 2
                   ↓  (parser)
Bytecode:        BINARY_OP  + (VM ejecuta)
                   ↓  (Compila)
CPython C:       busca __add__ en el tipo del objeto
                   ↓
Dunder method:   int.__add__(3, 2)  
                   ↓
Resultado:         5

Se compila a 3 instrucciones en c: Se cargan valores (referencias) en el stack. Las variables implican nombres. Acá no hay nombres, 3 y 2 son literales directos. El stack solo recibe las referencias a los objetos. a objetos que ya existen en el cache de small ints(numeros cacheados en el heap -5 hasta el 256) , y una instrucción BINARY_OP en C. Esa instrucción toma las dos referencias del stack de la VM, busca __add__ en el tipo del primer objeto, y aplica la operación.
Cuando ponemos  int.__add__(3, 2) es una simplificacion o idea general de lo que pasa cuando llama al metodo interno de un objeto.

Los operadores no “son” polimórficos por sí mismos, sino que activan comportamiento polimórfico porque delegan en métodos del objeto.

3 + 2        # int.__add__(3, 2)        → 5
"ho" + "la"  # str.__add__("ho", "la") → "hola"
[1] + [2]    # list.__add__([1], [2])  → [1, 2]

El operador + es el mismo. El comportamiento cambia según el tipo. Eso es polimorfismo.

Operador Dunder method Polimórfico

+               __add__✅
-               __sub__✅
*               __mul__✅
/               __truediv__✅
**              __pow__✅
%               __mod__✅
//              __floordiv__✅

# Ejemplos de polimorfismo por operador

# + (suma vs concatenación vs unión)
print(3 + 2)          # 5
print("hola" + " mundo")  # "hola mundo"
print([1,2] + [3,4])  # [1, 2, 3, 4]

# * (multiplicación vs repetición)
print(3 * 2)          # 6
print("ja" * 3)       # "jajaja"
print([0] * 4)        # [0, 0, 0, 0]

# % (módulo vs formato de string)
print(10 % 3)         # 1
print("Hola %s" % "mundo")  # "Hola mundo"

# ** (potencia vs desempaquetado en funciones)
print(2 ** 10)        # 1024
def f(a, b): return a + b
d = {"a": 1, "b": 2}
print(f(**d))         # 3

# El fenómeno del "Interning" (Caché de objetos) 🧠

Ahora, volviendo a tu duda sobre por qué 256 es el mismo objeto y 257 no, la respuesta reside en una optimización del intérprete.
    -Enteros Pequeños: Python asume que usarás números pequeños muy seguido. Por eso, al arrancar, crea una matriz estática de objetos int para todos los números en el rango de -5 a 256.
    -Reutilización: Cuando escribes a = 256, Python no crea un objeto nuevo; simplemente apunta a al objeto que ya existe en esa matriz global.
    -Nuevas Instancias: Para 257, Python generalmente crea un objeto nuevo en el heap cada vez que se asigna (fuera de optimizaciones específicas del compilador de bloques de código).

_____________________________________________________________________________________________________________________________________________________________________________________________
# Funciones Built-in

Python incluye un conjunto de funciones disponibles globalmente sin necesidad de importar nada. Están cargadas automáticamente en el namespace built-in cada vez que el intérprete arranca, por eso siempre están disponibles.

Las más utilizadas en el día a día son:

1. Interacción con el Usuario (Entrada y Salida)
    print(): Imprime valores en la salida estándar (consola).
    input(): Lee texto ingresado por el usuario.

2. Información y Metadatos
    type(): Devuelve el tipo de dato de un objeto.
    len(): Devuelve la cantidad de elementos de una secuencia (strings, listas, etc.).

3. Conversión de Tipos (Casting)
    int(), float(), str(): Convierten entre tipos de datos básicos (entero, decimal, cadena).
    list(), dict(), tuple(), set(): Convierten o crean colecciones de datos.

4. Operaciones y Ordenamiento
    min(), max(), sum(): Operaciones matemáticas básicas sobre colecciones numéricas.
    sorted(): Devuelve una nueva lista con los elementos ordenados.

5. Herramientas de Introspección (Exploración)
    dir(): ¿Qué hay? Lista los atributos y métodos de un objeto (nombres).
    help(): ¿Cómo funciona? Muestra la documentación completa y ejemplos.

# Ejemplo: Cómo se carga print y cómo se accede

Funcion print(), es una función incorporada (built-in) utilizada para mostrar o imprimir valores en la consola o en una salida estándar. 
Cuando arranca el intérprete, se carga el módulo builtins en el heap. Su  atributo __dict__ (Tipo diccionario) contiene pares nombre → objeto, donde el objeto es de tipo builtin_function_or_method — un wrapper Python que envuelve la función C por debajo.

Se carga cuando arranca el intérprete, antes de tu código:

Arranca Python
      ↓
Crea el módulo builtins en el heap
      ↓
builtins.__dict__ = {
    'print': <built-in function print>,
    'len':   <built-in function len>,
    'range': <built-in function range>,
    ...    ← todo en C, no en .py
}
      ↓

Cada módulo recibe en su __dict__:
    '__builtins__': builtins.__dict__     ← referencia al mismo objeto

# ¿Cómo lo encuentra Python cuando escribís print(...)?

Python sigue la regla LEGB para buscar cualquier nombre:
L → Local       (f_locals del frame actual)
E → Enclosing   (funciones anidadas)
G → Global      (f_globals = module.__dict__)
B → Builtins    (__builtins__ dentro del module.__dict__)

Flujo de ejecución completo de print(3+2)

CÓDIGO FUENTE
─────────────────────────────────────
print(3 + 2)


PASO 1 — Evalúa el argumento: 3 + 2
─────────────────────────────────────
Python ve el operador +
    ↓
Llama a int.__add__(3, 2)
    ↓
Retorna el objeto int 5 en el heap


PASO 2 — Busca el nombre "print" (regla LEGB)
─────────────────────────────────────
L → ¿está en f_locals?         ❌
E → ¿hay función anidada?      ❌
G → ¿está en module.__dict__?  ❌
B → ¿está en __builtins__?     ✅  encontrado


PASO 3 — Llama a print(5)
─────────────────────────────────────
STACK                        HEAP
────────────────             ──────────────────────────
[ frame de print ]           <built-in function print>
    argumento: 5                  (implementado en C)


PASO 4 — print ejecuta en C
─────────────────────────────────────
Llama internamente a sys.stdout.write("5\n")
    ↓
El sistema operativo recibe la llamada
    ↓
Imprime en la terminal: 5


PASO 5 — Frame de print se destruye
─────────────────────────────────────
Retorna None
Frame desaparece del stack
______________________________________________________________________________________________________________________________________________________________________________________

# Input()
Cuando Python llega a una línea con input(), el programa se detiene completamente (se bloquea). 
No continuará hasta que el usuario escriba algo en el teclado y presione la tecla.

    variable = input("Mensaje o Prompt: ")

Mensaje: El "Prompt": El texto dentro de los paréntesis es opcional, pero se utiliza para indicarle al usuario qué debe escribir.
Retorno: Todo lo que el usuario escribe se devuelve como un objeto de tipo String (texto).

Entrada: El usuario escribe 30 y presiona Enter.
    Heap: Python reserva un nuevo bloque de memoria en el Heap para crear un objeto String: '30'.
    Stack: Se crea una variable en el Stack (por ejemplo, edad) que guarda la dirección de memoria de ese objeto en el Heap.
    
    Nota importante: Aunque el usuario escriba un número, input() siempre crea un String. Si escribes 30, Python lo guarda como '30' (texto), no como el número 30.

# Conversión de Tipos (Casting)
Como input() siempre devuelve texto, si necesitas realizar operaciones matemáticas, debes convertir el dato usando funciones de "Casting":
    -int(): Convierte a número entero.
    -float(): Convierte a número decimal.

# Ejemplo de interacción completa
puntos_str = input("¿Cuántos puntos ganaste?: ") # Devuelve un String
puntos_int = int(puntos_str)                   # Lo convertimos a Entero para poder sumar
total = puntos_int + 10
print(f"Tu total es: {total}")
______________________________________________________________________________________________________________________________________________________________________________________