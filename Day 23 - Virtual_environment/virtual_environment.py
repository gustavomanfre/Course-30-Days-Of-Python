"""
Paso 1: Verificar que tienes Python instalado
python3 --version

Paso 2: Instalar virtualenv (si no lo tienes)
sudo apt update
sudo apt install python3-virtualenv

En realidad, lo que está instalado en tu sistema es el módulo venv, que viene integrado por defecto con Python 3.12.

    venv: Es la herramienta oficial y estándar de Python para crear entornos virtuales. Ya la tienes, no necesitas bajar nada.

    virtualenv: Es una herramienta externa (de terceros) que hace lo mismo que venv, pero a veces es un poco más rápida o tiene funciones extra.

Mi punto era: No necesitas pelearte instalando virtualenv porque ya tienes venv listo para usar con el comando python3 -m venv.
2. ¿Por qué apt y no pip? (La gran duda)

Aquí es donde entra la seguridad de tu sistema operativo (Ubuntu/Debian).

    pip (El instalador de Python): Cuando instalas algo con pip de forma global, este descarga código de internet y lo mete dentro de las carpetas de Python de tu sistema operativo.

    El Riesgo: Muchas herramientas de Linux (como tu escritorio, el panel de control o el instalador de actualizaciones) están escritas en Python. Si pip actualiza una librería que el sistema usa, podrías romper Linux y que no vuelva a arrancar.

    apt (El instalador de Linux): Los paquetes que instalas con sudo apt están probados y aprobados por los desarrolladores de Ubuntu. Ellos garantizan que instalar python3-virtualenv no romperá el resto de tu sistema.

Para verificar que se instaló correctamente:
virtualenv --version

Paso 3: Crear la estructura de carpetas del proyecto

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

$ virtualenv venv
created virtual environment CPython3.12.3.final.0-64 in 250ms
  creator CPython3Posix(dest=/home/itc/Documentos/Course-30-Days-Of-Python/Day 23 - Virtual_environment/30DaysOfPython/my_flask_app/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/home/itc/.local/share/virtualenv)
    added seed packages: pip==24.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
itc@itc-Latitude-7480:~/Documentos/Course-30-Days-Of-Python/Day 23 - Virtual_environment/30DaysOfPython/my_flask_app$ 

Python crea una carpeta llamada venv con toda la infraestructura del entorno virtual.

$ ls -la
total 12
drwxrwxr-x 3 itc itc 4096 ene 22 00:16 .
drwxrwxr-x 3 itc itc 4096 ene 22 00:14 ..
drwxrwxr-x 4 itc itc 4096 ene 22 00:16 venv

**Salida esperada:**
    venv/

**Estructura interna de venv (puedes explorarla):**
```
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

Paso 6: Activar el entorno virtual
:~/Documentos/Course-30-Days-Of-Python/Day 23 - Virtual_environment/30DaysOfPython/my_flask_app$ source venv/bin/activate

Implementado hasta aca


¿Cómo saber si funcionó?
Tu prompt cambiará para incluir (venv) al inicio:
Antes:
bashC:\Users\TuUsuario\Documents\30DaysOfPython\my_flask_app>
Después:
bash(venv) C:\Users\TuUsuario\Documents\30DaysOfPython\my_flask_app>
Verificación adicional:
bashwhich python     # Mac/Linux

Paso 7: Verificar paquetes instalados (debe estar vacío)





"""