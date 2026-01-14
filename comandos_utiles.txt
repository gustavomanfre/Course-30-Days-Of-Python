(Ctrl + `) -> Terminal > "New Terminal"
(Ctrl + F5)-> "Play" (triángulo) que aparece en la esquina superior derecha del editor. 
____________________________________________________________________________________________________________________________________________________________________________
Escribe esto en la terminal:
    cd "Day 10 - Loops"
    python3 loops.py

Tip: Escribe cd Day y presiona la tecla Tabulación (Tab) para que VS Code autocomplete el nombre de la carpeta con espacios automáticamente.
____________________________________________________________________________________________________________________________________________________________________________

Arepl for Python: Es increíble para aprender. Abre una ventana a la derecha que ejecuta el código en tiempo real mientras escribes, sin que tengas que darle a ningún botón.
AREPL es una maravilla porque no necesitas darle a ningún botón.

    Activación: Ya lo tienes abierto (es el panel negro a la derecha que dice "AREPL v3.0.0").
    Uso: Simplemente empieza a escribir código en el archivo loops.py de la izquierda.
    Resultados: AREPL evalúa el código mientras escribes.
        Si escribes print(fruits), el resultado aparecerá instantáneamente en el panel derecho.
        Si tienes un error, te lo marcará en rojo en el panel derecho en tiempo real.

Nota importante: En tu imagen, AREPL dice "Start typing or make a change". Haz un pequeño cambio (como borrar un espacio y volverlo a poner) y verás cómo se activa.

____________________________________________________________________________________________________________________________________________________________________________
El "Debug Console" (Para inspeccionar variables)

Si quieres ver qué hay dentro de tus acumuladores (sum_par, word_list) paso a paso mientras el bucle corre, el Debugger es tu mejor amigo.
    Pon un "Breakpoint": Haz clic justo a la izquierda del número de línea donde empieza tu bucle (aparecerá un punto rojo).
    Inicia el Debugging: Presiona F5 (elige "Python File").
    Inspecciona: El código se detendrá en ese punto. En el panel de la izquierda verás la sección "Variables". Podrás ver cómo cambian los valores en cada vuelta del bucle.
    Consola de depuración: En la parte inferior, busca la pestaña "Debug Console". Ahí puedes escribir el nombre de una variable (ej: invert_fruits) y presiona Enter para ver su estado actual en ese segundo.








    El error que ves en la terminal (imagen 2) ocurre porque estás intentando ejecutar un comando de Python directamente en la Bash (la terminal de Linux), y la terminal no entiende esa sintaxis.

Aquí te explico los dos motivos principales:
1. Bash vs. Python

La terminal (itc@itc-Latitude-7480:~$) espera comandos del sistema operativo (como ls, cd, mkdir). Cuando escribes help(random), la terminal intenta interpretarlo como un programa de sistema, no lo encuentra y lanza el "error sintáctico".

    help() es una función interna de Python. Para usarla, primero debes entrar al intérprete de Python escribiendo python3 en la terminal.

2. El módulo no está importado

Incluso dentro de Python, si haces help(random) sin antes haber puesto import random, te dará un error porque Python no sabrá qué es "random".
Cómo solucionarlo correctamente

Tienes dos formas de consultar la ayuda de un módulo desde la terminal:
Opción A: Desde el intérprete interactivo (Recomendado)

    En la terminal escribe: python3 (verás que el símbolo cambia a >>>).

    Escribe: import random

    Escribe: help(random)

Opción B: Comando directo desde la terminal

Si solo quieres leer la documentación sin entrar a Python, usa el comando pydoc:

    Escribe: python3 -m pydoc random

Nota sobre tu código de la Imagen 1

Relacionando esto con tu esquema de memoria:

    En el Global Frame, para que square_number o random existan, deben estar definidos o importados.

    Si intentas llamar a algo que no existe en el Heap, Python no puede crear el puntero (la flecha) y el programa falla.

¿Te gustaría que te ayude a crear un script que guarde toda la información del módulo random en un archivo de texto para que lo puedas leer con calma? Sería una buena forma de practicar el uso de sys y archivos.



____________________________________________________________________________________________________________________________________________________________________________
Recuerda que para ver el formato visual en VS Code, debes presionar Control + Shift + V.