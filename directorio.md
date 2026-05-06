🧭 Concepto base: rutas en Linux

En Linux todo es un árbol que empieza en:

/


Ese es el root del sistema de archivos.

Ejemplo:

/
├── home
│   └── gustavo
│       └── Documentos
├── etc
└── var

📁 cd → change directory

Sirve para moverte entre carpetas.

cd <ruta>

✅ 1️⃣ cd / → ruta absoluta

Empieza desde la raíz del sistema.

cd /etc


👉 Vas directo a /etc sin importar dónde estés.

✔ Siempre empieza con /
✔ Ruta completa

✅ 2️⃣ cd ./ → directorio actual

./ significa:

"el directorio donde estoy ahora"


Ejemplo:

cd ./templates


Es lo mismo que:

cd templates


👉 Se usa más en scripts o comandos ejecutables:

./script.sh


Significa:

ejecutar script.sh desde el directorio actual

✅ 3️⃣ cd ../ → subir un nivel

.. significa:

directorio padre


Ejemplo:

Estás en:

/home/gustavo/Documentos

cd ..


Ahora estás en:

/home/gustavo

✅ 4️⃣ cd ../../ → subir varios niveles

Cada .. sube uno.

cd ../../


Ejemplo:

/home/gustavo/Documentos/proyecto


↓

/home/gustavo

✅ 5️⃣ cd ~ → home del usuario

~ significa:

/home/tu_usuario


Para vos:

~ = /home/gustavo


Ejemplo:

cd ~


o simplemente:

cd


👉 Ambos van al home.

✅ 6️⃣ cd - → volver al directorio anterior

Muy útil.

Ejemplo:

cd /etc
cd /var
cd -


Volvés a:

/etc

✅ 7️⃣ cd ~/carpeta → ruta desde tu home

Ejemplo:

cd ~/Documentos


=

cd /home/gustavo/Documentos

✅ 8️⃣ Rutas relativas normales

Si estás en:

/home/gustavo


Entonces:

cd Documentos


funciona porque existe dentro del actual.

⚠️ Importante: espacios en rutas

Tu caso típico:

Day 26 - Python_web


Esto rompe cd.

Soluciones:

✔ con comillas
cd "Day 26 - Python_web"

✔ con escape
cd Day\ 26\ -\ Python_web

🧪 Ejemplo real (tu proyecto)

Estás en:

/home/gustavo


Ir a Flask:

cd ~/Documentos/Course-30-Days-Of-Python/Day\ 26\ -\ Python_web/30DaysOfPython/my_flask_app

🧠 Resumen mental rápido

Pensalo así:

/ → raíz del sistema

~ → tu casa

. → donde estás

.. → subir

- → volver

🎯 Ejercicio mental rápido

Si estás en:

/etc/openvpn/server

Comando	Resultado
cd ..	/etc/openvpn
cd ../..	/etc
cd /	/
cd ~	/home/gustavo
cd ./	igual
cd -	anterior

Si querés, te hago un mapa visual de tu sistema Linux con ejemplos reales de tu servidor y tu PC para que te quede grabado para siempre.