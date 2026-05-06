Borrar archivos

Hemos visto en la sección anterior, cómo hacer y eliminar un directorio usando el módulo os. De nuevo ahora, si queremos eliminar un archivo utilizamos el módulo os.

import os
os.remove('./files/example.txt')

Si el archivo no existe, el método de eliminación planteará un error, por lo que es bueno usar una condición como esta:

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

1. ¿Qué es os.path técnicamente?

Tienes razón: os es un módulo que importas. Sin embargo, path no es un simple atributo (como una variable) ni un método común.

os.path es un módulo dentro de otro módulo.

En Python, un módulo puede contener sub-módulos. Cuando haces import os, Python carga el módulo principal y, dentro de él, prepara el objeto path.

    ¿Por qué no lleva paréntesis? Porque no lo estás "ejecutando" en ese momento, sino que estás accediendo a un espacio de nombres que contiene muchas funciones útiles (como .exists(), .join(), etc.).

2. ¿Qué hace o qué tiene dentro?

El objetivo de os.path es la manipulación de rutas de archivos. Su "superpoder" es que es multiplataforma.

    En Windows, las carpetas se separan con barra invertida: C:\Users\Documentos.

    En Linux/Mac, se separan con barra normal: /Users/Documentos.

Si tú escribes las rutas a mano con barras, tu código podría fallar al cambiar de sistema operativo. os.path sabe en qué sistema estás y ajusta las reglas automáticamente.
3. ¿Qué contiene? (Atributos y Funciones)

Dentro de ese "atributo" path viven herramientas que hacen el trabajo sucio por ti:

    Funciones de consulta: (exists, isfile, isdir). Preguntan al disco duro qué hay ahí.

    Funciones de disección: * os.path.basename('/files/nota.txt') -> Te devuelve solo 'nota.txt'.

        os.path.dirname('/files/nota.txt') -> Te devuelve solo la carpeta '/files'.

    Funciones de pegado:

        os.path.join('carpeta', 'archivo.txt') -> Crea la ruta correcta según tu sistema.
Técnicamente, en Python esto se conoce como un submódulo. Cuando instalas Python, el módulo os viene con varios "ayudantes" internos, y path es el más importante de ellos porque se encarga específicamente de la lógica de las rutas (direcciones).

Aquí tienes el mapa mental de cómo están organizados:

    os (El Jefe): Se encarga de acciones directas con el Sistema Operativo (borrar archivos, crear carpetas, cambiar permisos, apagar procesos).

    os.path (El Especialista): No "hace" cambios físicos en el disco, sino que analiza y gestiona las direcciones. Es el que sabe si una ruta es válida, cómo se llama el archivo al final de una ruta larga, o si una dirección apunta a un archivo o a una carpeta.

Ejemplo práctico: El Jefe vs. El Especialista

Mira cómo trabajan juntos en este código:
Python

import os

ruta_completa = "./descargas/proyecto/manual.pdf"

# --- Aquí entra el ESPECIALISTA (os.path) ---
if os.path.exists(ruta_completa): # Pregunta: ¿Existe?
    nombre_archivo = os.path.basename(ruta_completa) # Extrae "manual.pdf"
    print(f"El archivo {nombre_archivo} está listo.")

    # --- Aquí entra el JEFE (os) ---
    # Solo cuando el especialista confirma, el jefe actúa
    # os.rename(ruta_completa, "./documentos/manual_final.pdf") 

¿Por qué se hace así?

La razón principal es que el módulo os es gigantesco. Separar la lógica de las rutas en os.path permite que el código sea más organizado. Además, como te mencioné antes, Python cambia lo que hay dentro de path dependiendo de si estás en Windows o Linux, sin que tú tengas que cambiar ni una letra de tu código.

____________________________________________________________________________________________________________________________________________________________
¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de texto usado para representar y transportar datos estructurados de forma simple y legible.

👉 JSON no es un lenguaje
👉 JSON no es un objeto
👉 JSON es texto (string)

¿Para qué se usa JSON?

JSON se usa principalmente para:
    Intercambiar datos entre sistemas
    Enviar datos entre frontend y backend
    Guardar configuraciones
    Comunicar APIs

Ejemplo típico:
    Un servidor envía datos en JSON
    Un cliente los recibe y los interpreta

Ejemplo JSON:

{
  "name": "Asabeneh",
  "country": "Finland",
  "skills": ["JavaScript", "Python"]
}

Ejemplo en Python
person_dict = {"name": "Ana", "age": 30}   # dict
person_json = '{"name": "Ana", "age": 30}' # JSON (str)

Regla mental importante
JSON es la forma escrita (texto) de los datos, no los datos en sí.

Frase para estudiar
JSON es un formato de texto estándar para representar y transportar datos estructurados de manera simple e independiente del lenguaje.

____________________________________________________________________________________________________________________________________________________________

JSON -> DICT

📌 Módulo necesario
Para trabajar con JSON en Python se usa el módulo estándar:

import json

🔁 1️⃣ De JSON (string) a diccionario Python: 
👉 Función: json.loads()
    loads = load string

Ejemplo
import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_dict = json.loads(person_json)

Qué pasa línea por línea
    person_json → es un str
    json.loads(person_json):
        Lee el texto JSON
        Lo interpreta
        Lo convierte en un dict

Resultado
type(person_dict)  # dict

📌 Ahora podés usarlo como diccionario

print(person_dict["name"])    # Asabeneh
print(person_dict["skills"])  # ['JavaScript', 'React', 'Python']
____________________________________________________________________________________________________________________________________________________________
DICT -> JSON
🔁 2️⃣ De diccionario Python a JSON (string)

👉 Función: json.dumps()
    dumps = dump string

Ejemplo
import json

person_dict = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

person_json = json.dumps(person_dict)

Qué pasa linea por linea:
    person_dict → dict

    json.dumps(person_dict):
        Convierte el diccionario
        A un string JSON válido

Resultado
type(person_json)  # str

3️⃣ JSON “bonito” (legible)

Por defecto, JSON sale en una sola línea.
Podés hacerlo más legible:

person_json = json.dumps(person_dict, indent=4)
print(person_json)


Salida:

{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScript",
        "React",
        "Python"
    ]
}

4️⃣ Resumen técnico clave (tabla)
Conversión	Función
JSON → dict	json.loads()
dict → JSON	json.dumps()
5️⃣ Regla mental definitiva

JSON es texto,
dict es estructura de datos.

loads → texto ➜ objeto
dumps → objeto ➜ texto

6️⃣ Frase para estudiar (nivel examen)

En Python, la conversión entre JSON y diccionarios se realiza mediante el módulo json, usando loads() para convertir texto JSON en objetos Python y dumps() para serializar objetos Python en texto JSON.

_____________________________________________________________________________________________________________________________________________________________

📌 Guardar datos como archivo JSON

La idea general es:
    Convertir un diccionario Python en texto JSON y escribirlo en un archivo .json.

Para eso usamos el módulo json.

1️⃣ Importar el módulo json
    import json

    -Importa el módulo estándar de Python para trabajar con JSON
    -Permite convertir entre:
        dict ⇄ JSON
        JSON ⇄ archivo

2️⃣ Diccionario Python (datos en memoria)
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person es un diccionario Python
    Vive en memoria RAM
    Todavía no es JSON
    Usa estructuras Python reales (dict, list, str)

3️⃣ Abrir un archivo para escritura
    with open('./files/json_example.json', 'w', encoding='utf-8') as f:

Qué hace exactamente
    open(...) abre (o crea) un archivo
    'w' → modo escritura
        Si el archivo existe → se sobrescribe
        Si no existe → se crea
    encoding='utf-8'
        Permite caracteres especiales (acentos, ñ, etc.)
    f es el archivo abierto
    Por qué usamos with
        Garantiza que el archivo:
        se cierre correctamente
        incluso si hay un error
Es la forma correcta y segura

4️⃣ Escribir el JSON en el archivo:

    json.dump(person, f, ensure_ascii=False, indent=4)

Esta es la línea más importante.

🔹 json.dump(...) (no dumps)
    Función	        Qué hace
    json.dumps()	dict → JSON (string)
    json.dump()	    dict → JSON directamente a un archivo
👉 dump escribe en disco.

🔹 Primer parámetro: person
    
    person

    -Diccionario Python
    -Datos fuente

🔹 Segundo parámetro: f

    f
    -Archivo abierto
    -Destino del JSON

🔹 ensure_ascii=False

    ensure_ascii=False

    -Permite caracteres Unicode
    -Evita que:
        "España" → "Espa\u00f1a"
✔ Hace el archivo más legible

🔹 indent=4
    indent=4

    -Agrega indentación (espacios)
    -Hace el JSON legible para humanos

Sin indent:
    {"name":"Asabeneh","country":"Finland"}

Con indent:
    {
        "name": "Asabeneh",
        "country": "Finland"
    }

5️⃣ Qué pasa internamente (paso a paso)

Python toma el dict person
    Lo convierte a texto JSON
    Aplica indentación
    Respeta UTF-8
    Escribe el texto en json_example.json
    Cierra el archivo automáticamente

6️⃣ Resultado final (archivo .json)

El archivo contendrá:
    {
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "skills": [
            "JavaScrip",
            "React",
            "Python"
        ]
    }

7️⃣ Resumen técnico corto
    json.dump() → escribe JSON en un archivo
    dict → convertido a texto JSON
    indent → legibilidad
    ensure_ascii=False → soporte Unicode
    with open() → manejo seguro del archivo

8️⃣ Frase para estudiar
El método json.dump() serializa un diccionario Python en formato JSON y lo escribe directamente en un archivo, permitiendo opciones de codificación e indentación para mejorar la legibilidad.

___________________________________________________________________________________________________________________________________________________________________________________

📊 Manejo de Archivos CSV en Python
📌 ¿Qué es un archivo CSV?

CSV (Comma-Separated Values) significa "valores separados por comas". Es el formato más común para intercambiar datos estructurados.

    Es un archivo de texto: Puede abrirse en cualquier editor (Bloc de notas, VS Code).

    Datos tabulares: Representa tablas con filas y columnas.

    Estructura: Cada línea del archivo es una fila y cada coma separa una columna.

Ejemplo de archivo csv_example.csv:
Fragmento de código

"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"

Interpretación visual:
name	country	city	skills
Asabeneh	Finland	Helsinki	JavaScript
📌 Lectura del archivo CSV en Python

Para leer estos archivos, seguimos un proceso lógico de 10 pasos:
1️⃣ Importar el módulo csv
Python

import csv

    Es el módulo estándar de Python.

    Maneja automáticamente problemas complejos como comillas dentro de los textos o saltos de línea.

2️⃣ Abrir el archivo
Python

with open('./files/csv_example.csv') as f:

    Usamos with para asegurar que el archivo se cierre automáticamente al terminar, evitando fugas de memoria.

3️⃣ Crear el lector (Lógica de la "Cremallera")
Python

csv_reader = csv.reader(f, delimiter=',')

    csv.reader(f): Transforma el archivo en un iterador.

    delimiter=',': Le indica a Python que la coma es la que separa las columnas.

4️⃣ Inicializar el contador
Python

line_count = 0

    Es fundamental para saber si estamos leyendo el encabezado (títulos) o los datos reales.

5️⃣ Recorrer el archivo fila por fila
Python

for row in csv_reader:

    En cada vuelta del bucle, row se convierte en una lista de strings.

    Ejemplo: row pasa de ser un texto a ["name", "country", ...].

6️⃣ Detectar y procesar el encabezado
Python

if line_count == 0:
    print(f'Column names are: {", ".join(row)}')
    line_count += 1

    La fila 0 siempre son los títulos. Usamos ", ".join(row) para imprimir los nombres de las columnas elegantemente.

7️⃣ Procesar las filas de datos
Python

else:
    print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
    line_count += 1

    Aquí accedemos a los datos por su índice: row[0] es el nombre, row[1] el país, etc.

8️⃣ Finalización
Python

print(f'Number of lines: {line_count}')

    Al terminar el bucle, informamos el total de líneas procesadas.

🏁 Output correcto esperado
Plaintext

Column names are :name, country, city, skills
    Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines: 2

    [!IMPORTANT] Nota técnica: Si el archivo tiene una línea vacía al final, el contador podría variar. El csv.reader devuelve siempre una lista, facilitando el acceso a los datos mediante índices numéricos.

💡 Resumen para estudiar

    "Un archivo CSV es un formato de texto que representa datos tabulares; en Python se lee usando el módulo csv, donde cada fila se convierte en una lista de valores, permitiendo separar la lógica del encabezado de la de los datos."

__________________________________________________________________________________________________________________________________________________________

# 1. 'def' define la función. 'file_path: str' es un "type hint" que indica que espera un texto. '-> tuple[int, int]' avisa que la función devolverá una tupla con dos números enteros.
def count_lines_words(file_path: str) -> tuple[int, int]:
    
    # 2. 'with' es un manejador de contexto que asegura que el archivo se cierre solo al terminar.
    # 'open' abre el archivo en modo lectura ("r") y 'as f' lo renombra como la variable 'f'.
    with open(file_path, "r") as f:
        
        # 3. 'f.readlines()' lee todo el archivo y guarda cada línea como un elemento de una lista.
        # 'lines: list[str]' es un "type hint" que aclara que 'lines' será una lista de cadenas de texto.
        lines: list[str] = f.readlines()
        
        # 4. 'return' entrega los resultados. 'len(lines)' cuenta cuántos elementos (líneas) hay en la lista.
        # La coma ',' crea automáticamente la tupla de retorno.
        # 'sum(...)' sumará los resultados de la expresión interna.
        # 'for line in lines' recorre cada línea.
        # 'line.split()' divide la línea en palabras (usando espacios) y 'len()' cuenta esas palabras.
        return len(lines), sum(len(line.split()) for line in lines)

Qué es una expresión generadora

Una expresión generadora es:

Una forma compacta de escribir un for que produce valores uno por uno, sin crear una lista en memoria.

Sintaxis general:

(expresión for elemento in iterable)

3️⃣ Analicemos la expresión generadora paso a paso
(len(line.split()) for line in lines)

🔹 for line in lines

Itera sobre cada elemento de lines

line toma cada valor de la lista

🔹 line.split()

Divide la línea en palabras (por espacios)

Ejemplo:

"Hola mundo Python".split()
# ['Hola', 'mundo', 'Python']

🔹 len(line.split())

Cuenta cuántas palabras hay en esa línea

🔹 Todo junto

Produce algo como:

3
5
2
...


Uno por vez, no todos juntos.

4️⃣ ¿Quién “consume” ese for?

👉 La función sum()

sum(len(line.split()) for line in lines)


sum() recibe la expresión generadora

Va pidiendo valores uno por uno

Los va sumando

Equivalente a:

total = 0
for line in lines:
    total += len(line.split())

5️⃣ Entonces, ¿qué devuelve la línea completa?
return len(lines), sum(len(line.split()) for line in lines)


Devuelve una tupla con dos valores:

len(lines) → cantidad de líneas

sum(...) → cantidad total de palabras

Ejemplo de retorno:

(10, 120)

6️⃣ Comparación clara (muy importante)
Con for tradicional
word_count = 0
for line in lines:
    word_count += len(line.split())

Con expresión generadora
word_count = sum(len(line.split()) for line in lines)


👉 Mismo resultado
👉 Menos código
👉 Más expresivo

7️⃣ Diferencia con list comprehension

Si fuera una lista:

sum([len(line.split()) for line in lines])


Pero:

Crea una lista completa en memoria ❌

La expresión generadora no ✔

8️⃣ Frase clave para que no se te mezcle

Ese for no es una estructura de control, es una expresión generadora que produce valores para otra función.

__________________________________________________________________________________________________________________________________________________________