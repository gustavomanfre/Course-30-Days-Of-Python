my_flask_app/           <-- Tu carpeta raíz (El proyecto)
├── venv/               <-- El cuarto de herramientas (Aislado)
├── app.py              <-- Tu código principal (A salvo)
├── requirements.txt    <-- La lista de compras
└── ... (otros .md)

gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python$ virtualenv --version
virtualenv 20.36.1 from /home/gustavo/.local/lib/python3.10/site-packages/virtualenv/__init__.py
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python$ 
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python$ cd ~/Documentos/Course-30-Days-Of-Python/Day\ 26\ -\ Python_web
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web$ mkdir 30DaysOfPython
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web$ cd 30DaysOfPython
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web/30DaysOfPython$ mkdir my_flask_app
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web/30DaysOfPython$ cd my_flask_app
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web/30DaysOfPython/my_flask_app$ virtualenv venv
gustavo@Desktop:~/Documentos/Course-30-Days-Of-Python/Day 26 - Python_web/30DaysOfPython/my_flask_app$ ls -la
total 12
drwxrwxr-x 3 gustavo gustavo 4096 ene 22 16:51 .
drwxrwxr-x 3 gustavo gustavo 4096 ene 22 16:48 ..
drwxrwxr-x 4 gustavo gustavo 4096 ene 22 16:51 venv
