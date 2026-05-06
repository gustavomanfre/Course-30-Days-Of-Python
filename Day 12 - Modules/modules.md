# 📘 Día 12 Módulos

# 📚 PARTE 1: Qué es un módulo en python.

# ¿Qué es un módulo?
Un módulo es simplemente un archivo .py. Cuando guardas un archivo con código Python, ese archivo es un módulo. 
Lo que lo hace especial no es su sintaxis sino lo que Python construye en memoria cuando lo importa.

Cuando Python importa un módulo, produce tres cosas concretas:

1- Un namespace separado: un diccionario que contiene todas las variables, funciones y clases definidas en ese archivo.
2- Un objeto de tipo module almacenado en el heap.
3- Una entrada en sys.modules que actúa como caché.

# ¿Para qué sirven los módulos?

Organización: dividir código grande en archivos manejables
Reutilización: usar el mismo código en múltiples proyectos
Mantenimiento: facilitar la actualización y corrección de errores
Colaboración: diferentes desarrolladores pueden trabajar en diferentes módulos

# El sistema de caché: sys.modules
Antes de entender cómo Python busca un módulo, hay que entender dónde los guarda.
------------------------------------------------------------------------------------------------------------------------------------
# Modulo sys
sys es un módulo built-in que expone, como atributos de un objeto en el heap, referencias a estructuras internas del runtime de CPython inicializadas durante el arranque del intérprete.

**sys** es un módulo incorporado (built-in):
- Está implementado en C dentro de CPython
- Forma parte del intérprete mismo
- No viene de un archivo .py

Se carga automáticamente cuando arranca el intérprete Internamente:

1- Arranca el intérprete
2- Inicializa estructuras internas
3- Crea el módulo sys
4- Lo mete en: sys.modules['sys'] es decir:
    1- Se crea el diccionario global de módulos: 
        modules = {}
    2- Se crea el objeto módulo sys: 
        sys = <module sys>
    3- Se registra el modulo sys: 
        modules['sys'] = sys
    4- Se conecta de la siguiente forma: 
        sys.modules = modules

sys es un objeto módulo (PyModuleObject), ese objeto vive en el heap como cualquier objeto en Python:

  Heap (memoria dinámica)
    - módulos
    - listas
    - funciones

Es un módulo con variables y funciones internas del intérprete. Podemos verificarlo de la siguiente forma:
  import sys
  print(dir(sys))

1. 🧾 sys.argv → argumentos del programa
2. 📚 sys.modules → cache de módulos (lo que veníamos viendo) es un diccionario con todos los módulos cargados.
3. 🛣️ sys.path → dónde busca módulos, rutas de búsqueda, podemos verificarlo de la siguiente forma:
  print(sys.path)

Salida típica:
    [
      '', 
      '/usr/lib/python3.10',
      '/home/usuario/proyecto'
    ]

4. 🖥️ sys.exit() → salir del programa
5. 📥📤 sys.stdin, sys.stdout, sys.stderr
  sys.stdin   # entrada (teclado)
  sys.stdout  # salida (print)
  sys.stderr  # errores
6. 🧠 sys.getsizeof() → tamaño en memoria
7. 🧬 sys.version → versión de Python
8. ⚙️ sys.platform → sistema operativo
9. 🔁 sys.getrecursionlimit() / setrecursionlimit()
    sys.getrecursionlimit()
👉 Límite de recursión (para evitar que Python explote)

Un módulo sys en Python es básicamente:
{
    '__name__': 'sys',
    '__doc__': '...',
    'argv': [...],
    'path': [...],
    'modules': {...},
    ...
}
------------------------------------------------------------------------------------------------------------------------------------
**sys.modules** es un diccionario que vive dentro del módulo sys. El diccionario Mapea nombres de módulos a sus objetos en memoria:

Es un diccionario así:
  {
    'nombre_modulo': objeto_modulo,
  }

# Ejemplo de diccionario:
import sys
print(sys.modules)

// Estás viendo un diccionario interno de Python que contiene todos los módulos que ya fueron cargados en memoria.
Salida:
{
  'sys': <module 'sys' (built-in)>, 
  'os': <module 'os' from '...'>, ...
}

# Detalle
- 'sys' → nombre con el que lo importaste
- <module 'sys' (built-in)> → objeto módulo en memoria
- (built-in) → significa que viene integrado en Python (no es archivo .py)

- 'os' → módulo
- 'from ...' → ruta del archivo .py desde donde se cargó

Ejemplo real:
<module 'os' from '/usr/lib/python3.10/os.py'>

Su propósito es evitar cargar el mismo módulo más de una vez. Si haces import math dos veces en el mismo programa, la segunda instrucción no lee el archivo ni ejecuta nada: simplemente devuelve lo que ya está en sys.modules.

import math
import math  # No recarga nada. Usa lo que ya está en sys.modules.

Este comportamiento tiene una consecuencia práctica importante: si modificas un módulo en disco mientras el programa está corriendo, el cambio no se refleja automáticamente, porque Python sigue usando el objeto que ya está en caché. En desarrollo interactivo puedes forzar una recarga con:

import importlib
importlib.reload(modulo)

# El proceso de importación paso a paso
Cuando escribes import mymodule, Python sigue este orden de búsqueda:
_______________________________________________________________________________________________________________________________________________

# Paso 1 — Verificar sys.modules 
if 'mymodule' in sys.modules:
    return sys.modules['mymodule']  # Fin. No hace nada más.

# Si ya fue importado antes, devuelve el objeto existente y se detiene aquí.

Entonces sys.modules tendría algo así:

{
    'sys': <module 'sys' (built-in)>,
    'os': <module 'os' from '/usr/lib/python3.10/os.py'>,
    'mymodule': <module 'mymodule' from '/home/usuario/mymodule.py'>
}

# Si no ha sido importado antes suponiendo que tenemos este archivo .py:

# mymodule.py
x = 10

def saludar():
    return "hola"

El intérprete verifica que el módulo no está en sys.modules, por lo que continúa la búsqueda en módulos built-in y en las rutas definidas en sys.path. 
Una vez que encuentra el archivo correspondiente (por ejemplo, mymodule.py), inicia el proceso de carga creando un módulo vacío en memoria.

[ Ver Seccion: Qué ocurre cuando Python encuentra el archivo. ]
_________________________________________________________________________________________________________________________________________________
Cuando hacés:
  import mymodule

# ACLARACION IMPORTANTE ESTE ES EL ESTADO FINAL, UNA VEZ EJECUTADO EL CODIGO
Python crea un objeto en el heap así (simplificado):

mymodule = {
    '__name__': 'mymodule',
    '__file__': '/ruta/mymodule.py',
    'x': 10,
    'saludar': <function saludar>
}

Ese objeto se guarda en sys.modules:

sys.modules['mymodule'] = <referencia a ese objeto módulo>
_______________________________________________________________________________________________________________________________________________

# Paso 2 — Verificar módulos built-in
Python comprueba si el nombre está en sys.builtin_module_names. 
Los módulos built-in están escritos en C y compilados dentro del ejecutable de Python:
No existen como archivos .py en disco.

import sys
print(sys.builtin_module_names)

Salida:
('_abc', '_ast', '_io', 'math', 'sys', 'time', ...)

# Carga de modulos built-in

Cuando ejecutás Python (python en consola), internamente ocurre esto (simplificado pero fiel a la realidad):

1. Se inicializa el runtime de Python (en C), se crean estructuras internas del intérprete:
- Memoria
- Manejo de objetos
- Sistema de tipos

2. Se crea el módulo builtin, este es clave, Contiene funciones como: 
- print 
- len
- str 
- int
-  etc.

Se cargan automáticamente y se inyectan en todos los módulos. Por eso podés hacer lo siguiente sin hacer import builtins.

  print("hola")

3. Se carga el módulo sys. También se inicializa automáticamente.

- Expone información del intérprete
- Contiene sys.path, sys.modules, etc.
- Está disponible desde el inicio

Aunque técnicamente existe desde el arranque, necesitás hacer lo siguiente para acceder a su nombre en tu código

  import sys

4. Se inicializa el sistema de imports.

Acá Python prepara todo lo necesario para resolver import:
- sys.modules → cache de módulos cargados
- sys.meta_path → loaders/importers
- sys.path → rutas de búsqueda

5. Se registran los módulos built-in. Todos los módulos compilados en C (como math, time, etc.):

- Se registran en una tabla interna
- Aparecen en sys.builtin_module_names
- Pero no se cargan todavía (salvo algunos)

Dentro de los módulos built-in hay dos categorías:

# 1. Cargados automáticamente al arrancar. Son esenciales para que Python funcione:

- sys
- builtins
- _io

Estos ya están en memoria desde el inicio

# 2. Cargados bajo demanda (lazy loading). Existen dentro del ejecutable, pero:

Existen dentro del ejecutable pero Python no los carga hasta que los importas explícitamente. Esto ahorra memoria.
  - math
  - time 
  - random
  - etc.

Esto explica por qué sys siempre está disponible aunque no lo hayas importado, y por qué math necesita un import math explícito.

- NO están en sys.modules al inicio
- Se cargan recién cuando hacés import

Ejemplo:

import sys
print("math" in sys.modules)  # False

import math
print("math" in sys.modules)  # True


# Resumen mental.
Cuando arranca Python:

- Se crea el entorno interno (runtime)
- Se carga builtins (funciones base)
- Se carga sys
- Se prepara el sistema de imports
- Se registran los built-in disponibles
- Solo algunos módulos se cargan; el resto queda “esperando import”
- Son esenciales para el funcionamiento de Python. Siempre están disponibles sin que hagas nada.
  - sys: gestión del sistema
  - builtins: funciones básicas como print, len, str
  - _io: operaciones de entrada/salida
_______________________________________________________________________________________________________________________________________________

# Paso 3 — Buscar en sys.path
sys.path es una lista de strings (rutas de directorios) que le dice a Python dónde buscar módulos cuando haces import.
Si el modulo no es built-in, Python busca un archivo .py recorriendo en orden cada directorio de la lista sys.path:

import sys
print(sys.path)

Salida:
[
    '/home/usuario/mi_proyecto',                          # 0: Directorio actual
    '/usr/lib/python312.zip',                             # 1: Biblioteca comprimida
    '/usr/lib/python3.12',                                # 2: Biblioteca estándar
    '/usr/lib/python3.12/lib-dynload',                    # 3: Extensiones dinámicas (C)
    '/home/usuario/.local/lib/python3.12/site-packages',  # 4: Paquetes usuario
    '/usr/lib/python3.12/site-packages'                   # 5: Paquetes sistema
]

Codigo para ver todos los directorios:

import sys
for i, ruta in enumerate(sys.path):
    print(f"{i}: {ruta}")

Salida:
0: /home/usuario/proyecto
1: /usr/lib/python312.zip
2: /usr/lib/python3.12
3: /usr/lib/python3.12/lib-dynload
4: /home/usuario/.local/lib/python3.12/site-packages
5: /usr/lib/python3.12/site-packages

sys.path es un atributo del módulo sys, que es un objeto lista almacenado en el heap.

HEAP:
┌────────────────────────────┐
│ module 'sys' (built-in)    │
│                            │
│ __dict__: {                │
│   'path': ──────────────┐  │
│   'modules': {...},     │  │
│   'argv': [...],        │  │
│   'version': '3.12.0',  │  │
│   ...                   │  │
│ }                       │  │
└─────────────────────────┼──┘
                          │
                          ↓
        ┌───────────────────────────────────────────┐
        │ list object (sys.path)                    │
        │ [                                         │
        │   str "/home/usuario/mi_proyecto",        │
        │   str "/usr/lib/python312.zip",           │
        │   str "/usr/lib/python3.12",              │
        │   str "/usr/lib/python3.12/lib-dynload",  │
        │   str "/home/usuario/.local/lib/...",     │
        │   str "/usr/lib/python3.12/site-packages" │
        │ ]                                         │
        └───────────────────────────────────────────┘

sys.path se crea durante el inicio del intérprete de Python, ANTES de ejecutar cualquier código de tu script.

1️⃣  Usuario ejecuta: python main.py
2️⃣  El SO carga el ejecutable de Python en memoria
3️⃣  Python inicia su inicialización interna
4️⃣  Se crea el módulo 'sys' (built-in)
5️⃣  Se crea sys.path (lista vacía inicialmente)
6️⃣  Python puebla sys.path con rutas EN ESTE ORDEN:
    6.1  Directorio del script ejecutado (o directorio actual si es interactivo)  
    6.2  Variable de entorno PYTHONPATH (si está configurada)
    6.3  Archivos .pth (si existen)
    6.4  Biblioteca estándar comprimida (python312.zip)
    6.5  Directorio de la librería estándar (/usr/lib/python3.12)
    6.6  Directorio de extensiones dinámicas (lib-dynload)
    6.7  Site-packages del usuario (~/.local/lib/.../site-packages)
    6.8  Site-packages del sistema (/usr/lib/.../site-packages)
7️⃣  Se cargan módulos esenciales (builtins, _io, etc.)
8️⃣  Python ejecuta main.py

Importante: Para cuando tu código empieza a ejecutarse, sys.path ya está completamente configurado.

El orden importa: si tienes un archivo os.py en tu proyecto, Python lo encontrará antes que el os de la librería estándar, y lo importará en su lugar. Esto puede causar bugs muy difíciles de detectar. Por eso nunca debes nombrar tus archivos igual que módulos de la librería estándar.
Si Python recorre toda la lista y no encuentra el archivo, lanza:

  ModuleNotFoundError: No module named 'mymodule'

Cuando ves este error, lo primero que debes hacer es verificar qué contiene sys.path en ese entorno de ejecución. El problema casi siempre es que el directorio donde está tu módulo no está en la lista.
_______________________________________________________________________________________________________________________________________________
# Qué ocurre cuando Python encuentra el archivo.

Una vez que localiza mymodule.py, ejecuta estas operaciones en orden:

# 1- Crea el objeto módulo en el heap (Contiene __dict__ casi vacío).[Heap]

module = <module 'mymodule'>
│
└── 
    module.__dict__ = {                   // Estado interno inicial (simplificado):
        '__name__': 'mymodule',
        '__loader__': <loader object>,
        '__package__': None,
        '__spec__': <module spec>,
        '__builtins__': {...}
        # sin x ni funciones todavía
    }

👉 En este punto:
- El módulo ya existe en memoria
- Tiene atributos internos básicos
- Todavía NO contiene el código del archivo (ni x ni funciones)

En ese momento, Python crea un “contenedor vacío” en memoria para el módulo, antes de leer o ejecutar cualquier código.

# 2- Se registra en sys.modules (caché de módulos) inmediatamente (Este paso ocurre SIEMPRE, sin importar de dónde venga el módulo).[Heap]
    sys.modules["mymodule"] = module

module es un objeto en memoria (heap) creado en el paso 1.

Este paso ocurre siempre, independientemente de si el módulo fue encontrado como built-in o en el sistema de archivos (sys.path).

Esto pasa ANTES de ejecutar el código, sirve para:
    - Evitar imports duplicados
    - Soportar imports circulares

# 3- Lee el archivo del disco.[Disco]
    - Python accede a mymodule.py ubicado en alguna de las rutas definidas sys.path

En sys.modules NO tiene todos los .py del sistema, solo tiene los módulos que ya fueron importados (o están en proceso de importarse).

# 4- Verifica __pycache__ / compila a bytecode si es necesario.

Python necesita bytecode para ejecutar.

Camino A — Hay .pyc válido en pycache:
    __pycache__/mymodule.cpython-311.pyc  ✅ existe y es válido
            ↓
    Python lo lee directamente
            ↓
    Saltea la compilación (no toca el .py para compilar)
            ↓
    Ejecuta ese bytecode

Camino B — No hay .pyc válido (o no existe):
    mymodule.py  (código fuente)
            ↓
    Python lo lee
            ↓
    Lo compila a bytecode
            ↓
    Guarda el resultado en __pycache__/mymodule.cpython-311.pyc
            ↓
    Ejecuta ese bytecode

¿Cuándo un .pyc se considera inválido?

- El .py fue modificado después de que se generó el .pyc
- La versión de Python cambió
- El .pyc está corrupto

Para no compilar siempre: Guarda el resultado en __pycache__

Solo si:
❌ no está en sys.modules
❌ no es built-in
✅ viene de un .py en disco

# 5- Guarda el .pyc, si hace falta.
    - Si se compiló desde .py, Python puede guardar el bytecode en __pycache__/
    - Si ya se usó un .pyc válido, no se vuelve a escribir

DISCO
──────────────────────────────────
__pycache__/
    mymodule.cpython-311.pyc  ← se escribe acá (o ya existía)

HEAP
──────────────────────────────────
sys.modules = {
    "mymodule": <module 'mymodule'>  ← sigue igual que paso 2
}

module.__dict__ = {
    '__name__': 'mymodule',
    '__loader__': ...,
    '__package__': None,
    '__spec__': ...,
    '__builtins__': {...}
    # todavía sin x ni funciones
}

STACK
──────────────────────────────────
(vacío, ningún frame creado aún)

  5.1 - Crear GLOBAL FRAME
      - Se crea en el stack
      - Usa como globals: module.__dict__

STACK                              HEAP
─────────────────────────          ──────────────────────────────
[ frame de mymodule ]              module.__dict__ = {
    │                                  '__name__': 'mymodule',
    ├── f_globals ─────────────→       '__loader__': ...,
    │                                  '__builtins__': {...}
    ├── f_locals  ─────────────→   }
    │         (mismo objeto)
    └── f_code → <bytecode>

El frame tiene dos punteros:

f_globals → apunta a module.__dict__
f_locals → apunta al mismo module.__dict__
Apuntan al mismo porque estamos en el top-level del módulo, no dentro de una función.

# 6- Ejecuta el bytecode dentro del frame, que va llenando el __dict__ del módulo, construyendo el **namespace del módulo**.
    - Python crea un frame de ejecución
    - Este frame usa module.__dict__ como entorno global
    - El código del módulo se ejecuta línea por línea

- Durante la ejecución, se va llenando el __dict__ del módulo. [Heap]
    - Variables, funciones y clases se agregan al namespace del módulo

# 7- Llenar el namespace del módulo

    Todo lo que se define va a:
      module.__dict__

Ejemplo:

  {
    'x': 10,
    'funcion': <function>
  }

STACK                              HEAP
─────────────────────────          ──────────────────────────────
[ frame de mymodule ]              module.__dict__ = {
    ├── f_globals ─────────────→       '__name__': 'mymodule',
    ├── f_locals  ─────────────→       '__loader__': ...,
    └── f_code ejecutando...           '__builtins__': {...},
                                       'x': 10,           ← aparece
                                       'funcion': <func>  ← aparece
                                   }
Cada línea ejecutada escribe directamente en module.__dict__ a través de f_globals.

# 8- Destruir el frame 
    - El frame desaparece (stack)
    - El módulo queda (heap)
    
El frame desaparece. El módulo queda vivo en el heap referenciado por sys.modules.
_______________________________________________________________________________________________________________________________________________

# Namespaces y frames: la distinción que importa
Este es el punto donde muchos desarrolladores tienen una confusión que luego genera errores difíciles de depurar.

Cuando Python ejecuta el código de un módulo, no ejecuta el código “en el aire”, necesita un contexto de ejecución en memoria, crea un frame en el stack. 
Ese frame tiene dos referencias (punteros): globals y locals, ambas apuntando al __dict__ del módulo (namespace del modulo) es decir el namespace no está dentro del frame, el frame apunta al namespace. El namespace vive en el Heap, mientras que el frame vive en el Stack.

Un **frame** es el contexto de ejecución donde Python gestiona:
  - Variables (x, funciones, clases) 
  - El flujo de control: Sabe qué línea de código (bytecode) se está ejecutando en cada momento y cuál es la siguiente.
  - Referencias al entorno.
      - Global frame → para el módulo
      - Local frame → para funciones

[Ver Seccion: Qué ocurre cuando Python encuentra el archivo]

Resumen corto.
[Heap]   módulo creado
[Heap]   se guarda en sys.modules
[Disco]  se lee .py / .pyc
[Stack]  se crea frame
[Exec]   se ejecuta código
[Heap]   se llena __dict__
[Stack]  frame desaparece

Cuando el código termina de ejecutarse, el frame desaparece del stack. El __dict__ permanece en el heap.
STACK (temporal)              HEAP (permanente)
┌─────────────────┐           ┌──────────────────────────────┐
│ Global frame    │           │ module 'mymodule'            │
│                 │           │                              │
│ globals ──────────────────> │   __dict__: {                │
│ locals  ──────────────────> │     'generate_full_name': ...│
│                 │           │   }                          │
└─────────────────┘           └──────────────────────────────┘
Esto explica por qué puedes acceder a las variables de un módulo después de que terminó de ejecutarse: lo que persiste no es el frame sino el namespace.

Cada módulo tiene exactamente un namespace. En tu programa siempre existe además el namespace de builtins (que contiene print, len, str, etc.). Por lo tanto en cualquier programa Python hay como mínimo tres namespaces activos: __main__, el de cada módulo importado, y builtins.

# Trazar un ejemplo completo en memoria

# mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

# main.py
import mymodule
resultado = mymodule.generate_full_name("Juan", "Pérez")
print(resultado)

Al ejecutar python main.py, el estado final en memoria es:

HEAP:

module '__main__'
  __dict__: {
    '__name__': '__main__',
    'mymodule':  ─────────────────────────────────┐
    'resultado': "Juan Pérez"                      │
  }                                                │
                                                   ↓
module 'mymodule'
  __dict__: {
    '__name__': 'mymodule',
    'generate_full_name': ────────────────────────┐
  }                                               │
                                                  ↓
function 'generate_full_name'
  __module__:  'mymodule'
  __globals__:  → apunta al __dict__ de mymodule
  __code__:     <bytecode>
  parámetros:   (firstname, lastname)

Hay dos puntos críticos aquí:

Primero, la línea import mymodule en main.py no solo carga el módulo: también crea una variable mymodule en el namespace de __main__ que apunta al objeto módulo. Por eso funciona la sintaxis mymodule.generate_full_name(...). Si hicieras del mymodule, perderías esa variable en __main__, pero el módulo seguiría existiendo en sys.modules.

Segundo, el objeto función almacena en __globals__ una referencia al namespace del módulo donde fue definida (mymodule), no del módulo desde donde se llama (main). Esto determina dónde Python busca los nombres globales cuando la función se ejecuta. 
Si generate_full_name internamente usara una variable global llamada PREFIJO, Python la buscaría en el namespace de mymodule, no en el de main. Este comportamiento es la causa raíz de muchos bugs cuando se mezclan variables globales entre módulos.
_________________________________________________________________________________________________________________________________________________
# __pycache__ es un cache del resultado de compilar mymodule.py

Después de la primera importación, Python guarda el bytecode compilado en disco:
mi_proyecto/
  ├── mymodule.py
  └── __pycache__/
      └── mymodule.cpython-312.pyc (Version compilada del codigo original)

Ese .pyc es una versión:
  - Más rápida de cargar
  - No legible fácilmente
  - Lista para ejecutar por la VM de Python

En importaciones siguientes, si el archivo .py no cambió, Python usa directamente el .pyc sin recompilar. 
Para decidir si recompilar o no, compara el timestamp y el tamaño del .py con los metadatos guardados dentro del .pyc. Si el .py cambió, recompila.

Esto es relevante en entornos de deployment: si copias solo los .pyc sin los .py, o si los timestamps del sistema de archivos están mal (común en algunos sistemas de contenedores), Python puede ejecutar bytecode desactualizado y verás comportamiento "viejo" aunque hayas modificado el código.

El resultado final en memoria es un objeto módulo en el heap:

module 'mymodule' (en el heap)
  ├── __name__: 'mymodule'
  ├── __file__: '/home/user/proyecto/mymodule.py'
  └── __dict__: {
        'generate_full_name': <function object>
      }

El atributo __dict__ es el namespace del módulo: un diccionario ordinario, permanente en el heap, que contiene todo lo definido en ese archivo.
_______________________________________________________________________________________________________________________________________________________
# Errores comunes y su causa real
Con todo lo anterior, estos son los errores más frecuentes con módulos y qué los causa exactamente:
  ModuleNotFoundError: No module named 'X'

Python recorrió toda la lista de sys.path y no encontró el archivo. Verifica el contenido de sys.path en tu entorno. El problema más común es ejecutar el script desde un directorio diferente al esperado, o trabajar en un virtualenv que no tiene el paquete instalado.
Modificas un módulo y el cambio no se refleja

El módulo ya está en sys.modules. Python no vuelve a leer el archivo. Usa importlib.reload() en desarrollo interactivo, o reinicia el proceso.
Un módulo importa una versión incorrecta (el tuyo en lugar del de la librería estándar)

El orden de sys.path pone tu directorio antes que la librería estándar. Si tu archivo se llama os.py, math.py o cualquier nombre que coincida con un módulo existente, Python lo encontrará primero y lo usará en su lugar.
AttributeError al acceder a algo de un módulo importado
Dos causas posibles: o el nombre no existe en el namespace de ese módulo (revisa qué hay en modulo.__dict__), o estás en un caso de circular import donde el módulo fue registrado en sys.modules pero su __dict__ todavía está incompleto porque no terminó de ejecutarse.

Circular imports
Cuando A importa B y B importa A, Python puede intentar usar un objeto módulo que todavía está siendo construido. En ese momento su __dict__ está parcialmente lleno: solo contiene lo que se ejecutó antes de llegar al import circular. El resultado es un ImportError o un AttributeError sobre un nombre que "debería existir". La solución habitual es mover el import dentro de la función que lo necesita, o reestructurar el código para eliminar la dependencia circular.

-----------------------------------------------------------------------------------------------------------------------------------------------------#

# Explicación Detallada y Avanzada: Importación y Módulos en Python
Voy a explicarte cada ejemplo del documento con profundidad de libro avanzado, cubriendo cada línea de código y concepto.

📘 PARTE 1: Importación con Alias (Renombrado)
Código Completo:
python# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

Análisis Línea por Línea
Línea 1: from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
Esta línea realiza 4 importaciones simultáneas con renombrado.

Sintaxis General:
pythonfrom módulo import nombre_original as nuevo_nombre
Componentes:

from: Palabra clave que indica importación selectiva
módulo: Nombre del módulo fuente
import: Palabra clave de importación
nombre_original: Nombre del objeto en el módulo
as: Palabra clave para crear alias
nuevo_nombre: Nuevo nombre en el namespace local


Proceso Interno Detallado:
Paso 1: Python importa el módulo completo
python# Internamente, Python hace (pseudocódigo):
import mymodule  # Carga el módulo completo en sys.modules
En memoria:
HEAP:
┌────────────────────────────────────────┐
│ module 'mymodule'                      │
│                                        │
│ __dict__: {                            │
│   'generate_full_name': <function>,   │
│   'sum_two_nums': <function>,         │
│   'person': <dict>,                   │
│   'gravity': <float>                  │
│ }                                      │
└────────────────────────────────────────┘

Paso 2: Python copia referencias con nuevos nombres
python# Equivalente interno (pseudocódigo):
fullname = mymodule.generate_full_name
total = mymodule.sum_two_nums
p = mymodule.person
g = mymodule.gravity
En memoria del módulo main.py:
Global frame (main.py):
┌────────────────────────────────────────┐
│ fullname ───────> <function generate_full_name>  │
│ total ──────────> <function sum_two_nums>        │
│ p ──────────────> <dict person>                  │
│ g ──────────────> <float gravity>                │
└────────────────────────────────────────┘

HEAP (compartido):
┌────────────────────────────────────────┐
│ function 'generate_full_name'          │
│   __name__: 'generate_full_name' ← ¡Nombre original!
│   __module__: 'mymodule'               │
└────────────────────────────────────────┘
Concepto crítico: Solo hay UN objeto función en memoria. fullname y mymodule.generate_full_name son dos nombres diferentes apuntando al mismo objeto.

Verificación:
pythonfrom mymodule import generate_full_name as fullname
import mymodule

# Son el mismo objeto
print(fullname is mymodule.generate_full_name)  # True
print(id(fullname) == id(mymodule.generate_full_name))  # True

# El nombre interno no cambia
print(fullname.__name__)  # 'generate_full_name' (NO 'fullname')

Línea 2: print(fullname('Asabneh','Yetayeh'))
Análisis:

Búsqueda de fullname:

Python busca en LEGB
Global: ✅ Encuentra fullname → referencia a la función


Creación del frame:

Stack:
┌────────────────────────────────────────┐
│ Frame: generate_full_name              │
│                                        │
│ firstname ─────> str "Asabneh"        │
│ lastname ──────> str "Yetayeh"        │
│                                        │
│ globals ───────> mymodule.__dict__     │ ← ¡Importante!
└────────────────────────────────────────┘
Concepto importante: Aunque llamamos a la función como fullname(), el frame se llama generate_full_name (el nombre original) y su globals apunta al namespace de mymodule (donde fue definida), NO al namespace de main.py.

Ejecución:

pythonreturn firstname + ' ' + lastname
# Crea: "Asabneh Yetayeh"

Print:

Salida: Asabneh Yetayeh

Línea 3: print(total(1, 9))
Similar al anterior, pero con sum_two_nums.
Suponiendo que mymodule.py contiene:
pythondef sum_two_nums(a, b):
    return a + b
Frame:
Frame: sum_two_nums
  a ─────> int(1)
  b ─────> int(9)
Ejecución:
pythonreturn a + b  # 1 + 9 = 10
Salida:
10

Líneas 4-6: Cálculo de peso
pythonmass = 100 
weight = mass * g
print(weight)
Suponiendo que mymodule.py contiene:
pythongravity = 9.81  # m/s²
Análisis:
Línea 4: mass = 100
Global frame (main.py):
  mass ─────> int(100)
Línea 5: weight = mass * g
Proceso:

Busca mass: ✅ Global, valor 100
Busca g: ✅ Global, apunta a 9.81 (del módulo)
Operación *:

python# Internamente:
(100).__mul__(9.81)
# Retorna: float(981.0)

Asignación:

Global frame (main.py):
  weight ─────> float(981.0)
Línea 6: print(weight)
Salida: 981.0

Líneas 7-8: Acceso a diccionario
pythonprint(p)
print(p['firstname'])
Suponiendo que mymodule.py contiene:
pythonperson = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'age': 250,
    'country': 'Finland'
}
Línea 7: print(p)
En memoria:
Global frame (main.py):
  p ─────────> dict object en mymodule

HEAP:
dict object {
  'firstname': 'Asabeneh',
  'lastname': 'Yetayeh',
  'age': 250,
  'country': 'Finland'
}
Salida:
{'firstname': 'Asabeneh', 'lastname': 'Yetayeh', 'age': 250, 'country': 'Finland'}

Línea 8: print(p['firstname'])
Proceso:

Busca p: ✅ Referencia al dict
Operación [] (indexación):

python# Internamente:
p.__getitem__('firstname')
# Retorna: 'Asabeneh'
Salida:
Asabeneh

🎯 Concepto Avanzado: Mutabilidad y Referencias Compartidas
Experimento importante:
python# main.py
from mymodule import person as p

# Modificar el diccionario
p['age'] = 300

# Importar el módulo completo
import mymodule

# Verificar
print(mymodule.person['age'])  # 300 ← ¡Cambió!
¿Por qué?
Porque p y mymodule.person apuntan al mismo objeto dict en memoria. Los diccionarios son mutables, por lo que las modificaciones se reflejan en todas las referencias.

📦 PARTE 2: Módulo os (Sistema Operativo)
pythonimport os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

Línea 1: import os
Proceso interno:

Verificar sys.modules:

pythonif 'os' in sys.modules:
    os = sys.modules['os']  # Ya cargado
else:
    # Primera importación...

Buscar el módulo:

os es un módulo de la biblioteca estándar
Ubicación típica: /usr/lib/python3.12/os.py


Cargar el módulo:

HEAP:
┌────────────────────────────────────────┐
│ module 'os'                            │
│                                        │
│ __dict__: {                            │
│   'mkdir': <function>,                │
│   'chdir': <function>,                │
│   'getcwd': <function>,               │
│   'rmdir': <function>,                │
│   'path': <module 'posixpath'>,       │
│   # ... cientos de otras funciones    │
│ }                                      │
└────────────────────────────────────────┘
Nota: El módulo os internamente importa submódulos específicos de la plataforma:

Linux/Mac: posix
Windows: nt


Línea 2: os.mkdir('directory_name')
Análisis de mkdir:
Firma de la función:
pythondef mkdir(path, mode=0o777, *, dir_fd=None):
    """
    Create a directory.
    """
Parámetros:

path: Ruta de la carpeta a crear
mode: Permisos (Unix) en octal (por defecto: 0o777 = rwxrwxrwx)
dir_fd: Descriptor de directorio (avanzado)


Proceso interno:
1. Llamada a la función:
Frame: mkdir
  path ─────> str "directory_name"
  mode ─────> int 0o777 (511 en decimal)
  dir_fd ───> None
2. Validación:
python# Internamente (pseudocódigo):
if os.path.exists(path):
    raise FileExistsError("Directory already exists")
3. Llamada al sistema operativo:
python# En C (CPython):
result = mkdir_syscall(path, mode)
if result != 0:
    raise OSError(errno, strerror(errno))
Syscalls por plataforma:

Linux: mkdir() (POSIX)
Windows: CreateDirectoryW()

4. Efecto:
Se crea una carpeta en el sistema de archivos:
proyecto/
  ├── main.py
  └── directory_name/  ← Carpeta creada
5. Retorno:
pythonreturn None

Manejo de errores:
pythonimport os

try:
    os.mkdir('mi_carpeta')
except FileExistsError:
    print("La carpeta ya existe")
except PermissionError:
    print("Sin permisos para crear carpeta")
except OSError as e:
    print(f"Error: {e}")

Línea 3: os.chdir('path')
¿Qué hace?
Cambia el directorio de trabajo actual (CWD - Current Working Directory).

Proceso interno:
1. Frame:
Frame: chdir
  path ─────> str "path"
2. Validación:
pythonif not os.path.exists(path):
    raise FileNotFoundError("Directory not found")
if not os.path.isdir(path):
    raise NotADirectoryError("Path is not a directory")
3. Syscall:
c// Linux/Mac
chdir(path);

// Windows
SetCurrentDirectory(path);
4. Efecto:
python# Antes
os.getcwd()  # "/home/user/proyecto"

os.chdir('/tmp')

# Después
os.getcwd()  # "/tmp"

Concepto importante: Rutas relativas vs absolutas
Ruta relativa:
pythonos.chdir('subcarpeta')  # Relativa al CWD actual
# Si estás en /home/user, te mueves a /home/user/subcarpeta
Ruta absoluta:
pythonos.chdir('/home/user/proyecto')  # Ruta completa desde la raíz

Uso práctico:
pythonimport os

# Guardar directorio actual
original_dir = os.getcwd()

try:
    # Cambiar a otra carpeta para trabajar
    os.chdir('/tmp')
    # Hacer operaciones...
    
finally:
    # Siempre volver al directorio original
    os.chdir(original_dir)

Línea 4: os.getcwd()
¿Qué hace?
Retorna el directorio de trabajo actual como string.

Proceso interno:
1. Frame:
Frame: getcwd
  (sin parámetros)
2. Syscall:
c// Linux/Mac
char* cwd = getcwd(NULL, 0);

// Windows
DWORD len = GetCurrentDirectory(0, NULL);
TCHAR* cwd = malloc(len);
GetCurrentDirectory(len, cwd);
3. Retorno:
pythonreturn "/home/user/proyecto"  # String con la ruta completa

Uso práctico:
pythonimport os

# Ver dónde estamos
print(f"Directorio actual: {os.getcwd()}")

# Construir rutas relativas al CWD
archivo = os.path.join(os.getcwd(), 'datos.txt')
print(archivo)  # /home/user/proyecto/datos.txt

Línea 5: os.rmdir()
Firma:
pythondef rmdir(path, *, dir_fd=None):
    """
    Remove a directory.
    """

Proceso interno:
1. Frame:
Frame: rmdir
  path ─────> str "directory_name"
2. Validaciones:
pythonif not os.path.exists(path):
    raise FileNotFoundError("Directory not found")

if not os.path.isdir(path):
    raise NotADirectoryError("Not a directory")

if os.listdir(path):  # Si no está vacía
    raise OSError("Directory not empty")
3. Syscall:
c// Linux/Mac
rmdir(path);

// Windows
RemoveDirectory(path);
4. Efecto:
La carpeta se elimina del sistema de archivos.

Restricción importante:
Solo elimina carpetas VACÍAS.
pythonimport os

# Esto falla si la carpeta tiene contenido
os.rmdir('mi_carpeta')  # OSError: Directory not empty

Eliminar carpetas con contenido:
pythonimport shutil

# Elimina recursivamente (¡PELIGROSO!)
shutil.rmtree('mi_carpeta')

🐍 PARTE 3: Módulo sys (Sistema)
pythonimport sys
print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

Concepto: sys.argv
¿Qué es?
Una lista que contiene los argumentos de línea de comandos.

Estructura:
pythonsys.argv = [
    'nombre_script.py',  # Índice 0: siempre el nombre del script
    'arg1',              # Índice 1: primer argumento
    'arg2',              # Índice 2: segundo argumento
    # ...
]

Ejemplo: python script.py Asabeneh 30DaysOfPython
Proceso del sistema operativo:

El shell parsea el comando:

bashComando: python script.py Asabeneh 30DaysOfPython

Componentes:
  - Ejecutable: python
  - Argumentos: ['script.py', 'Asabeneh', '30DaysOfPython']

El SO ejecuta Python con esos argumentos
Python crea sys.argv:

pythonsys.argv = ['script.py', 'Asabeneh', '30DaysOfPython']
En memoria:
module 'sys':
  argv ─────> list [
                str "script.py",
                str "Asabeneh",
                str "30DaysOfPython"
              ]

Análisis del código:
pythonprint('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
Desglose:
1. Acceso a sys.argv[1]:
pythonsys.argv[1]
# Internamente:
sys.__dict__['argv'].__getitem__(1)
# Retorna: "Asabeneh"
2. Acceso a sys.argv[2]:
pythonsys.argv[2]  # "30DaysOfPython"
3. Método format():
python'Welcome {}. Enjoy {} challenge!'.format('Asabeneh', '30DaysOfPython')
Proceso interno de format():
python# 1. Encuentra placeholders {}
# 2. Los reemplaza con argumentos posicionales
# 3. Retorna el string formateado

# Resultado:
"Welcome Asabeneh. Enjoy 30DaysOfPython challenge!"
4. Print:
Salida: Welcome Asabeneh. Enjoy 30DaysOfPython challenge!

Manejo de errores:
pythonimport sys

# Verificar cantidad de argumentos
if len(sys.argv) < 3:
    print("Uso: python script.py nombre desafío")
    sys.exit(1)  # Salir con código de error

nombre = sys.argv[1]
desafio = sys.argv[2]

print(f'Welcome {nombre}. Enjoy {desafio} challenge!')

Otros comandos útiles de sys:
1. sys.exit()
Firma:
pythondef exit(status=None):
    """
    Exit the interpreter by raising SystemExit(status).
    """
Uso:
pythonimport sys

# Salir con éxito
sys.exit(0)  # Código 0 = éxito

# Salir con error
sys.exit(1)  # Código distinto de 0 = error
Proceso interno:
python# sys.exit(1) internamente hace:
raise SystemExit(1)
La excepción SystemExit es capturada por el intérprete y termina el programa.

2. sys.maxsize
¿Qué es?
El entero más grande que puede representar Py_ssize_t (tipo C usado para índices).
pythonimport sys

print(sys.maxsize)
# 64-bit: 9223372036854775807 (2^63 - 1)
# 32-bit: 2147483647 (2^31 - 1)
Nota: En Python 3, los enteros pueden ser arbitrariamente grandes, pero sys.maxsize marca el límite para índices de listas/secuencias.

3. sys.path
Ya lo vimos en detalle anteriormente.
pythonimport sys

print(sys.path)
# ['', '/usr/lib/python3.12', '/usr/lib/python3.12/site-packages', ...]

4. sys.version
pythonimport sys

print(sys.version)
# '3.12.0 (main, Oct  2 2023, 12:00:00) \n[GCC 11.2.0]'

# Solo la versión
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=0, releaselevel='final', serial=0)

📊 PARTE 4: Módulo statistics
pythonfrom statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

Línea 1: from statistics import *
⚠️ Advertencia: import * importa TODO del módulo.

¿Qué se importa?
El módulo statistics define __all__:
python# Dentro de statistics.py
__all__ = [
    'mean', 'median', 'mode', 'stdev', 'variance',
    'pstdev', 'pvariance', 'quantiles', # ... etc
]
Proceso:
python# Equivalente a:
from statistics import mean
from statistics import median
from statistics import mode
from statistics import stdev
# ... etc (todas en __all__)
En memoria:
Global frame (main.py):
  mean ──────> <function mean>
  median ────> <function median>
  mode ──────> <function mode>
  stdev ─────> <function stdev>
  # ... todas las demás

Línea 2: ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
Proceso:

Crear objetos int:

Todos están en el cache (-5 a 256), así que son referencias a objetos existentes.

Crear lista:

HEAP:
list object [
  ref -> int(20),  ← Todas las referencias a 20 apuntan
  ref -> int(20),  ← al MISMO objeto int
  ref -> int(4),
  ref -> int(24),
  ref -> int(25),
  ref -> int(22),
  ref -> int(26),
  ref -> int(20),  ← Mismo objeto que los otros 20
  ref -> int(23),
  ref -> int(22),
  ref -> int(26)
]

Asignación:

Global frame:
  ages ────> list object

Línea 3: print(mean(ages))
Análisis de mean():
Firma simplificada:
pythondef mean(data):
    """
    Return the sample arithmetic mean of data.
    """

Implementación interna (simplificada):
pythondef mean(data):
    # Convertir a lista si es necesario
    data = list(data)
    
    # Validar
    if len(data) == 0:
        raise StatisticsError("mean requires at least one data point")
    
    # Calcular suma
    total = sum(data)
    
    # Calcular cantidad
    n = len(data)
    
    # Retornar media
    return total / n

Ejecución paso a paso:
1. Frame:
Frame: mean
  data ────> list [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
2. Calcular suma:
pythontotal = sum(data)

# sum() internamente hace:
resultado = 0
for item in data:
    resultado = resultado + item

# resultado = 252
3. Calcular longitud:
pythonn = len(data)  # 11
4. División:
pythonreturn 252 / 11
# Internamente: (252).__truediv__(11)
# Retorna: 22.90909090909091
5. Print:
Salida: 22.90909090909091

Línea 4: print(median(ages))
¿Qué es la mediana?
El valor central cuando los datos están ordenados.

Implementación interna (simplificada):
pythondef median(data):
    # Convertir y ordenar
    sorted_data = sorted(data)
    
    # Calcular longitud
    n = len(sorted_data)
    
    # Si es impar: elemento central
    if n % 2 == 1:
        return sorted_data[n // 2]
    
    # Si es par: promedio de los dos centrales
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

Ejecución:
1. Ordenar:
pythonsorted_data = sorted(ages)
# [4, 20, 20, 20, 22, 22, 23, 24, 25, 26, 26]
2. Calcular posición central:
pythonn = 11  # Impar

# Posición central:
n // 2 = 11 // 2 = 5
3. Obtener elemento:
pythonsorted_data[5]  # 22
4. Print:
Salida: 22

Línea 5: print(mode(ages))
¿Qué es la moda?
El valor más frecuente en los datos.

Implementación interna (simplificada):
pythondef mode(data):
    # Contar frecuencias
    from collections import Counter
    
    counts = Counter(data)
    # Counter({20: 3, 22: 2, 26: 2, 4: 1, 24: 1, 25: 1, 23: 1})
    
    # Encontrar la frecuencia máxima
    max_count = max(counts.values())
    
    # Encontrar todos los valores con esa frecuencia
    modes = [value for value, count in counts.items() if count == max_count]
    
    # Si hay una sola moda, retornarla
    if len(modes) == 1:
        return modes[0]
    
    # Si hay múltiples modas, error
    raise StatisticsError("no unique mode")

Ejecución:
1. Contar:
pythonCounter(ages)
# {20: 3, 22: 2, 26: 2, 4: 1, 24: 1, 25: 1, 23: 1}
2. Frecuencia máxima:
pythonmax_count = 3  # El 20 aparece 3 veces
3. Valores con máxima frecuencia:
pythonmodes = [20]  # Solo el 20 tiene frecuencia 3
4. Retornar:
pythonreturn 20
5. Print:
Salida: 20

Línea 6: print(stdev(ages))
¿Qué es la desviación estándar?
Mide la dispersión de los datos respecto a la media.
Fórmula (desviación estándar muestral):
s = √[ Σ(xi - μ)² / (n-1) ]
Donde:

xi: cada valor
μ: media
n: cantidad de valores


Implementación interna (simplificada):
pythondef stdev(data):
    # Calcular media
    m = mean(data)
    
    # Calcular suma de cuadrados de diferencias
    ss = sum((x - m) ** 2 for x in data)
    
    # Dividir por n-1 (corrección de Bessel)
    variance = ss / (len(data) - 1)
    
    # Raíz cuadrada
    return variance ** 0.5

Ejecución:
1. Media:
pythonm = 22.909090909090907
2. Suma de cuadrados:
pythonss = sum((x - 22.909090909090907) ** 2 for x in ages)

# Desglose:
# (20 - 22.91)² = 8.47
# (20 - 22.91)² = 8.47
# (4 - 22.91)² = 357.79
# ... etc
# Total ss ≈ 535.64
3. Varianza:
pythonvariance = 535.64 / (11 - 1)
variance = 535.64 / 10
variance = 53.564
4. Desviación estándar:
pythonstdev = 53.564 ** 0.5
stdev ≈ 7.318...
Nota: El resultado del documento dice ~2.3, lo cual parece un error. El valor correcto es aproximadamente 7.32.
Verificación:
pythonimport statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(statistics.stdev(ages))  # 7.318...

🔢 PARTE 5: Módulo math
pythonimport math
print(math.pi)           # 3.141592653589793
print(math.sqrt(2))      # 1.4142135623730951
print(math.pow(2, 3))    # 8.0
print(math.floor(9.81))  # 9
print(math.ceil(9.81))   # 10
print(math.log10(100))   # 2

Línea 1: import math
Proceso:

Verificar sys.modules
Si no está, cargar el módulo built-in math
Crear objeto módulo en heap
Registrar en sys.modules
Crear referencia en global frame


Línea 2: print(math.pi)
¿Qué es math.pi?
Una constante (variable float) definida en el módulo math.

Definición interna (en C):
c// En el código fuente de CPython (mathmodule.c)
static PyObject *math_pi = PyFloat_FromDouble(3.141592653589793);
En el namespace de math:
pythonmath.__dict__['pi'] = 3.141592653589793

Acceso:
pythonmath.pi
# Internamente:
math.__dict__['pi']
# Retorna: float(3.141592653589793)
Print:
Salida: 3.141592653589793

Línea 3: print(math.sqrt(2))
sqrt() - Raíz cuadrada
Firma:
pythondef sqrt(x):
    """
    Return the square root of x.
    """

Implementación (en C):
c// CPython (mathmodule.c)
static PyObject *
math_sqrt(PyObject *self, PyObject *x)
{
    double result = sqrt(PyFloat_AsDouble(x));
    return PyFloat_FromDouble(result);
}
Usa la función sqrt() de la biblioteca matemática de C (<math.h>).

Proceso:
1. Frame:
Frame: sqrt
  x ────> int(2)
2. Conversión:
python# int(2) se convierte a float(2.0)
3. Cálculo (en C):
cresult = sqrt(2.0)  // Algoritmo de Newton-Raphson
result = 1.4142135623730951
4. Retorno:
pythonreturn float(1.4142135623730951)
5. Print:
Salida: 1.4142135623730951

Línea 4: print(math.pow(2, 3))
pow() - Potencia
Firma:
pythondef pow(x, y):
    """
    Return x**y (x to the power of y).
    """

Diferencia con **:
python# Operador **
2 ** 3  # Retorna int(8)

# math.pow()
math.pow(2, 3)  # Retorna float(8.0)
math.pow() SIEMPRE retorna float.

Proceso:
1. Frame:
Frame: pow
  x ────> int(2)
  y ────> int(3)
2. Cálculo (en C):
cresult = pow(2.0, 3.0)  // Función pow() de C
result = 8.0
3. Retorno:
pythonreturn float(8.0)
4. Print:
Salida: 8.0

Línea 5: print(math.floor(9.81))
floor() - Redondeo hacia abajo
¿Qué hace?
Retorna el entero más grande que es menor o igual al número.

Ejemplos:
pythonmath.floor(9.81)   # 9
math.floor(9.1)    # 9
math.floor(9.999)  # 9
math.floor(-2.5)   # -3 ← Hacia abajo (más negativo)

Proceso:
1. Frame:
Frame: floor
  x ────> float(9.81)
2. Cálculo:
c// En C
result = floor(9.81)  // 9.0
3. Conversión a int:
pythonreturn int(9)
4. Print:
Salida: 9

Línea 6: print(math.ceil(9.81))
ceil() - Redondeo hacia arriba
¿Qué hace?
Retorna el entero más pequeño que es mayor o igual al número.

Ejemplos:
pythonmath.ceil(9.81)   # 10
math.ceil(9.1)    # 10
math.ceil(9.01)   # 10
math.ceil(-2.5)   # -2 ← Hacia arriba (menos negativo)

Proceso:
1. Frame:
Frame: ceil
  x ────> float(9.81)
2. Cálculo:
cresult = ceil(9.81)  // 10.0
3. Conversión:
pythonreturn int(10)
4. Print:
Salida: 10

Línea 7: print(math.log10(100))
log10() - Logaritmo base 10
¿Qué hace?
Calcula el logaritmo en base 10.
Pregunta que responde: ¿A qué potencia debo elevar 10 para obtener x?
log₁₀(100) = ?
10^? = 100
10^2 = 100
log₁₀(100) = 2

Proceso:
1. Frame:
Frame: log10
  x ────> int(100)
2. Cálculo (en C):
cresult = log10(100.0)  // 2.0
3. Retorno:
pythonreturn float(2.0)
4. Print:
Salida: 2.0

Otros logaritmos:
pythonimport math

# Logaritmo natural (base e)
math.log(10)     # 2.302585...

# Logaritmo base 2
math.log2(8)     # 3.0

# Logaritmo base arbitraria
math.log(8, 2)   # 3.0 (log₂(8))

📝 PARTE 6: Importación Selectiva de math
Ejemplo 1: Importar una función
pythonfrom math import pi
print(pi)
Proceso:

Importa el módulo math completo
Copia la referencia de pi al namespace local

En memoria:
Global frame:
  pi ────> float(3.141592653589793)

sys.modules:
  'math': <module 'math'>  ← Módulo completo en memoria
Print:
Salida: 3.141592653589793

Ejemplo 2: Importar múltiples
pythonfrom math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2.0  ← ⚠️ ERROR en el documento
Error en el documento:
pythonprint(math.log10(100))  # ❌ NameError: name 'math' is not defined
Debería ser:
pythonprint(log10(100))  # ✅ Correcto

Ejemplo 3: Importar todo
pythonfrom math import *
print(pi)                  # 3.141592653589793
print(sqrt(2))             # 1.4142135623730951
print(pow(2, 3))           # 8.0
print(floor(9.81))         # 9
print(ceil(9.81))          # 10
print(log10(100))          # 2.0  ← ✅ Correcto ahora
⚠️ Problema con import *:
python# Si ya tienes una función pow
def pow(x, y):
    return x * y  # Multiplicación en vez de potencia

from math import *  # ¡Sobrescribe tu función pow!

print(pow(2, 3))  # 8.0 (potencia, no 6)

Ejemplo 4: Renombrar
pythonfrom math import pi as PI
print(PI)  # 3.141592653589793
En memoria:
Global frame:
  PI ────> float(3.141592653589793)

HEAP:
  (mismo objeto float, dos nombres diferentes)

🔤 PARTE 7: Módulo string
pythonimport string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Análisis:
string.ascii_letters
Definición interna:
python# En string.py
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
Valor:
python'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Uso práctico:
pythonimport string
import random

# Generar contraseña aleatoria
password = ''.join(random.choice(string.ascii_letters) for _ in range(8))
print(password)  # 'kJhgTyPl' (aleatorio)

string.digits
Definición:
pythondigits = '0123456789'
Uso:
python# Verificar si un string contiene solo dígitos
texto = "12345"
if all(c in string.digits for c in texto):
    print("Solo dígitos")

string.punctuation
Definición:
pythonpunctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
Uso:
python# Eliminar puntuación de un texto
import string

texto = "¡Hola, mundo!"
sin_puntuacion = ''.join(c for c in texto if c not in string.punctuation)
print(sin_puntuacion)  # "Hola mundo"

🎲 PARTE 8: Módulo random
pythonfrom random import random, randint
print(random())           # 0.something
print(randint(5, 20))     # número entre 5 y 20

Función random()
Firma:
pythondef random():
    """
    Return random float in [0.0, 1.0).
    """

¿Qué hace?
Retorna un número flotante aleatorio en el rango [0.0, 1.0).
Nota: Incluye 0.0, pero NO incluye 1.0.

Implementación interna:
Usa el Mersenne Twister (algoritmo de generación de números pseudoaleatorios).
c// En C (simplificado)
static double random_random(void) {
    unsigned long value = genrand_int32();  // Mersenne Twister
    return value / 4294967296.0;  // Normalizar a [0, 1)
}

Ejemplos de salida:
pythonfrom random import random

print(random())  # 0.8444218515250481
print(random())  # 0.7579544029403025
print(random())  # 0.420571580830845
Cada llamada retorna un valor diferente (pseudoaleatorio).

Uso práctico:
python# Generar probabilidad
if random() < 0.3:  # 30% de probabilidad
    print("Evento raro ocurrió")

Función randint(a, b)
Firma:
pythondef randint(a, b):
    """
    Return random integer in range [a, b], including both end points.
    """

¿Qué hace?
Retorna un entero aleatorio N tal que: a ≤ N ≤ b
Importante: Incluye AMBOS extremos.

Implementación interna:
pythondef randint(a, b):
    # Equivalente a:
    return a + int((b - a + 1) * random())

Ejemplo: randint(5, 20)
Posibles valores:
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
Todos tienen la misma probabilidad (distribución uniforme).

Ejemplos de salida:
pythonfrom random import randint

print(randint(5, 20))  # 12
print(randint(5, 20))  # 7
print(randint(5, 20))  # 20
print(randint(5, 20))  # 5

Uso práctico:
python# Simular dado de 6 caras
dado = randint(1, 6)
print(f"Sacaste: {dado}")

# Seleccionar índice aleatorio
lista = ['manzana', 'banana', 'naranja']
indice = randint(0, len(lista) - 1)
print(lista[indice])

🎯 Resumen de Conceptos Avanzados
1. Importación con alias (as)
pythonfrom mymodule import func as f

Crea nueva referencia con diferente nombre
Mismo objeto en memoria
El __name__ interno NO cambia


2. Módulo os

Interfaz con el sistema operativo
Funciones llaman a syscalls del SO
Operaciones sobre archivos y directorios


3. Módulo sys

Configuración del intérprete
sys.argv: argumentos de línea de comandos
sys.modules: cache de módulos
sys.path: rutas de búsqueda


4. Módulos de matemáticas
statistics:

Funciones estadísticas
mean, median, mode, stdev

math:

Operaciones matemáticas básicas
Constantes: pi, e
Funciones: sqrt, pow, floor, ceil, log


5. Módulos de utilidad
string:

Constantes de caracteres
ascii_letters, digits, punctuation

random:

Números pseudoaleatorios
random(): float [0, 1)
randint(a, b): entero [a, b]


📋 Mejores Prácticas
1. Evita import *
❌ Malo:
pythonfrom math import *
✅ Bueno:
pythonfrom math import pi, sqrt, ceil

2. Usa alias descriptivos
❌ Malo:
pythonfrom statistics import stdev as s
✅ Bueno:
pythonfrom statistics import stdev as std_deviation

3. Maneja errores de sys.argv
❌ Malo:
pythonnombre = sys.argv[1]  # IndexError si no hay argumentos
✅ Bueno:
pythonif len(sys.argv) < 2:
    print("Uso: script.py <nombre>")
    sys.exit(1)
nombre = sys.argv[1]

4. Importa solo lo necesario
❌ Malo:
pythonimport os  # Importa TODO el módulo
os.getcwd()  # Solo usas una función
✅ Bueno:
pythonfrom os import getcwd
getcwd()