import os
import json
import csv
import re
from collections import Counter
#sys.path.append("data")
#from stop_words import stop_words as sw # Used in Level 2-7

# 💻 Ejercicios: Día 19 - Manejo de Archivos 

# ==========================================
# Ejercicios: Nivel 1
# ==========================================

# 1. Escriba una función que cuente el número de líneas y el número de palabras en un texto.
# Archivos: obama_speech.txt, michelle_obama_speech.txt, donald_speech.txt, melina_trump_speech.txt 

# Define la función que recibe una ruta (texto) y promete devolver una tupla de dos enteros

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
        #(expresión for elemento in iterable)
        return len(lines), sum(len(line.split()) for line in lines)
    
    
# print(f"Obama: {count_lines_and_words('./data/obama_speech.txt')}")
# print(f"Michelle: {count_lines_and_words('./data/michelle_obama_speech.txt')}")
# print(f"Donald: {count_lines_and_words('./data/donald_speech.txt')}")
# print(f"Melina: {count_lines_and_words('./data/melina_trump_speech.txt')}")


# 2. Lea el archivo countries_data.json y encuentre los diez idiomas más hablados.

# 1. 'def' define la función. 'file_path: str' es la ruta del JSON y 'n: int' es cuántos idiomas queremos ver.
def most_spoken_languages(file_path: str, n: int):
    
    # 2. Abrimos el archivo en modo lectura ('r'). 'encoding="utf-8"' es vital para leer nombres de idiomas con tildes o caracteres especiales.
    with open(file_path, "r", encoding="utf-8") as f:
        # 3. 'json.load(f)' transforma el texto del archivo JSON en una lista de diccionarios de Python y la guarda en 'countries'.
        countries = json.load(f)
    
    # 4. Inicializamos un diccionario vacío donde la 'llave' será el idioma y el 'valor' será cuántas veces aparece.
    language_counts: dict[str, int] = {}
    
    # 5. Esta es una "List Comprehension" anidada: recorre cada 'country' en 'countries', 
    # y por cada país, recorre su lista de 'languages', extrayendo cada 'lang' individual a una lista plana.
    all_languages = [lang for country in countries for lang in country["languages"]]

    # 6. Iteramos sobre nuestra gran lista de idiomas (donde hay muchos repetidos).
    for lang in all_languages:
        # 7. 'language_counts.get(lang, 0)' busca el idioma; si no existe, devuelve 0. 
        # Luego le suma 1 y actualiza el diccionario. Así evitamos errores de "llave no encontrada".
        # language_counts[espaniol] = language_counts.get(espaniol, 0) + 1, 
        # Esto dice que si el idioma ya existe, le suma 1 al valor almacenado; si no, lo inicializa en 0 y luego le suma 1.
        language_counts[lang] = language_counts.get(lang, 0) + 1

    # 8. Aquí pasan tres cosas:
    # A) '[(count, lang) for lang, count in language_counts.items()]' crea una lista de tuplas poniendo el número PRIMERO para poder ordenar por cantidad.
    # B) 'sorted(..., reverse=True)' ordena la lista de mayor a menor frecuencia.
    # C) '[:n]' hace un "slicing" para devolver solo los primeros 'n' elementos (los más hablados).
    # language_counts hasta esta línea es un diccionario como {'English': 91, 'French': 45, ...}
    # language_counts.items() convierten el diccionario en una lista de tuplas: [('English', 91), ('French', 45), ...]
    #Cada tupla es (lang, count), la recibe lang y count en el for y las invierte en (count, lang) para que sorted pueda ordenar por count
    #Como es una expresión de lista, crea una nueva lista con las tuplas invertidas (count, lang)
    # sorted(...) recibe una lista de tuplas y ordena esa lista de tuplas por el primer elemento de cada tupla (count) en orden descendente (reverse=True)
    return sorted([(count, lang) for lang, count in language_counts.items()], reverse=True)[:n]



# print(most_spoken_languages(filename='./data/countries_data.json', limit=10))
# print(most_spoken_languages(filename='./data/countries_data.json', limit=3))


# 3. Lea el archivo countries_data.json y cree una lista de los diez países más poblados.

# 1. 'def' define la función. Los "type hints" indican que devuelve una lista de diccionarios.
# 'int|str' significa que los valores del diccionario pueden ser números o texto.
def most_populated_countries(file_path: str, n: int) -> list[dict[str, int|str]]:
    
    # 2. Abrimos el archivo en modo lectura ('r') con UTF-8 para asegurar que los nombres de países se lean bien.
    with open(file_path, "r", encoding="utf-8") as f:
        # 3. 'json.load(f)' convierte el contenido del JSON en una lista de diccionarios de Python.
        countries = json.load(f)

    # 4. Usamos "List Comprehension" para crear una NUEVA lista más simple.
    # Por cada país en la lista original, creamos un diccionario pequeño solo con "country" y "population".
    # countries tiene diccionarios como {"name": "Afghanistan", "population": 40218234, ...}
    # Empezamos con countries pasando cada diccionario a country
    # Por cada country, creamos un nuevo diccionario {"country": country["name"], "population": country["population"]} y lo añadimos a population_list
    population_list: list[dict[str, int|str]] = [
        {"country": country["name"], "population": country["population"]} 
        for country in countries
    ]
    # -------------------------------------------------------------
    # AQUÍ OCURRE LA MAGIA DEL ORDENAMIENTO
    # -------------------------------------------------------------

    # sorted() es una función incorporada de Python que:
    # 1) Recorre internamente la lista (NO necesitamos escribir un for)
    # 2) Ordena los elementos
    # 3) Devuelve una NUEVA lista ordenada (no modifica la original)

    # population_list:
    # Es la lista que queremos ordenar.
    # Contiene diccionarios como:
    # {"country": "China", "population": 1440000000}

    # key= :
    # key espera UNA FUNCIÓN.
    # Esa función se va a ejecutar UNA VEZ por cada elemento de la lista.
    #
    # Python hace internamente algo equivalente a:
    #
    # for x in population_list:
    #     valor = key(x)
    #     # usa ese valor para comparar y ordenar
    #
    # Nosotros NO escribimos ese for, sorted() lo hace por nosotros.

    # lambda x: x["population"]
    #
    # Esto es una función anónima (lambda).
    # - x representa CADA diccionario de la lista
    # - x["population"] obtiene el valor de población de ese diccionario
    #
    # Ejemplo:
    # x = {"country": "China", "population": 1440000000}
    # x["population"] → 1440000000
    #
    # Ese número es el que Python usa para ordenar.

    # reverse=True:
    # - False (por defecto): orden ascendente (menor a mayor)
    # - True: orden descendente (mayor a menor)
    #
    # Como queremos los países MÁS poblados primero,
    # usamos reverse=True.

    # [:n]:
    # Una vez ordenada la lista,
    # cortamos la lista y devolvemos solo los primeros 'n' elementos.

    return sorted(
        population_list,                 # Lista de diccionarios a ordenar
        key=lambda x: x["population"],    # Función que indica POR QUÉ valor ordenar
        reverse=True                      # Orden descendente (mayor a menor)
    )[:n]                                # Devuelve solo los primeros n países.
                                        # sorted devuelve una lista, y el slicing [:n] corta esa lista.

# print(most_populated_countries(filename='./data/countries_data.json', limit=10))
# print(most_populated_countries(filename='./data/countries_data.json', limit=3))


# ==========================================
# Ejercicios: Nivel 2
# ==========================================

# 4. Extraiga todas las direcciones de correo electrónico de email_exchange_big.txt. 
#
#  TODAVIA NO HE VISTO REGEX ASI QUE LO DEJO PARA MAS ADELANTE

import re # 1. ¡Importante! Debes importar el módulo 're' para usar expresiones regulares.

# 2. Definimos la función. 'file_path: str' es la ruta y '-> list[str]' indica que devolverá una lista de textos (emails).
def get_email(file_path: str) -> list[str]:
    
    # 3. Abrimos el archivo en modo lectura ('r'). Usamos 'with' para que se cierre solo al terminar.
    with open(file_path, "r") as f:
        # 4. 'f.read()' lee TODO el contenido del archivo y lo guarda como una única cadena de texto gigante en 'raw_txt'.
        raw_txt: str = f.read()

    # 5. Aquí ocurre la magia de Regex:
    # 're.findall()' busca todas las coincidencias del patrón en el texto y las devuelve en una lista.
    # El prefijo 'r' antes de las comillas indica que es una "raw string" (cadena en crudo), 
    # necesaria para que Python no confunda las barras invertidas de Regex con comandos especiales.
    
    # Desglose del patrón r"[\w\.-]+@[\w\.-]+\.\w+":
    # [\w\.-]+  => Busca uno o más caracteres que sean letras, números, guiones bajos, puntos o guiones.
    # @         => Busca el símbolo '@' literal.
    # [\w\.-]+  => Busca el dominio (ej: 'gmail', 'outlook.co').
    # \.        => El punto es un carácter especial en Regex, así que '\.' le dice: "busca un punto real".
    # \w+       => Busca la terminación (ej: 'com', 'org', 'es').
    all_emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", raw_txt)
    
    # 6. Devolvemos la lista con todos los correos electrónicos encontrados en el archivo.
    return all_emails

# 5. Encuentra las palabras más comunes en el idioma inglés.
# Debe devolver una serie de tuplas en orden descendente.

# 1. Definimos la función. Recibe la ruta y el número 'n' de palabras deseadas.
# Retorna una lista de tuplas, donde cada tupla es (frecuencia, palabra).
def find_most_common_words(file_path: str, n: int) -> list[tuple]:
    
    # 2. Abrimos el archivo. 'f.read()' obtiene todo el texto.
    # '.lower()' convierte todo a minúsculas para que "Python" y "python" se cuenten como la misma palabra.
    with open(file_path, "r") as f:
        raw_text: str = f.read().lower()
    
    # 3. 're.findall' busca patrones. 
    # '\b' es un "word boundary" (límite de palabra): asegura que no capturemos letras dentro de otras palabras.
    # '[a-z]+' busca secuencias de una o más letras (ignora números y símbolos de puntuación).
    all_words = re.findall(r"\b[a-z]+\b", raw_text)
    
    # 4. Creamos el diccionario de frecuencias.
    word_count: dict[str, int] = {}
    for word in all_words:
        # 5. Si la palabra ya existe, suma 1. Si no existe (.get devuelve 0), inicia en 1.
        word_count[word] = word_count.get(word, 0) + 1
    
    # 6. Transformación y Ordenamiento:
    # A) Convertimos el diccionario en una lista de tuplas (count, word) mediante una List Comprehension.
    # B) 'sorted(..., reverse=True)' ordena de mayor a menor frecuencia.
    # C) '[:n]' corta la lista para devolver solo el "Top N".
    return sorted([(count, word) for word, count in word_count.items()], reverse=True)[:n]

# print(find_most_common_words('sample.txt', 10))

# The previous was my original approach. However, when refactoring my code, I came across this different approach using set(). This is significantly slower since list.count() runs in O(n) and is called for every unique word (O(n²) overall). Nevertheless, I will leave it because I thought it was interesting
def find_most_common_wordsV2(file_path: str, n: int) -> list[tuple]:
    with open(file_path, "r") as f:
        raw_text:str = f.read().lower()
    
    all_words = re.findall(r"\b[a-z]+\b", raw_text)
    
    word_count = {word: all_words.count(word) for word in set(all_words)}
    
    return sorted([(count, word) for word, count in word_count.items()], reverse=True)[:n]


# 6. Utilice la función anterior para encontrar las 10 palabras más frecuentes en:
# 1. 'print()' es la función de salida que enviará todo el texto procesado a la consola.
print(
    # 2. 'f' indica que es un f-string (cadena formateada), lo que permite insertar código entre {}.
    # Usamos comillas dobles " " para envolver todo el bloque del f-string.
    # '\n' es un carácter de escape que inserta un "salto de línea" para que el texto sea legible.
    f"Obama's speech 10 most frequent words:\n"
    
    # 3. Entre llaves { } llamamos a la función definida anteriormente.
    # IMPORTANTE: Usamos comillas simples './data/...' para la ruta del archivo.
    # Si usáramos dobles, Python pensaría que el f-string terminó ahí y daría error.
    # Pasamos el archivo y el número 10 para obtener las 10 palabras más comunes.
    # \n\n" añade dos saltos de línea para separar visualmente cada bloque de resultados.
    # Un ejemplo de separar visualmente los resultados, seria: palabras mas comunes de Obama, luego dos espacio, luego las de Michelle, etc.
    f"{find_most_common_words('./data/obama_speech.txt', 10)}\n\n"
    
    # 4. Repetimos el proceso para el discurso de Michelle.
    # El f-string evalúa la función, obtiene la lista de tuplas y la convierte en texto automáticamente.
    f"Michelle's speech 10 most frequent words:\n"
    f"{find_most_common_words('./data/michelle_obama_speech.txt', 10)}\n\n"
    
    # 5. Ejecución para el discurso de Trump. 
    # Cada llamada a la función abre el archivo, lo limpia, cuenta palabras y devuelve el Top 10.
    f"Trump's speech 10 most frequent words:\n"
    f"{find_most_common_words('./data/donald_speech.txt', 10)}\n\n"
    
    # 6. Última ejecución para el discurso de Melina. 
    # Cerramos el paréntesis del print después de haber concatenado todas las cadenas.
    f"Melina's speech 10 most frequent words:\n"
    f"{find_most_common_words('./data/melina_trump_speech.txt', 10)}"
)

#  TODAVIA NO HE VISTO REGEX ASI QUE LO DEJO PARA MAS ADELANTE
#
# ==========================================
# 7. Escriba una aplicación que compruebe la similitud entre dos textos (Michelle vs Melina).
# Necesitarás limpiar el texto, eliminar stop_words y calcular la similitud.

# 1. Función para extraer palabras limpias de un archivo.
# Devuelve una lista de strings con todas las palabras encontradas.
def clean_text(file: str) -> list[str]:
    # Abrimos el archivo en modo lectura.
    with open(file, "r") as f:
        # Leemos todo el contenido y lo pasamos a minúsculas para normalizar.
        raw_text: str = f.read().lower()

    # Usamos Regex para extraer solo secuencias de letras, ignorando signos y números.
    # '\b' marca el límite de palabra para asegurar capturas precisas.
    return re.findall(r"\b[a-z]+\b", raw_text)

# 2. Función para filtrar las "stop words" (palabras de soporte como 'the', 'is', 'of').
def remove_support_words(all_words: list[str]) -> list[str]:
    # Usamos una List Comprehension para crear una nueva lista.
    # Solo incluimos la palabra si NO está en la lista global de stop_words 'sw'.
    return [word for word in all_words if word not in sw]

# 3. Función principal para calcular el índice de similitud de Jaccard.
# Recibe las rutas de dos archivos y devuelve un número entre 0.0 (nada parecido) y 1.0 (idénticos).
def check_txt_similarity(text_path1: str, text_path2: str) -> float:
    # Procesamos el primer texto: limpiamos -> quitamos stop_words -> convertimos a SET (conjunto).
    # El set() es clave porque elimina duplicados y permite operaciones matemáticas de conjuntos.
    words1: set[str] = set(remove_support_words(clean_text(text_path1)))
    
    # Hacemos lo mismo con el segundo texto.
    words2: set[str] = set(remove_support_words(clean_text(text_path2)))
    
    # Calculamos la INTERSECCIÓN: palabras que aparecen en AMBOS conjuntos.
    intersection: set[str] = words1.intersection(words2)
    
    # Calculamos la UNIÓN: todas las palabras únicas que existen entre los dos textos.
    union: set[str] = words1.union(words2)
    
    # Aplicamos la fórmula de Jaccard: (elementos comunes) / (total de elementos únicos).
    # Usamos 'round(..., 2)' para limitar el resultado a dos decimales.
    # 'if union else 0.0' evita el error de división por cero si ambos archivos están vacíos.
    return round(len(intersection) / len(union), 2) if union else 0.0

# 8. Encuentra las 10 palabras más repetidas en romeo_and_juliet.txt.
print(f"The 10 most repeated words in romeo and juliet are: {find_most_common_words("./data/romeo_and_juliet.txt", 10)}")

# 9. Lea el archivo hacker_news.csv y averigüe:
# a) Número de líneas que contienen Python o python
# b) Número de líneas que contienen JavaScript, Javascript o javascript
# c) Número de líneas que contienen Java y NO JavaScript

import csv  # Importamos el módulo csv para poder leer archivos CSV correctamente

# Definimos una función que recibe la ruta del archivo CSV como string
def count_languages(file_path: str):
    # Contador de líneas que contienen la palabra "python"
    py_count = 0

    # Contador de líneas que contienen la palabra "javascript"
    js_count = 0

    # Contador de líneas que contienen "java" pero NO "javascript"
    java_count = 0
    
    # Abrimos el archivo CSV en modo lectura ("r")
    # with asegura que el archivo se cierre automáticamente al terminar
    with open(file_path, "r") as csvf:
        
        # csv.reader permite leer el archivo línea por línea,
        # donde cada línea se devuelve como una lista de valores (columnas)
        #Estás creando un objeto lector (iterable). 
        #Es como un puntero que está listo para recorrer el archivo fila por fila.
        # id	        title	                    url	                num_points
        # 1	        Learning Python is fun	    http://python.org	        100
        # 2	        JS vs Java: The battle	    http://battle.com	        50
        # 3	        Java for beginners	        http://java.com	            80

        csvreader = csv.reader(csvf)

        # Recorremos cada fila (row) del archivo CSV
        for row in csvreader:
            
            #Vuelta1: row es una lista (por ejemplo: ["title", "url", "author", ...])
            #Vuelta2: row recibe ['1', 'Learning Python is fun', 'http://python.org', '100']
            #VUelta3: row recibe ['2', 'JavaScript is great', 'http://js.com', '150']
            # " ".join(row) une todos los elementos de la fila en un solo string
            # .lower() convierte todo a minúsculas para evitar problemas de mayúsculas
            line = " ".join(row).lower()
            
            # Si la palabra "python" aparece en la línea,
            # aumentamos el contador de Python
            if "python" in line:
                py_count += 1
            
            # Si la palabra "javascript" aparece en la línea,
            # aumentamos el contador de JavaScript
            if "javascript" in line:
                js_count += 1
            
            # Si la palabra "java" aparece en la línea
            # Y al mismo tiempo "javascript" NO aparece,
            # entonces contamos solo Java (excluyendo JavaScript)
            if "java" in line and "javascript" not in line:
                java_count += 1
    
    # Devolvemos un string con los resultados finales formateados
    return (
        f"Python count: {py_count}\n"
        f"JavaScript count: {js_count}\n"
        f"Java (not JS) count: {java_count}"
    )

# Llamamos a la función pasando la ruta del archivo CSV
# e imprimimos el resultado en pantalla
print(count_languages("./data/hacker_news.csv"))
