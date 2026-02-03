# 📘 Día 12 Módulos

# Qué es un módulo
Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones que se pueden incluir en una aplicación. 
Un módulo podría ser un archivo que contiene una sola variable, una función o una gran base de código.
Un módulo es simplemente un archivo Python (con extensión .py) que contiene código: variables, funciones, clases, o cualquier combinación de estos elementos.

# Propósito de los módulos:

Organización: Dividir código grande en archivos manejables
Reutilización: Usar el mismo código en múltiples proyectos
Mantenimiento: Facilitar la actualización y corrección de errores
Colaboración: Diferentes desarrolladores pueden trabajar en diferentes módulos

# Creación de un módulo

Para crear un módulo escribimos nuestros códigos en un script de Python y lo guardamos como un archivo .py. Crear un archivo llamado mymodule.py dentro de la carpeta del proyecto. Escribamos un código en este archivo.

Crea un archivo llamado mymodule.py:
# Archivo mymodule.py 
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
                             
*** Explicación línea por línea:**
- `def`: Palabra clave para definir una función
- `generate_full_name`: Nombre descriptivo de la función
- `firstname, lastname`: Parámetros que la función espera recibir

- `return`: Devuelve un valor al que llama la función
- `firstname + ' ' + lastname`: Concatena los dos nombres con un espacio entre ellos
- Ejemplo: `generate_full_name('Juan', 'Pérez')` devuelve `'Juan Pérez'`

**¿Qué tiene de especial este archivo?**
¡Nada! Es solo un archivo Python normal. Se convierte en "módulo" cuando otro archivo lo importa.

### Estructura de tu proyecto ###:
mi_proyecto/
├── mymodule.py
└── main.py


# Archivo main.py:
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))  # Asabeneh Yetayeh

*** Explicación línea por línea:**
- `import`: Palabra clave de Python para cargar módulos
- `mymodule`: Nombre del archivo sin .py
- `Efecto`: Python busca mymodule.py, lo ejecuta, y crea un objeto módulo

- `mymodule.`: Sintaxis de punto para acceder a contenido del módulo
- `generate_full_name(...)`: Llama a la función definida en `mymodule.py`
- `print(...)`: Imprime el resultado

# ¿Qué Sucede Internamente Durante la Importación?
Ahora viene la parte profunda. Vamos a explorar exactamente qué hace Python cuando ejecutas `import mymodule`

Paso 1: Python busca el módulo
Cuando escribes import mymodule, cuando escribes import mymodule en main.py, Python necesita encontrar el archivo mymodule.py. 
Para ello, busca en varios lugares siguiendo un orden específico.
______________________________________________________________________________________________________________________________

    1.1: Búsqueda en el Directorio Actual donde está main.py
    Primero, Python busca en el mismo directorio donde está el archivo que hace la importación (main.py).

        import mymodule  # Python busca mymodule.py AQUÍ PRIMERO

    Cómo busca Python:
        Python obtiene la ruta de main.py: /home/usuario/mi_proyecto/main.py
        Extrae el directorio: /home/usuario/mi_proyecto/
        Busca en ese directorio un archivo llamado mymodule.py
        ✅ Lo encuentra: /home/usuario/mi_proyecto/mymodule.py

Si NO lo encuentra aquí, pasa al siguiente lugar.
______________________________________________________________________________________________________________________________

    1.2: Búsqueda en PYTHONPATH: Variable de entorno PYTHONPATH (si está configurada)
    Segundo, Python busca en los directorios definidos en la variable de entorno PYTHONPATH (si existe).

    ¿Qué es PYTHONPATH?
    Es una variable de entorno que TÚ puedes configurar para decirle a Python dónde más buscar módulos.

    Ejemplo de configuración (en tu terminal):

        export PYTHONPATH=/home/usuario/mis_modulos:/home/usuario/otros_modulos


    **Estructura con PYTHONPATH:**

    /home/usuario/mi_proyecto/
    └── main.py

    /home/usuario/mis_modulos/
    └── mymodule.py    ← Python también buscará AQUÍ

# Cómo busca Python:

1. Lee la variable PYTHONPATH: `/home/usuario/mis_modulos`
2. Busca `mymodule.py` en `/home/usuario/mis_modulos/mymodule.py`
3. ✅ Si lo encuentra, lo usa

**Nota:** La mayoría de las veces NO necesitas configurar PYTHONPATH. Solo es útil para proyectos complejos o múltiples ubicaciones de código.

______________________________________________________________________________________________________________________________

    1.3: Búsqueda en de instalación de Python (donde están los módulos built-in)
    Tercero, Python busca en sus directorios de instalación, donde están los módulos que vienen con Python (módulos built-in y paquetes instalados).

**Ubicaciones típicas:**

En Linux/Mac:
```
/usr/lib/python3.9/              ← Librería estándar (os, sys, math, etc.)
/usr/lib/python3.9/site-packages/ ← Paquetes instalados con pip (flask, requests, etc.)


Ejemplo: Cuando haces import os:
    Python no encuentra os.py en tu proyecto
    Python no encuentra os.py en PYTHONPATH
    Python busca en /usr/lib/python3.9/os.py
    ✅ Lo encuentra y lo importa

______________________________________________________________________________________________________________________________

Una vez encontrado `mymodule.py`, Python:

1. **Lee el archivo** como texto
2. **Lo parsea** (analiza la sintaxis)
3. **Lo compila** a bytecode (lenguaje intermedio)
4. **Guarda el bytecode** en `__pycache__/mymodule.cpython-39.pyc`

**Estructura después de la primera importación:**
```
mi_proyecto/
├── mymodule.py
├── main.py
└── __pycache__/
    └── mymodule.cpython-39.pyc  

¿Por qué bytecode?

Más rápido de ejecutar que código fuente
Se reutiliza en futuras ejecuciones (caché)
Solo se recompila si mymodule.py cambia
______________________________________________________________________________________________________________________________

Paso 3: Python ejecuta el código del módulo
Python ejecuta TODO el código en mymodule.py de arriba hacia abajo:
python# Si mymodule.py tuviera esto:
print("Cargando mymodule...")

def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

print("mymodule cargado")
```

**Salida al importar:**
```
Cargando mymodule...
mymodule cargado
```

**Punto crítico:** El código se ejecuta **una sola vez**, la primera vez que se importa.

---

______________________________________________________________________________________________________________________________

#### Paso 4: Python crea un objeto módulo en memoria

Después de ejecutar el código, Python crea un **objeto módulo** especial.

**Visualización en memoria:**
```
┌─────────────────────────────────────────┐
│  Objeto Módulo: mymodule                │
├─────────────────────────────────────────┤
│  __name__ = 'mymodule'                  │
│  __file__ = '/ruta/a/mymodule.py'       │
│  generate_full_name = <función>         │  ← Referencia a la función
└─────────────────────────────────────────┘
Este objeto es un namespace (espacio de nombres) que contiene todas las definiciones del módulo.

______________________________________________________________________________________________________________________________

Paso 5: Python registra el módulo en sys.modules
Python mantiene un diccionario global llamado sys.modules que almacena todos los módulos importados.
pythonimport sys
import mymodule

print(sys.modules['mymodule'])
# <module 'mymodule' from '/ruta/a/mymodule.py'>
Estructura de sys.modules:
pythonsys.modules = {
    'builtins': <módulo built-in>,
    'sys': <módulo sys>,
    'mymodule': <módulo mymodule>,  # Tu módulo aquí
    ...
}
```

**¿Por qué esto es importante?**
Si vuelves a hacer `import mymodule` en otro lugar, Python **no lo vuelve a cargar**. Simplemente devuelve la referencia ya existente en `sys.modules`.
______________________________________________________________________________________________________________________________

#### Paso 6: Python crea una referencia en el namespace actual

Finalmente, Python crea una variable `mymodule` en el namespace de `main.py` que **apunta** al objeto módulo.

**Visualización completa en memoria:**
```
Memoria de Python:

sys.modules = {
    'builtins': <módulo built-in>,
    'sys': <módulo sys>,
    'mymodule': <módulo mymodule>,  # Tu módulo aquí
    ...
}
```

**¿Por qué esto es importante?**
Si vuelves a hacer `import mymodule` en otro lugar, Python **no lo vuelve a cargar**. Simplemente devuelve la referencia ya existente en `sys.modules`.

---

#### Paso 6: Python crea una referencia en el namespace actual

Finalmente, Python crea una variable `mymodule` en el namespace de `main.py` que **apunta** al objeto módulo.

**Visualización completa en memoria:**
```
Memoria de Python:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  sys.modules = {                                        │
│    'mymodule': ┐                                        │
│  }             │                                        │
│                │                                        │
│                ↓                                        │
│  ┌───────────────────────────────┐                      │
│  │ Objeto Módulo: mymodule       │                      │
│  ├───────────────────────────────┤                      │
│  │ generate_full_name = ────→ ┐  │                      │
│  └──────────────────────────-─┘  │                      │
│                                │                        │
│                                ↓                        │
│              ┌─────────────────────────────────┐        │
│              │ Objeto Función:                 │        │
│              │ generate_full_name              │        │
│              │ - parámetros: firstname, lastname│       │
│              │ - código: return firstname + ...│        │
│              └─────────────────────────────────┘        │
│                                                         │
│  Namespace de main.py:                                  │
│  ┌──────────────────────────┐                           │
│  │ mymodule ────────────────┼──────┐                    │
│  └──────────────────────────┘      │                    │
│                                    │                    │
│                                    └─→ (apunta al       │
│                                        objeto módulo)   │
└─────────────────────────────────────────────────────────┘

Resumen del Proceso de Importación

import mymodule
```

**Internamente:**
```
1. Buscar 'mymodule.py' en sys.path
   ↓
2. Compilar a bytecode (si es necesario)
   ↓
3. Ejecutar todo el código del módulo
   ↓
4. Crear objeto módulo con todas las definiciones
   ↓
5. Registrar en sys.modules['mymodule']
   ↓
6. Crear variable 'mymodule' en namespace actual
   que apunta al objeto módulo

______________________________________________________________________________________________________________________________

Capítulo 5: Accediendo a Funciones del Módulo

print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```

**¿Qué sucede aquí con punteros y referencias?**
```
1. Python evalúa 'mymodule'
   └─> Busca en el namespace local de main.py
       └─> Encuentra referencia al objeto módulo

2. Python evalúa 'mymodule.generate_full_name'
   └─> Sigue el puntero al objeto módulo
       └─> Busca atributo 'generate_full_name'
           └─> Encuentra referencia a la función

3. Python llama la función con argumentos ('Asabeneh', 'Yetayeh')
   └─> Se crea un nuevo frame de ejecución
       └─> Parámetros firstname='Asabeneh', lastname='Yetayeh'
       └─> Ejecuta: return 'Asabeneh' + ' ' + 'Yetayeh'
       └─> Devuelve: 'Asabeneh Yetayeh'

4. print() recibe el resultado y lo imprime
```

**Visualización de referencias:**
```
main.py (namespace):
    mymodule ───────┐
                    │
                    ↓
            ┌─────────────────┐
            │ Módulo mymodule │
            ├─────────────────┤
            │ generate_full_name ───┐
            └─────────────────┘     │
                                    ↓
                            ┌────────────────┐
                            │ Función        │
                            │ generate_...   │
                            └────────────────┘
                            
______________________________________________________________________________________________________________________________

Módulo de Estadística

El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. Las funciones estadísticas populares que se definen en este módulo: media, mediana, modo, stdev, etc.

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
La razón por la que no ves el prefijo statistics. es por la forma específica en la que se importó el módulo en la primera línea: from statistics import *.

En Python, existen tres formas principales de importar herramientas, y cada una cambia cómo debes escribir el código después:
1. El uso del Asterisco (from statistics import *)

Cuando usas el asterisco, le dices a Python: "Trae todas las funciones de este módulo y ponlas directamente en mi archivo".

    Resultado: Puedes usar median(), mean() o mode() directamente, como si tú mismo las hubieras escrito en ese archivo.

    Ventaja: Escribes menos código.

    Desventaja: Si tienes muchas funciones, podrías confundirte de dónde viene cada una.

2. Importación Estándar (import statistics)

Si el código hubiera empezado así, sí tendrías que usar el punto obligatoriamente.

    Código: import statistics

    Llamada: statistics.median(ages)

    Por qué: Aquí el módulo actúa como un "contenedor" o carpeta. Para entrar a la carpeta y sacar la herramienta, necesitas usar el punto.

3. Importación Específica (from statistics import median)

Esta es una mezcla de ambas. Solo traes la herramienta que necesitas.

    Código: from statistics import median

    Llamada: median(ages)

    Por qué: Solo "importaste" la mediana, por lo que no necesitas el prefijo para ella, pero si intentas usar mean(), el programa fallará porque no la trajiste.
Pero si queremos importar toda la función en el módulo matemático podemos utilizar *.

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
    ---------------------------------------------------------------------------------------------------------------------------

    Ahora, hemos importado el módulo de matemáticas que contiene mucha función que puede ayudarnos a realizar cálculos matemáticos. 
    Para comprobar qué funciones tiene el módulo, podemos usar help(math) o dir(math). E
    sto mostrará las funciones disponibles en el módulo. Si queremos importar solo una función específica del módulo la importamos de la siguiente manera:

from math import pi
print(pi)
---------------------------------------------------------------------------------------------------------------------------
 join(random.choices(caracteres_hex, k=6)) 

 Esta es una de las líneas más potentes de tu código porque combina tres conceptos diferentes en una sola instrucción. Para entenderla, debemos leerla de adentro hacia afuera, como si estuviéramos pelando una cebolla.

Aquí tienes el desglose técnico:
1. random.choices(caracteres_hex, k=6)

Esta función es la encargada de la "selección".

    caracteres_hex: Es tu "bolsa" de símbolos (0123456789abcdef).

    k=6: Le dice a Python: "Mete la mano en la bolsa y saca 6 elementos".

    Comportamiento: choices permite repeticiones (puedes sacar dos veces la letra 'a').

    Resultado en Memoria: Esta función crea una Lista en el Heap que se ve así: ['a', '3', 'e', '1', '2', 'f'].

2. "".join(...)

Aquí es donde ocurre la magia de la unión. El método .join() toma todos los elementos de esa lista y los pega.

    El Separador "": El string vacío al principio indica que no quieres nada entre los caracteres. Si usaras "-".join(), el resultado sería a-3-e-1-2-f.

    Eficiencia: Python mira la lista, calcula cuánto espacio sumarán los 6 caracteres y reserva un solo bloque de memoria en el Heap para crear el string final.