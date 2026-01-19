1. Python del sistema (el de Linux)
/usr/bin/python3  ← Este es el Python "oficial" del sistema

Viene preinstalado con Linux
Lo usan aplicaciones del sistema operativo
NO debes tocarlo porque podrías romper cosas del sistema

2. Entornos virtuales para desarrollo
~/mis_proyectos/proyecto1/venv  ← Python aislado para proyecto 1
~/mis_proyectos/proyecto2/venv  ← Python aislado para proyecto 2

Cada proyecto tiene su propio "mini-Python"
Puedes instalar lo que quieras sin miedo
Si algo se rompe, solo afecta a ese proyecto


¿Por qué es mejor así?
Problema sin entornos virtuales:
Sistema Linux
    └── Python del sistema
        ├── numpy versión 1.20  ← Proyecto A necesita esta versión
        └── numpy versión 1.25  ← Proyecto B necesita esta versión
                                   ❌ ¡CONFLICTO! Solo puedes tener una
Solución con entornos virtuales:
Sistema Linux
    └── Python del sistema (intocable)

Proyecto A
    └── venv/
        └── numpy versión 1.20  ✅

Proyecto B
    └── venv/
        └── numpy versión 1.25  ✅

Flujo de trabajo recomendado
Paso 1: Crear un proyecto nuevo
bash# Crear carpeta del proyecto
mkdir mi_proyecto
cd mi_proyecto

# Crear entorno virtual
python3 -m venv venv
Paso 2: Activar el entorno virtual
bash# En Linux/Mac
source venv/bin/activate

# Verás que el prompt cambia:
(venv) itc@itc-Latitude-7480:~/mi_proyecto$
       ↑
    Este prefijo indica que estás dentro del entorno virtual
Paso 3: Instalar lo que necesites
bash# Ahora SÍ puedes usar pip libremente
pip install pandas
pip install requests
pip install lo-que-sea
Paso 4: Trabajar en tu proyecto
bash# Crear tu archivo Python
nano main.py

# Ejecutarlo
python main.py
Paso 5: Desactivar cuando termines
bashdeactivate

Ejemplo práctico completo
bash# 1. Crear proyecto
mkdir proyecto_web
cd proyecto_web

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
source venv/bin/activate

# 4. Instalar librerías (ahora sin errores)
pip install flask
pip install requests

# 5. Crear tu programa
echo 'print("Hola desde mi entorno virtual")' > app.py

# 6. Ejecutar
python app.py

# 7. Desactivar cuando termines
deactivate
```

---

## Ventajas de este enfoque

| Ventaja | Explicación |
|---------|-------------|
| **Seguridad** | No tocas el Python del sistema |
| **Aislamiento** | Cada proyecto es independiente |
| **Versiones diferentes** | Proyecto A usa Flask 2.0, Proyecto B usa Flask 3.0 |
| **Limpieza** | Si borras la carpeta `venv`, empiezas desde cero |
| **Portabilidad** | Puedes compartir tu proyecto fácilmente |

---

## Pregunta frecuente

**¿Y el Python del sistema para qué sirve entonces?**

El Python del sistema se usa para:
- Herramientas del sistema operativo
- Scripts de administración
- Crear nuevos entornos virtuales (con `python3 -m venv`)

**Tu Python del sistema es como la "fábrica de Pythons"**: lo usas para crear copias independientes para tus proyectos.

---

## Resumen visual
```
┌─────────────────────────────────────┐
│   LINUX (Sistema Operativo)         │
│                                     │
│   Python del Sistema (intocable)    │ ← No modificar
│   /usr/bin/python3                  │
│                                     │
└─────────────────────────────────────┘
            │
            │ crea
            ↓
┌─────────────────────────────────────┐
│   Proyecto 1                        │
│   venv/ (entorno virtual)           │ ← Instala lo que quieras
│   ├── pandas                        │
│   └── numpy                         │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   Proyecto 2                        │
│   venv/ (entorno virtual)           │ ← Instala lo que quieras
│   ├── flask                         │
│   └── requests                      │
└─────────────────────────────────────┘

________________________________________________________________________________________________________________________________________

El diagrama completo (que omití por simplicidad)
Déjame mostrarte lo que realmente está pasando:
┌─────────────────────────────────────────────┐
│   LINUX (Sistema Operativo)                 │
│                                             │
│   Python del Sistema 3.11                   │ ← Instalado con Linux
│   /usr/bin/python3                          │
│   ├── pip (herramienta de instalación)      │
│   └── Librerías básicas del sistema         │
│                                             │
└─────────────────────────────────────────────┘
            │
            │ crea una COPIA
            ↓
┌─────────────────────────────────────────────┐
│   Proyecto A                                │
│                                             │
│   venv/                                     │
│   ├── Python 3.11 (COPIA del sistema)      │ ← ¡Aquí está Python!
│   ├── pip (propio de este entorno)         │
│   └── Librerías instaladas:                │
│       ├── numpy versión 1.20               │
│       └── pandas versión 1.5               │
│                                             │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│   Proyecto B                                │
│                                             │
│   venv/                                     │
│   ├── Python 3.11 (OTRA COPIA del sistema) │ ← Otra copia de Python
│   ├── pip (propio de este entorno)         │
│   └── Librerías instaladas:                │
│       ├── numpy versión 1.25               │
│       └── flask versión 2.0                │
│                                             │
└─────────────────────────────────────────────┘

La clave: Cada entorno virtual TIENE su propio Python
Lo que realmente ocurre:
Cuando creas un entorno virtual con:
bashpython3 -m venv venv
```

Python hace esto:

1. **Crea una carpeta `venv/`**
2. **Copia el intérprete de Python** dentro de esa carpeta
3. **Crea su propio `pip`**
4. **Configura todo para que esté aislado**

---

## Veámoslo con un ejemplo real

### **Estructura de carpetas de un entorno virtual:**
```
mi_proyecto/
├── venv/
│   ├── bin/
│   │   ├── python           ← COPIA del Python del sistema
│   │   ├── python3          ← Enlace al python de arriba
│   │   ├── pip              ← pip propio de este entorno
│   │   └── activate         ← Script para activar el entorno
│   │
│   ├── lib/
│   │   └── python3.11/
│   │       └── site-packages/  ← Aquí se instalan las librerías
│   │           ├── numpy/
│   │           ├── pandas/
│   │           └── ...
│   │
│   └── include/
│       └── python3.11/
│
└── main.py  ← Tu código

Demostración práctica
Sin activar el entorno virtual:
bash$ which python3
/usr/bin/python3          ← Usa el Python del sistema

$ python3 --version
Python 3.11.2             ← Versión del sistema
Con el entorno virtual activado:
bash$ source venv/bin/activate

(venv) $ which python3
/home/usuario/mi_proyecto/venv/bin/python3  ← Usa el Python del entorno

(venv) $ python3 --version
Python 3.11.2             ← Misma versión, pero es una COPIA independiente
```

---

## Analogía mejorada

Piensa en Python como un **chef con su cocina**:

### **Python del sistema (Linux):**
```
Chef Principal (Python 3.11)
    └── Cocina del restaurante (sistema)
        ├── Recetas básicas (librerías del sistema)
        └── Ingredientes limitados (no puedes modificar)
```

### **Proyecto A (entorno virtual):**
```
Chef Clonado A (Python 3.11 - copia)
    └── Cocina personal A (venv/)
        ├── Mismas recetas básicas
        └── Ingredientes personalizados:
            ├── numpy 1.20
            └── pandas 1.5
```

### **Proyecto B (entorno virtual):**
```
Chef Clonado B (Python 3.11 - copia)
    └── Cocina personal B (venv/)
        ├── Mismas recetas básicas
        └── Ingredientes personalizados:
            ├── numpy 1.25
            └── flask 2.0
Cada chef (Python) tiene su propia cocina (entorno) con sus propios ingredientes (librerías).

¿Por qué es una "copia"?
Técnicamente, para ahorrar espacio, Python usa enlaces simbólicos (symlinks) en lugar de copiar todos los archivos:
bash# Dentro de venv/bin/python3
lrwxrwxrwx 1 user user 7 Jan 15 10:00 python3 -> /usr/bin/python3
Pero se comporta como si fuera una copia independiente:

Tiene su propio pip
Instala librerías en su propia carpeta
No afecta al Python del sistema
No afecta a otros entornos virtuales


Resumen corregido
ComponenteTiene PythonTiene librerías¿Puedes modificarlo?Sistema Linux✅ Python 3.11✅ Librerías básicas❌ No recomendadoProyecto A (venv)✅ Python 3.11 (copia/enlace)✅ numpy 1.20, pandas✅ Sí, librementeProyecto B (venv)✅ Python 3.11 (copia/enlace)✅ numpy 1.25, flask✅ Sí, libremente

Verificación práctica
Puedes comprobarlo tú mismo:
bash# 1. Crear entorno virtual
python3 -m venv mi_entorno

# 2. Ver que el entorno tiene su propio Python
ls -la mi_entorno/bin/
# Verás:
# python
# python3
# pip
# activate
# etc.

# 3. Activar y verificar
source mi_entorno/bin/activate
which python  # Te mostrará la ruta dentro de mi_entorno/bin/
```

---

## La pregunta clave resuelta

**¿Por qué puse solo las librerías en mi diagrama anterior?**

Porque quería enfatizar la **diferencia principal**: las librerías que instalas son diferentes en cada entorno. El Python es (casi) el mismo, pero **aislado**.

**Diagrama corregido con TODO incluido:**
```
Sistema Linux
└── Python 3.11 + librerías básicas

Proyecto A
└── venv/
    ├── Python 3.11 (enlazado/copiado)
    ├── pip (independiente)
    └── numpy 1.20 (independiente)

Proyecto B
└── venv/
    ├── Python 3.11 (enlazado/copiado)
    ├── pip (independiente)
    └── numpy 1.25 (independiente)

________________________________________________________________________________________________________________________________________

PIP Freeze - Explicación Detallada

1. ¿QUÉ ES pip freeze?
Definición: Es un comando que lista todos los paquetes instalados en tu entorno Python actual junto con sus versiones exactas.
Sintaxis:
bashpip freeze

2. ¿PARA QUÉ SIRVE?
Problema que resuelve:
Imagina que desarrollas un proyecto en tu computadora y funciona perfectamente. Luego quieres:

Compartirlo con un compañero
Subirlo a un servidor
Trabajar en otra computadora

¿Cómo sabe la otra persona qué librerías necesita instalar?
Respuesta: Con pip freeze creas una "lista de compras" de todas las librerías necesarias.

3. EJEMPLO PRÁCTICO COMPLETO
PASO 1: Crear proyecto y entorno virtual
bash# Crear carpeta del proyecto
mkdir mi_proyecto_web
cd mi_proyecto_web

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
PASO 2: Instalar librerías para el proyecto
bash(venv) $ pip install flask
(venv) $ pip install requests
(venv) $ pip install pandas
PASO 3: Ver qué librerías se instalaron
bash(venv) $ pip freeze
```

**Salida**:
```
blinker==1.7.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
Flask==3.0.0
idna==3.6
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
numpy==1.26.2
pandas==2.1.4
python-dateutil==2.8.2
pytz==2023.3.post1
requests==2.31.0
six==1.16.0
tzdata==2023.4
urllib3==2.1.0
Werkzeug==3.0.1
¿Por qué hay tantas?

Instalaste 3 paquetes: flask, requests, pandas
Pero cada uno tiene dependencias (otros paquetes que necesitan)
pip freeze muestra TODOS los paquetes instalados


PASO 4: Guardar en archivo requirements.txt
bash(venv) $ pip freeze > requirements.txt
```

**¿Qué hace este comando?**
- `pip freeze`: Lista los paquetes
- `>`: Operador de redirección (guarda la salida en un archivo)
- `requirements.txt`: Nombre del archivo donde se guarda

**Ahora tu proyecto tiene este archivo**:
```
mi_proyecto_web/
├── venv/
├── app.py
└── requirements.txt  ← Archivo creado
```

**Contenido de `requirements.txt`**:
```
blinker==1.7.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
Flask==3.0.0
idna==3.6
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
numpy==1.26.2
pandas==2.1.4
python-dateutil==2.8.2
pytz==2023.3.post1
requests==2.31.0
six==1.16.0
tzdata==2023.4
urllib3==2.1.0
Werkzeug==3.0.1

4. ¿CÓMO SE USA EL ARCHIVO requirements.txt?
Escenario 1: Tu compañero quiere ejecutar tu proyecto
Tu compañero hace esto:
bash# 1. Clonar/descargar tu proyecto
cd mi_proyecto_web

# 2. Crear su propio entorno virtual
python3 -m venv venv

# 3. Activar el entorno virtual
source venv/bin/activate

# 4. Instalar TODAS las librerías con un solo comando
(venv) $ pip install -r requirements.txt
¿Qué hace pip install -r requirements.txt?

Lee el archivo línea por línea
Instala cada paquete con la versión exacta especificada
Tu compañero tendrá exactamente las mismas librerías que tú


Escenario 2: Desplegar en un servidor
bash# En el servidor
git clone https://github.com/tuusuario/mi_proyecto_web.git
cd mi_proyecto_web
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  ← Instala todo automáticamente
python app.py  ← El proyecto funciona igual que en tu computadora

5. ANÁLISIS DE LA SALIDA DEL EJEMPLO
bashasabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

**Desglose de cada línea:**

| Paquete | Versión | Significado |
|---------|---------|-------------|
| `docutils` | `0.11` | Librería para procesar documentación |
| `Jinja2` | `2.7.2` | Motor de plantillas (usado por Flask, Sphinx) |
| `MarkupSafe` | `0.19` | Dependencia de Jinja2 (escape de HTML) |
| `Pygments` | `1.6` | Librería para resaltar código |
| `Sphinx` | `1.2.2` | Generador de documentación |

**Formato**:
```
nombre_paquete==versión_exacta
```

**El símbolo `==`**: Significa "versión exacta"
- `Flask==3.0.0`: Instala **exactamente** la versión 3.0.0
- No instala 3.0.1 ni 2.9.9, solo 3.0.0

---

## 6. FLUJO COMPLETO: De desarrollo a producción
```
┌─────────────────────────────────────────┐
│  TU COMPUTADORA (Desarrollo)            │
│                                         │
│  1. Crear entorno virtual               │
│     python3 -m venv venv                │
│                                         │
│  2. Instalar librerías                  │
│     pip install flask pandas            │
│                                         │
│  3. Desarrollar el proyecto             │
│     app.py, main.py, etc.               │
│                                         │
│  4. Congelar dependencias               │
│     pip freeze > requirements.txt       │
│                                         │
│  5. Subir a GitHub/GitLab               │
│     git push origin main                │
│                                         │
└─────────────────────────────────────────┘
                    │
                    │ Internet
                    ↓
┌─────────────────────────────────────────┐
│  SERVIDOR (Producción)                  │
│                                         │
│  1. Descargar proyecto                  │
│     git clone ...                       │
│                                         │
│  2. Crear entorno virtual               │
│     python3 -m venv venv                │
│                                         │
│  3. Instalar TODAS las librerías        │
│     pip install -r requirements.txt     │
│     ↑                                   │
│     └── Lee el archivo y instala TODO   │
│                                         │
│  4. Ejecutar aplicación                 │
│     python app.py                       │
│                                         │
└─────────────────────────────────────────┘

7. COMANDOS IMPORTANTES
Crear requirements.txt:
bashpip freeze > requirements.txt
Instalar desde requirements.txt:
bashpip install -r requirements.txt
Ver paquetes instalados (sin guardar):
bashpip freeze
Ver paquetes con detalles:
bashpip list
Diferencia entre pip freeze y pip list:
bash# pip freeze (formato para requirements.txt)
Flask==3.0.0
requests==2.31.0

# pip list (formato legible para humanos)
Package    Version
---------- -------
Flask      3.0.0
requests   2.31.0

8. BUENAS PRÁCTICAS
✅ LO QUE DEBES HACER:
bash# 1. Siempre crear entorno virtual para cada proyecto
python3 -m venv venv

# 2. Activar el entorno antes de instalar
source venv/bin/activate

# 3. Instalar solo lo necesario
pip install flask requests

# 4. Generar requirements.txt
pip freeze > requirements.txt

# 5. Incluir requirements.txt en tu repositorio Git
git add requirements.txt
git commit -m "Add dependencies"
❌ LO QUE NO DEBES HACER:
bash# ❌ NO hacer pip freeze sin entorno virtual activado
# (incluirá TODOS los paquetes del sistema)

# ❌ NO editar requirements.txt manualmente sin saber
# (pip freeze lo hace automáticamente)

# ❌ NO compartir la carpeta venv/
# (es pesada e innecesaria, solo comparte requirements.txt)
```

---

## 9. EJEMPLO REAL: Proyecto Flask

### **Tu proyecto**:
```
mi_app_flask/
├── venv/                  ← NO se comparte
├── app.py
├── templates/
│   └── index.html
├── requirements.txt       ← SÍ se comparte
└── README.md
```

### **Contenido de `requirements.txt`**:
```
Flask==3.0.0
Werkzeug==3.0.1
Jinja2==3.1.2
click==8.1.7
itsdangerous==2.1.2
MarkupSafe==2.1.3
Tu compañero hace:
bash# 1. Clonar repositorio
git clone https://github.com/tu/mi_app_flask.git
cd mi_app_flask

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python app.py

# ✅ ¡Funciona! Tiene las mismas librerías que tú
```

---

## 10. PREGUNTAS FRECUENTES

### **¿Debo incluir `venv/` en Git?**
❌ **NO**. Solo incluye `requirements.txt`.

**¿Por qué?**
- La carpeta `venv/` puede pesar 100+ MB
- Cada persona puede recrearla con `pip install -r requirements.txt`
- Puede causar conflictos entre diferentes sistemas operativos

**En `.gitignore`**:
```
venv/
__pycache__/
*.pyc

¿Qué pasa si actualizo una librería?
bash# Actualizar Flask a la última versión
pip install --upgrade Flask

# Regenerar requirements.txt
pip freeze > requirements.txt

# Ahora requirements.txt tiene la nueva versión

¿Puedo instalar solo algunas librerías de requirements.txt?
No directamente, pero puedes crear un archivo temporal:
bash# Crear requirements_minimal.txt con solo lo básico
echo "Flask==3.0.0" > requirements_minimal.txt
echo "requests==2.31.0" >> requirements_minimal.txt

# Instalar solo esas
pip install -r requirements_minimal.txt
```

---

## 11. RESUMEN EJECUTIVO

| Comando | Acción |
|---------|--------|
| `pip freeze` | Muestra lista de paquetes instalados |
| `pip freeze > requirements.txt` | Guarda la lista en un archivo |
| `pip install -r requirements.txt` | Instala todos los paquetes del archivo |
| `pip list` | Muestra paquetes en formato tabla |

---

## 12. ANALOGÍA FINAL

**`requirements.txt` es como una receta de cocina**:
```
Receta: Pastel de Chocolate
- Harina (2 tazas) ← Flask==3.0.0
- Azúcar (1 taza)  ← requests==2.31.0
- Huevos (3)       ← pandas==2.1.4
- Chocolate (200g) ← numpy==1.26.2

________________________________________________________________________________________________________________________________________

response.text
Tipo de dato: str (string/cadena de texto)
Formato: Texto plano tal como viene del servidor
Ejemplo:
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)

texto = response.text
print(type(texto))  # <class 'str'>
print(texto[:200])  # Primeros 200 caracteres
Salida:
python<class 'str'>
'[{"name":"Afghanistan","topLevelDomain":[".af"],"alpha2Code":"AF","alpha3Code":"AFG","callingCodes":["93"],"capital":"Kabul","altSpellings":["AF","Afġānistān"],"region":"Asia"...'
Es un string largo con formato JSON, pero sigue siendo texto plano.

response.json()
Tipo de dato: Depende del JSON, típicamente list o dict
Formato: Estructura de datos de Python (lista, diccionario, etc.)
Ejemplo:
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)

paises = response.json()
print(type(paises))  # <class 'list'>
print(type(paises[0]))  # <class 'dict'>
Salida:
python<class 'list'>
<class 'dict'>
Es una lista de Python que contiene diccionarios.

2. COMPARACIÓN LADO A LADO
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)

# ============================================
# USANDO response.text
# ============================================
texto = response.text
print(f"Tipo: {type(texto)}")
print(f"Primeros 100 caracteres:")
print(texto[:100])
print(f"¿Puedo acceder como lista? NO ❌")
# texto[0]  # Esto daría el primer CARACTER '[', no el primer país

# ============================================
# USANDO response.json()
# ============================================
paises = response.json()
print(f"\nTipo: {type(paises)}")
print(f"Número de países: {len(paises)}")
print(f"¿Puedo acceder al primer país? SÍ ✅")
print(f"Primer país: {paises[0]['name']}")
```

**Salida**:
```
Tipo: <class 'str'>
Primeros 100 caracteres:
[{"name":"Afghanistan","topLevelDomain":[".af"],"alpha2Code":"AF","alpha3Code":"AFG","calling
¿Puedo acceder como lista? NO ❌

Tipo: <class 'list'>
Número de países: 250
¿Puedo acceder al primer país? SÍ ✅
Primer país: Afghanistan

3. ANÁLISIS DETALLADO DE response.json()
Estructura completa del dato retornado:
pythoncountries = response.json()

# Tipo externo
print(type(countries))  # <class 'list'>

# Estructura:
# [
#     {...},  ← Diccionario del país 1
#     {...},  ← Diccionario del país 2
#     {...},  ← Diccionario del país 3
#     ...
# ]

# Cada elemento es un diccionario
print(type(countries[0]))  # <class 'dict'>

Ejemplo de UN país (diccionario):
pythonprimer_pais = countries[0]

# Es un diccionario con esta estructura:
{
    'name': 'Afghanistan',                    # str
    'alpha2Code': 'AF',                       # str
    'alpha3Code': 'AFG',                      # str
    'capital': 'Kabul',                       # str
    'region': 'Asia',                         # str
    'subregion': 'Southern Asia',             # str
    'population': 27657145,                   # int
    'area': 652230.0,                         # float
    'borders': ['IRN', 'PAK', 'TKM', ...],   # list
    'languages': [                            # list de dict
        {
            'iso639_1': 'ps',
            'name': 'Pashto',
            'nativeName': 'پښتو'
        },
        {...}
    ],
    'currencies': [                           # list de dict
        {
            'code': 'AFN',
            'name': 'Afghan afghani',
            'symbol': '؋'
        }
    ],
    'flag': 'https://...',                   # str
    'timezones': ['UTC+04:30'],              # list
    ...
}

4. CÓMO SE DIVIDE Y ACCEDE
Acceso a elementos de response.json():
pythoncountries = response.json()

# ============================================
# NIVEL 1: Acceder a un país específico
# ============================================
primer_pais = countries[0]        # Primer país (índice 0)
segundo_pais = countries[1]       # Segundo país (índice 1)
ultimo_pais = countries[-1]       # Último país

# ============================================
# NIVEL 2: Acceder a propiedades de un país
# ============================================
nombre = countries[0]['name']              # 'Afghanistan'
capital = countries[0]['capital']          # 'Kabul'
poblacion = countries[0]['population']     # 27657145
region = countries[0]['region']            # 'Asia'

# ============================================
# NIVEL 3: Acceder a listas dentro del país
# ============================================
idiomas = countries[0]['languages']        # Lista de diccionarios
primer_idioma = idiomas[0]                 # Primer idioma (diccionario)
nombre_idioma = primer_idioma['name']      # 'Pashto'

# O en una sola línea:
nombre_idioma = countries[0]['languages'][0]['name']  # 'Pashto'

# ============================================
# NIVEL 4: Fronteras (lista simple de strings)
# ============================================
fronteras = countries[0]['borders']        # ['IRN', 'PAK', 'TKM', ...]
primera_frontera = fronteras[0]            # 'IRN'

5. EJEMPLOS PRÁCTICOS COMPLETOS
Ejemplo 1: Listar nombres de todos los países
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
countries = response.json()

# Iterar sobre la lista de países
for pais in countries:
    print(pais['name'])
```

**Salida**:
```
Afghanistan
Åland Islands
Albania
Algeria
American Samoa
...

Ejemplo 2: Filtrar países por región
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
countries = response.json()

# Filtrar países de América del Sur
paises_sudamerica = []
for pais in countries:
    if pais['region'] == 'Americas' and pais['subregion'] == 'South America':
        paises_sudamerica.append(pais['name'])

print("Países de Sudamérica:")
for nombre in paises_sudamerica:
    print(f"  - {nombre}")
```

**Salida**:
```
Países de Sudamérica:
  - Argentina
  - Bolivia
  - Brazil
  - Chile
  - Colombia
  - Ecuador
  - Guyana
  - Paraguay
  - Peru
  - Suriname
  - Uruguay
  - Venezuela

Ejemplo 3: Mostrar países e idiomas
pythonimport requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
countries = response.json()

# Mostrar primeros 5 países con sus idiomas
for i in range(5):
    pais = countries[i]
    nombre_pais = pais['name']
    idiomas = pais['languages']
    
    print(f"\n{nombre_pais}:")
    for idioma in idiomas:
        print(f"  - {idioma['name']} ({idioma['nativeName']})")
```

**Salida**:
```
Afghanistan:
  - Pashto (پښتو)
  - Uzbek (Oʻzbek)
  - Turkmen (Türkmen)

Åland Islands:
  - Swedish (svenska)

Albania:
  - Albanian (Shqip)

Algeria:
  - Arabic (العربية)

American Samoa:
  - English (English)
  - Samoan (gagana fa'a Samoa)

6. TABLA COMPARATIVA COMPLETA
Aspectoresponse.textresponse.json()Tipo de datostr (string)list o dict (depende del JSON)FormatoTexto planoEstructura de datos de PythonUsoPara archivos txt, html, xmlPara datos JSON (APIs)AccesoComo string: texto[0] (primer carácter)Como estructura: datos[0] (primer elemento)ModificaciónDifícil (necesitas parsear manualmente)Fácil (acceso directo con índices/claves)Ejemplo'[{"name":"Afghanistan"}...]'[{'name': 'Afghanistan'}, ...]

7. ¿CUÁNDO USAR CADA UNO?
Usa response.text cuando:

El contenido es texto plano (.txt)
El contenido es HTML (.html)
El contenido es XML
Quieres ver el contenido "crudo" sin procesar

Ejemplo:
pythonurl = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
contenido = response.text  # Texto plano
print(contenido)

Usa response.json() cuando:

El contenido es JSON (datos estructurados)
Estás consultando una API
Necesitas acceder a propiedades específicas
Quieres iterar sobre los datos

Ejemplo:
pythonurl = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
paises = response.json()  # Lista de diccionarios
print(paises[0]['name'])  # Acceso directo

8. CONVERSIÓN MANUAL (para entender mejor)
pythonimport json

# ============================================
# Si usas response.text con JSON
# ============================================
url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)

# Obtienes un string
texto_json = response.text
print(type(texto_json))  # <class 'str'>

# Necesitas convertir manualmente a estructura Python
paises = json.loads(texto_json)
print(type(paises))  # <class 'list'>

# ============================================
# Si usas response.json()
# ============================================
# Hace la conversión automáticamente
paises = response.json()
print(type(paises))  # <class 'list'>
Lo que response.json() hace internamente:
python# response.json() es equivalente a:
import json
json.loads(response.text)
```

---

## 9. DIAGRAMA VISUAL
```
API Server (https://restcountries.eu/rest/v2/all)
                    ↓
        Envía datos en formato JSON
                    ↓
┌─────────────────────────────────────────────┐
│  response (objeto Response de requests)      │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ response.text                       │   │
│  │ Tipo: str                           │   │
│  │ Contenido:                          │   │
│  │ '[{"name":"Afghanistan",...}]'      │   │
│  │                                     │   │
│  │ ✅ Para txt, html, xml              │   │
│  │ ❌ Difícil trabajar con JSON        │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ response.json()                     │   │
│  │ Tipo: list[dict]                    │   │
│  │ Contenido:                          │   │
│  │ [                                   │   │
│  │   {'name': 'Afghanistan', ...},     │   │
│  │   {'name': 'Albania', ...},         │   │
│  │   ...                               │   │
│  │ ]                                   │   │
│  │                                     │   │
│  │ ✅ Para JSON (APIs)                 │   │
│  │ ✅ Fácil acceder a datos            │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘

# response.text → String (texto plano)
texto = response.text
# '[{"name":"Afghanistan"}]'  ← Es un STRING, no una lista

# response.json() → Estructura Python (lista/diccionario)
datos = response.json()
# [{'name': 'Afghanistan'}]  ← Es una LISTA de diccionarios

# Para JSON, SIEMPRE usa .json()
# Para texto plano, usa .text

______________________________________________________________________________________________________________________________________

1. ESTRUCTURA EXACTA
pythoncountries = response.json()

# Es una LISTA que CONTIENE diccionarios
# Lista → [dict, dict, dict, ...]
Visualización con niveles:
pythoncountries = [              # ← LISTA (el contenedor externo)
    {                      # ← DICCIONARIO 1 (primer país)
        'name': 'Afghanistan',
        'capital': 'Kabul',
        'population': 27657145
    },
    {                      # ← DICCIONARIO 2 (segundo país)
        'name': 'Albania',
        'capital': 'Tirana',
        'population': 2886026
    },
    {                      # ← DICCIONARIO 3 (tercer país)
        'name': 'Algeria',
        'capital': 'Algiers',
        'population': 40400000
    }
]

# Tipos:
print(type(countries))      # <class 'list'>
print(type(countries[0]))   # <class 'dict'>

2. LECTURA DE countries[0]['name']
De IZQUIERDA a DERECHA:
pythoncountries[0]['name']
    ↓       ↓     ↓
    │       │     └── 3. Acceder a la clave 'name' del diccionario
    │       └──────── 2. Obtener el elemento en índice 0 (primer diccionario)
    └──────────────── 1. Variable que contiene la LISTA
Paso a paso:
PASO 1: countries es una lista
pythoncountries = [
    {...},  # índice 0
    {...},  # índice 1
    {...}   # índice 2
]

print(type(countries))  # <class 'list'>
PASO 2: countries[0] accede al primer elemento (un diccionario)
pythoncountries[0] = {
    'name': 'Afghanistan',
    'capital': 'Kabul',
    'population': 27657145
}

print(type(countries[0]))  # <class 'dict'>
PASO 3: countries[0]['name'] accede a la clave 'name' del diccionario
pythoncountries[0]['name'] = 'Afghanistan'

print(type(countries[0]['name']))  # <class 'str'>
```

---

## 3. ANALOGÍA VISUAL

### **Piensa en una estantería con cajas**:
```
ESTANTERÍA (Lista)
├── Caja 0 (Diccionario)
│   ├── Etiqueta "name": "Afghanistan"
│   ├── Etiqueta "capital": "Kabul"
│   └── Etiqueta "population": 27657145
│
├── Caja 1 (Diccionario)
│   ├── Etiqueta "name": "Albania"
│   ├── Etiqueta "capital": "Tirana"
│   └── Etiqueta "population": 2886026
│
└── Caja 2 (Diccionario)
    ├── Etiqueta "name": "Algeria"
    ├── Etiqueta "capital": "Algiers"
    └── Etiqueta "population": 40400000
Acceso:
pythoncountries[0]           # Tomar la Caja 0
countries[0]['name']   # Leer la etiqueta "name" de la Caja 0

4. COMPARACIÓN: Lista vs Diccionario
¿Qué es una LISTA?
python# Lista: Colección ORDENADA con ÍNDICES numéricos
frutas = ['manzana', 'banana', 'naranja']
#         ↑          ↑         ↑
#      índice 0   índice 1  índice 2

# Acceso por POSICIÓN
frutas[0]  # 'manzana'
frutas[1]  # 'banana'
¿Qué es un DICCIONARIO?
python# Diccionario: Colección con pares CLAVE-VALOR
persona = {
    'nombre': 'Juan',    # clave: 'nombre', valor: 'Juan'
    'edad': 30,          # clave: 'edad', valor: 30
    'ciudad': 'Madrid'   # clave: 'ciudad', valor: 'Madrid'
}

# Acceso por CLAVE
persona['nombre']  # 'Juan'
persona['edad']    # 30

5. LISTA DE DICCIONARIOS (Tu caso)
python# Lista que contiene diccionarios
countries = [
    {'name': 'Afghanistan', 'capital': 'Kabul'},     # Diccionario en índice 0
    {'name': 'Albania', 'capital': 'Tirana'},        # Diccionario en índice 1
    {'name': 'Algeria', 'capital': 'Algiers'}        # Diccionario en índice 2
]

# ============================================
# ACCESO CON DOS PASOS
# ============================================

# PASO 1: Acceder a la lista (por índice numérico)
primer_pais = countries[0]
print(primer_pais)
# {'name': 'Afghanistan', 'capital': 'Kabul'}

# PASO 2: Acceder al diccionario (por clave string)
nombre = primer_pais['name']
print(nombre)
# 'Afghanistan'

# ============================================
# ACCESO DIRECTO (combinado)
# ============================================
nombre = countries[0]['name']
#        └────┬────┘ └──┬──┘
#             │         └── Acceso al diccionario por clave
#             └────────── Acceso a la lista por índice

6. EJEMPLOS ADICIONALES
Ejemplo 1: Acceder a diferentes elementos
pythoncountries = [
    {'name': 'Afghanistan', 'capital': 'Kabul', 'population': 27657145},
    {'name': 'Albania', 'capital': 'Tirana', 'population': 2886026},
    {'name': 'Algeria', 'capital': 'Algiers', 'population': 40400000}
]

# Primer país
print(countries[0]['name'])        # 'Afghanistan'
print(countries[0]['capital'])     # 'Kabul'
print(countries[0]['population'])  # 27657145

# Segundo país
print(countries[1]['name'])        # 'Albania'
print(countries[1]['capital'])     # 'Tirana'

# Último país
print(countries[-1]['name'])       # 'Algeria'
print(countries[-1]['capital'])    # 'Algiers'

Ejemplo 2: Iterar sobre la lista
pythoncountries = [
    {'name': 'Afghanistan', 'capital': 'Kabul'},
    {'name': 'Albania', 'capital': 'Tirana'},
    {'name': 'Algeria', 'capital': 'Algiers'}
]

# Iterar sobre cada diccionario en la lista
for pais in countries:
    # En cada iteración, 'pais' es un diccionario
    print(f"País: {pais['name']}, Capital: {pais['capital']}")
```

**Salida**:
```
País: Afghanistan, Capital: Kabul
País: Albania, Capital: Tirana
País: Algeria, Capital: Algiers

Ejemplo 3: Acceso con listas anidadas
pythoncountries = [
    {
        'name': 'Afghanistan',
        'languages': ['Pashto', 'Uzbek', 'Turkmen']  # ← Lista dentro del diccionario
    },
    {
        'name': 'Albania',
        'languages': ['Albanian']
    }
]

# Acceso a lista anidada
print(countries[0]['languages'])           # ['Pashto', 'Uzbek', 'Turkmen']
print(countries[0]['languages'][0])        # 'Pashto'
print(countries[0]['languages'][1])        # 'Uzbek'

# Lectura:
# countries[0]              → Primer diccionario (Afghanistan)
# countries[0]['languages'] → Lista de idiomas
# countries[0]['languages'][0] → Primer idioma de la lista

7. DIFERENCIAS CLAVE
❌ NO es "diccionario de listas":
python# Un diccionario de listas sería así:
diccionario_de_listas = {
    'frutas': ['manzana', 'banana', 'naranja'],
    'verduras': ['lechuga', 'tomate', 'zanahoria'],
    'carnes': ['pollo', 'res', 'cerdo']
}

# Acceso:
diccionario_de_listas['frutas']      # ['manzana', 'banana', 'naranja']
diccionario_de_listas['frutas'][0]   # 'manzana'
✅ SÍ es "lista de diccionarios":
python# Una lista de diccionarios es así:
lista_de_diccionarios = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'María', 'edad': 25},
    {'nombre': 'Pedro', 'edad': 35}
]

# Acceso:
lista_de_diccionarios[0]            # {'nombre': 'Juan', 'edad': 30}
lista_de_diccionarios[0]['nombre']  # 'Juan'

8. DIAGRAMA COMPLETO
pythoncountries = [                           # LISTA (contenedor externo)
    {                                   # ← DICCIONARIO índice 0
        'name': 'Afghanistan',          # ← Par clave-valor
        'capital': 'Kabul',
        'languages': [                  # ← LISTA dentro del diccionario
            'Pashto',
            'Uzbek'
        ]
    },
    {                                   # ← DICCIONARIO índice 1
        'name': 'Albania',
        'capital': 'Tirana',
        'languages': [
            'Albanian'
        ]
    }
]

# Tipos por nivel:
type(countries)                         # <class 'list'>
type(countries[0])                      # <class 'dict'>
type(countries[0]['name'])              # <class 'str'>
type(countries[0]['languages'])         # <class 'list'>
type(countries[0]['languages'][0])      # <class 'str'>

9. TABLA RESUMEN
ExpresiónTipo retornadoValor en el ejemplocountrieslist[{...}, {...}, {...}]countries[0]dict{'name': 'Afghanistan', ...}countries[0]['name']str'Afghanistan'countries[0]['languages']list['Pashto', 'Uzbek', ...]countries[0]['languages'][0]str'Pashto'

10. RESPUESTA DIRECTA A TU PREGUNTA
¿Cómo se lee countries[0]['name']?
NO es: "diccionario de listas"
SÍ es: "lista de diccionarios"
Se lee como:

"Accede al elemento en el índice 0 de la lista countries, y luego accede a la clave 'name' de ese diccionario."

O más simple:

"Del primer país de la lista, dame su nombre"


11. REGLA MNEMOTÉCNICA
pythoncountries[0]['name']
   ↓       ↓     ↓
 Lista  Índice Clave

# Corchetes con NÚMERO → Acceso a LISTA
# Corchetes con STRING → Acceso a DICCIONARIO
Secuencia:

countries → Variable (lista)
[0] → Acceso a lista (índice numérico)
['name'] → Acceso a diccionario (clave string)


12. COMPARACIÓN VISUAL FINAL
LISTA DE DICCIONARIOS (tu caso):
python[                           # ← Inicio de LISTA
    {...},                  # ← Diccionario
    {...},                  # ← Diccionario
    {...}                   # ← Diccionario
]                           # ← Fin de LISTA
DICCIONARIO DE LISTAS (caso diferente):
python{                           # ← Inicio de DICCIONARIO
    'key1': [...],          # ← Lista
    'key2': [...],          # ← Lista
    'key3': [...]           # ← Lista
}                           # ← Fin de DICCIONARIO

______________________________________________________________________________________________________________________________________
Un paquete puede contener uno o más módulos relevantes.
un módulo puede contener múltiples objetos, tales como clases, funciones, etc. 

Un paquete es en realidad una carpeta que contiene uno o más archivos de módulo. Vamos a crear un paquete llamado mypackage, siguiendo los siguientes pasos:

La estructura de carpetas de su paquete debe verse así:
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py