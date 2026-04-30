# FLUJO DE COMANDOS - EJEMPLOS

# Paso 1: Verificar que tienes Python instalado
python3 --version

# Paso 2: Instalar virtualenv (si no lo tienes)
sudo apt update
sudo apt install python3-virtualenv

¡Bienvenido a la era de PEP 668! Lo que estás viendo no es un error de tu computadora, 
sino una nueva medida de seguridad en versiones modernas de Linux (como Ubuntu 24.04 con Python 3.12).

El sistema te está diciendo: "No me instales paquetes con pip directamente en el Python del sistema, porque podrías romper herramientas críticas del sistema operativo".

Aquí tienes las dos formas correctas de solucionar esto según lo que necesites:

# Opción 1: Usar venv (La recomendada para tu curso)
Ya no necesitas instalar virtualenv por separado. Python 3.12 ya incluye su propio gestor de entornos. Sigue estos pasos en tu terminal:

    Crea el entorno virtual:
    Bash
      python3 -m venv .venv

    (Esto creará una carpeta llamada .venv en tu proyecto).

    Actívalo:
    Bash

    source .venv/bin/activate

    (Verás que tu terminal ahora muestra (.venv) al principio. Ahora ya puedes usar pip install libremente dentro de ese entorno).

# Opción 2: Instalar virtualenv vía el sistema (Apt)

Si realmente quieres tener la herramienta virtualenv disponible globalmente como intentabas antes, debes usar el gestor de paquetes de Linux (apt), no pip:
Bash

sudo apt update
sudo apt install python3-virtualenv

# 🔍 ¿Por qué sucede esto? (Explicación rápida)

Antiguamente, si hacías pip install de algo que requería una versión específica de una librería, podías "pisar" una librería que Ubuntu necesitaba para funcionar (como el gestor de actualizaciones o la interfaz gráfica). Ahora, Linux bloquea el pip global para obligarnos a usar Entornos Virtuales, que son como "cajas de arena" donde puedes instalar lo que quieras sin afectar a nadie más.

1. En realidad, lo que está instalado en tu sistema es el módulo venv, que viene integrado por defecto con Python 3.12.
    venv: Es la herramienta oficial y estándar de Python para crear entornos virtuales. Ya la tienes, no necesitas bajar nada.
    virtualenv: Es una herramienta externa (de terceros) que hace lo mismo que venv, pero a veces es un poco más rápida o tiene funciones extra.

Mi punto era: No necesitas pelearte instalando virtualenv porque ya tienes venv listo para usar con el comando python3 -m venv.

2. ¿Por qué apt y no pip? (La gran duda)
Aquí es donde entra la seguridad de tu sistema operativo (Ubuntu/Debian).

    -pip (El instalador de Python): Cuando instalas algo con pip de forma global, este descarga código de internet y lo mete dentro de las carpetas de Python de tu sistema operativo.

    -El Riesgo: Muchas herramientas de Linux (como tu escritorio, el panel de control o el instalador de actualizaciones) están escritas en Python. Si pip actualiza una librería que el sistema usa, podrías romper Linux y que no vuelva a arrancar.

    -apt (El instalador de Linux): Los paquetes que instalas con sudo apt están probados y aprobados por los desarrolladores de Ubuntu. Ellos garantizan que instalar python3-virtualenv no romperá el resto de tu sistema.

Cuando instalas con sudo apt install python3-virtualenv, el sistema operativo descarga un paquete pre-compilado y probado por los desarrolladores de Ubuntu.

    Ubicación: Se instala en carpetas protegidas como /usr/bin/ y /usr/lib/python3/dist-packages/.

    Control de versiones: Ubuntu sabe exactamente qué versión instaló. Si otra herramienta del sistema necesita una librería específica, apt se asegura de que la actualización de virtualenv no rompa esa dependencia.

3. ¿Por qué apt no reemplaza/rompe el sistema?
A diferencia de pip, que descarga lo más nuevo de internet sin mirar a quién afecta, apt utiliza un sistema de dependencias estricto.

    -Si virtualenv necesitara una librería que el panel de control de Ubuntu también usa, apt solo permitirá la instalación si la versión es compatible con ambos.
    -Los paquetes de apt están diseñados para coexistir con el sistema operativo.

4. La diferencia con pip (El riesgo)
Cuando usas sudo pip install, le das permiso a Python para entrar en las carpetas del sistema y sobrescribir cualquier archivo.

    El desastre: Si pip instala una versión de la librería requests más nueva de la que Ubuntu usa para su gestor de actualizaciones, el gestor de actualizaciones podría dejar de funcionar.
    PEP 668: Por este riesgo, las versiones modernas como la tuya (Python 3.12) bloquean el pip global para proteger la estabilidad de Linux.

5. El concepto de "Paquetes Debian" (.deb)
Cuando instalas con apt, no estás bajando código suelto de internet. Estás bajando un paquete que los ingenieros de Ubuntu ya probaron en miles de computadoras. Ellos garantizan que:

    -Las versiones de las librerías coincidan con las que tu escritorio y sistema necesitan.
    -Si hay una actualización, esta no moverá archivos críticos de lugar.

6. ¿Qué pasa si hay un conflicto?
Si intentas instalar algo por apt que realmente rompería el sistema, el comando fallará y te dirá: "Los siguientes paquetes tienen dependencias incumplidas". apt prefiere no instalar nada antes que romper tu Linux. pip no tiene esa "conciencia" del sistema operativo.

7. La jerarquía de carpetas (El secreto)
Linux separa las cosas para evitar accidentes:

    /usr/bin y /usr/lib: Aquí es donde apt guarda las herramientas del sistema (como el virtualenv que instalaste). Es "territorio oficial".
    .venv/ (tu entorno local): Aquí es donde pip guarda tus librerías de trabajo. Es tu "caja de arena" privada.

# Para verificar que se instaló correctamente:
virtualenv --version

# Paso 3: Crear la estructura de carpetas del proyecto

# Navega al escritorio (o donde prefieras)
cd ~/Documentos/Course-30-Days-Of-Python/Day\ 23\ -\ Virtual_environment

# Crea la carpeta principal
mkdir 30DaysOfPython

# Entra a esa carpeta
cd 30DaysOfPython

# Crea la carpeta del proyecto
mkdir my_flask_app

# Entra a la carpeta del proyecto
cd my_flask_app

**Tu ubicación actual debe ser:**
itc@itc-Latitude-7480:~/Documentos/Course-30-Days-Of-Python/Day 23 - Virtual_environment/30DaysOfPython/my_flask_app$ 

# Creamos el entorno virtual.
$ virtualenv venv
created virtual environment CPython3.12.3.final.0-64 in 250ms
  creator CPython3Posix(dest=/home/itc/Documentos/Course-30-Days-Of-Python/Day 23 - Virtual_environment/30DaysOfPython/my_flask_app/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/home/itc/.local/share/virtualenv)
    added seed packages: pip==24.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

Python crea una carpeta llamada venv con toda la infraestructura del entorno virtual.

$ ls -la
total 12
drwxrwxr-x 3 itc itc 4096 ene 22 00:16 .
drwxrwxr-x 3 itc itc 4096 ene 22 00:14 ..
drwxrwxr-x 4 itc itc 4096 ene 22 00:16 venv

**Salida esperada:**
    venv/

**Estructura interna de venv (puedes explorarla):**

my_flask_app/
└── venv/
    ├── Scripts/        (bin/ en Mac/Linux)
    │   ├── activate
    │   ├── activate.bat
    │   ├── python.exe
    │   └── pip.exe
    ├── Lib/            (lib/ en Mac/Linux)
    │   └── site-packages/
    ├── Include/        (include/ en Mac/Linux)
    └── pyvenv.cfg

# Paso 6: Activar el entorno virtual
$ source venv/bin/activate

¿Cómo saber si funcionó?
Tu prompt cambiará para incluir (venv) al inicio:
Antes:
bash
C:\Users\TuUsuario\Documents\30DaysOfPython\my_flask_app>

Después:
bash(venv) C:\Users\TuUsuario\Documents\30DaysOfPython\my_flask_app>

Verificación adicional:
which python     # Mac/Linux
Esto debe mostrar la ruta dentro de tu carpeta venv, no la ruta global de Python.

Paso 7: Verificar paquetes instalados (debe estar vacío)
pip list



**Salida esperada:**

Package    Version
---------- -------
pip        21.x.x
setuptools 58.x.x

Paso 8: Instalar Flask en el entorno virtual
pip install Flask

Paso 9: Verificar las dependencias instaladas
pip freeze

Paso 10: Guardar las dependencias en requirements.txt
pip freeze > requirements.txt
> redirige la salida a un archivo
requirements.txt es el nombre estándar para listar dependencias

Verificar que se creó:


# Mac/Linux
cat requirements.txt

Paso 11: Crear un archivo .gitignore
Crea un archivo llamado .gitignore en la raíz de tu proyecto:

Para Mac/Linux:
bash
touch .gitignore
```

Luego abre el archivo con un editor de texto y agrega:
```
# Entorno virtual
venv/
env/

# Archivos de Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Archivos de distribución
*.egg-info/
dist/
build/

# Variables de entorno
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Sistema operativo
.DS_Store
Thumbs.db

Paso 12: Crear una aplicación Flask simple de prueba
Crea un archivo llamado app.py:
# Mac/Linux
touch app.py

Abre app.py con tu editor favorito y agrega:
python from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return '''
    <h1>¡Mi Primera Aplicación Flask!</h1>
    <p>El entorno virtual está funcionando correctamente.</p>
    <p>Flask versión: 3.0.0</p>
    '''

# Ruta adicional
@app.route('/hola/<nombre>')
def hola(nombre):
    return f'<h2>¡Hola, {nombre}! Bienvenido a mi app Flask.</h2>'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)


Paso 13: Ejecutar la aplicación
Con el entorno virtual activado (debes ver (venv)), ejecuta:
python app.py

```

**Salida esperada:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in production.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

**Abre tu navegador y visita:**
- http://127.0.0.1:5000/ → Verás "¡Mi Primera Aplicación Flask!"
- http://127.0.0.1:5000/hola/Juan → Verás "¡Hola, Juan!"

**Para detener el servidor:** Presiona `Ctrl + C` en la terminal

---

# Paso 14: Estructura final del proyecto

```
30DaysOfPython/
└── my_flask_app/
    ├── venv/                 # Entorno virtual (NO subir a Git)
    ├── app.py                # Tu aplicación Flask
    ├── requirements.txt      # Lista de dependencias
    └── .gitignore           # Archivos a ignorar en Git

Paso 15: Desactivar el entorno virtual
Cuando termines de trabajar:
bash
deactivate
Tu prompt volverá a la normalidad (sin (venv)).


🔄 Flujo de trabajo diario
Al comenzar a trabajar:
bashcd 30DaysOfPython/my_flask_app
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
python app.py

Al terminar:
bash# Detén el servidor con Ctrl+C
deactivate

✅ Verificación final
Para confirmar que todo está correcto, ejecuta estos comandos con el entorno activado:
bash# 1. Verificar que venv está activo
echo $VIRTUAL_ENV    # Mac/Linux (debe mostrar la ruta)
echo %VIRTUAL_ENV%   # Windows (debe mostrar la ruta)

# 2. Verificar Python correcto
which python         # Mac/Linux (debe apuntar a venv/bin/python)
where python         # Windows (debe apuntar a venv\Scripts\python.exe)

# 3. Verificar Flask instalado
python -c "import flask; print(flask.__version__)"
# Debe imprimir: 3.0.0 (o similar)

🔍 Una observación importante sobre tu Entorno Virtual

He notado algo curioso en tu comando de activación que es bueno que sepas:

En tu terminal ejecutaste: source /home/.../Course-30-Days-Of-Python/.venv/bin/activate

    Lo que hiciste: Activaste un entorno virtual llamado .venv que está en la carpeta principal del curso (arriba del todo).

    Lo que muestra tu carpeta de trabajo: Dentro de my_flask_app tienes otra carpeta llamada venv (sin el punto).

¿Qué significa esto? Ahora mismo estás usando el "motor" de Python que está en la carpeta principal del curso, pero estás guardando tus archivos de código (app.py) dentro de la carpeta del día 23. ¡Esto funciona perfectamente! Solo recuérdalo para no confundirte si intentas buscar las librerías instaladas dentro de la carpeta venv local de my_flask_app.

Siguiente paso: Abre ese archivo app.py (haciendo clic en él en la barra lateral) y pega el código de prueba de Flask (Paso 12 de tu guía).
"""