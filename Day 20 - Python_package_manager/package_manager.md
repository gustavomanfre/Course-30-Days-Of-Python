📘 Día 20 - Python PIP - Administrador de paquetes de Python
¿Qué es PIP?

PIP significa programa de instalación preferido. Usamos pip para instalar diferentes paquetes de Python. El paquete es un módulo de Python que puede contener uno o más módulos u otros paquetes. Un módulo o módulos que podemos instalar en nuestra aplicación es un paquete. En programación, no tenemos que escribir todos los programas de utilidad, sino que instalamos paquetes e importamos a nuestras aplicaciones.

Instalación de PIP

Si no ha instalado pip, déjenos instalarlo ahora. Vaya a su terminal o solicitud de comando y copia y pegue esto:
Bash

# Llama a pip para que se instale a sí mismo (actualización)
asabeneh@Asabeneh:~$ pip install pip

Compruebe si el pip está instalado escribiendo:
Bash

# Solicita al sistema la versión actual de pip y su ubicación
pip --version

Plaintext

# Ejemplo de salida en la terminal
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)

Como puede ver, estoy usando la versión 21.1.3 de pip, si ve un poco de número un poco más abajo o por encima de eso, significa que tiene pip instalado.
Instalación de paquetes con pip

Tratemos de instalar numpy, llamado Python numérico. Es uno de los paquetes más populares en el aprendizaje automático y la ciencia de datos.

NumPy es el paquete fundamental para la computación científica con Python. Contiene, entre otras cosas:

    Un poderoso objeto de matriz N-dimensional

    Funciones sofisticadas (de radiodifusión)

    Herramientas para integrar código C/C++ y Fortran

    Álgebra lineal útil, transformación de Fourier y capacidades de números aleatorios

Bash

# Descarga e instala la librería numpy desde el repositorio oficial PyPI
asabeneh@Asabeneh:~$ pip install numpy

Empecemos a usar numpy. Abra su shell interactivo de python, escriba python y luego importe numpy de la siguiente manera:
Python

# Entramos al intérprete de Python en la terminal
asabeneh@Asabeneh:~$ python
# Mensaje informativo de la versión de Python cargada
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import numpy # Carga el paquete numpy en la memoria
>>> numpy.version.version # Accede al atributo que guarda la versión instalada
'1.20.1'
>>> lst = [1, 2, 3, 4, 5] # Crea una lista estándar de Python
>>> np_arr = numpy.array(lst) # Transforma la lista en un objeto de matriz NumPy
>>> np_arr # Muestra el objeto matriz
array([1, 2, 3, 4, 5])
>>> len(np_arr) # Cuenta los elementos en la matriz
5
>>> np_arr * 2 # Operación vectorial: multiplica cada número por 2
array([ 2,  4,  6,  8, 10])
>>> np_arr + 2 # Operación vectorial: suma 2 a cada número
array([3, 4, 5, 6, 7])

Instalación de Pandas

Pandas es una biblioteca de código abierto con licencia BSD que proporciona estructuras de datos de alto rendimiento y fáciles de usar. Instalemos al hermano mayor de numpy, pandas:
Bash

# Instala la librería pandas mediante pip
asabeneh@Asabeneh:~$ pip install pandas

Python

# Probando la importación en Python
asabeneh@Asabeneh:~$ python
...
>>> import pandas # Carga el paquete pandas para análisis de datos

Importar módulo webbrowser

Importemos un módulo de navegador web, que puede ayudarnos a abrir cualquier sitio web. No necesitamos instalar este módulo, ya está instalado por defecto con Python 3.
Python

import webbrowser # Importa el módulo nativo de Python para navegación web

# Definimos una lista de direcciones URL
pythonurl_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# Recorremos la lista de sitios
for url in pythonurl_lists:
    # Por cada url en la lista, abre una nueva pestaña en el navegador predeterminado
    webbrowser.open_new_tab(url)

Gestión de Paquetes (Comandos de Terminal)
Desinstalar paquetes
Bash

# Elimina el paquete especificado de tu computadora
pip uninstall packagename

Lista de paquetes
Bash

# Muestra todos los paquetes instalados actualmente en el entorno
pip list

Paquete de espectáculo (show)
Bash

# Muestra metadatos y detalles de un paquete específico
pip show packagename

Plaintext

# Ejemplo de salida para pandas
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:

Congelación PIP (freeze)

Genera paquetes Python instalados con su versión y la salida es adecuada para usarlo en un archivo de requisitos (requirements.txt).
Bash

# Lista los paquetes instalados con el formato nombre==versión
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2

Lectura desde URL (Módulo Requests)

A veces, nos gustaría leer de un sitio web usando url o desde una API. Para abrir una conexión de red, necesitamos un paquete llamado requests.
Bash

# Instala el paquete requests para realizar peticiones HTTP (GET, POST, etc.)
asabeneh@Asabeneh:~$ pip install requests

Ejemplo 1: Leer un archivo .txt de la web
Python

import requests # Importa el módulo para peticiones de red

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # Dirección del archivo de texto
response = requests.get(url) # Abre la red y descarga los datos de la URL

print(response) # Imprime el objeto de respuesta (ej: <Response [200]>)
print(response.status_code) # Imprime el código de estado (200 significa éxito)
print(response.headers)     # Muestra los encabezados HTTP enviados por el servidor
print(response.text) # Muestra el contenido de texto plano recuperado de la página

Salida esperada:
Plaintext

<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', ...}
# (Aquí saldría todo el texto del archivo .txt solicitado)

Ejemplo 2: Leer desde una API (JSON)
Python

import requests

url = 'https://restcountries.eu/rest/v2/all'  # URL de una API de países
response = requests.get(url)  # Realiza la petición GET para obtener los datos

print(response) # Muestra el objeto de respuesta de la conexión
print(response.status_code)  # Verifica que la petición fue exitosa (200)

countries = response.json() # Extrae y parsea el contenido JSON a una lista de Python
print(countries[:1])  # Aplica un corte para mostrar solo el primer país de la lista

Salida exacta del Output:
Plaintext

<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz', 
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]

Crear un paquete

Organizamos archivos en carpetas para gestionarlos fácilmente. Un paquete es una carpeta que contiene un archivo vacío __init__.py y uno o más archivos de módulo.
Estructura:

─ mypackage ├── __init__.py (Identifica la carpeta como un paquete de Python) ├── arithmetic.py (Módulo con funciones matemáticas) └── greet.py (Módulo con funciones de saludo)
mypackage/arithmetics.py:
Python

# Define una suma que acepta infinitos argumentos numéricos
def add_numbers(*args):
    total = 0
    for num in args: # Recorre cada número pasado como argumento
        total += num # Lo acumula en la variable total
    return total # Devuelve la suma final

def subtract(a, b): # Función para resta simple
    return (a - b)

def multiple(a, b): # Función para multiplicación
    return a * b

def division(a, b): # Función para división
    return a / b

def remainder(a, b): # Función para obtener el residuo de la división
    return a % b

def power(a, b): # Función para elevar un número a la potencia de otro
    return a ** b

mypackage/greet.py:
Python

# Función que recibe dos strings y devuelve una cadena de bienvenida formateada
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'

Probar el paquete en la terminal:
Python

>>> from mypackage import arithmetics # Importa el módulo arithmetics del paquete mypackage
>>> arithmetics.add_numbers(1, 2, 3, 5) # Llama a la función de suma
11
>>> arithmetics.subtract(5, 3) # Llama a la función de resta
2
>>> from mypackage import greet # Importa el módulo greet del paquete
>>> greet.greet_person('Asabeneh', 'Yetayeh') # Ejecuta la función de saludo
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'