#📚 Ejercicio 1: Romeo y Julieta (Frecuencia de palabras)
#Objetivo: Descargar un libro de internet, limpiarlo de signos de puntuación y contar qué palabras se repiten más.

# 1. IMPORTACIONES
import requests  # Librería para hacer "llamadas" a internet (como abrir una web con código).
import re        # Librería de "Expresiones Regulares" (para buscar patrones en texto).
from collections import Counter # Una herramienta especializada en contar elementos de una lista.

# 2. DEFINICIÓN DE LA FUNCIÓN
def contar_palabras_romeo():
    # Variable tipo string con la dirección web del archivo de texto.
    url = 'https://www.gutenberg.org/files/1112/1112.txt'
    
    # requests.get(url): Va a la dirección web y descarga el contenido.
    # .text: Extrae solo el contenido de texto de la respuesta (ignora encabezados técnicos). Devuelve un <class 'str'>
    texto_bruto = requests.get(url).text
    
    # .lower(): Convierte TODO el texto a minúsculas.
    # Hacemos esto para que "Romeo" y "romeo" cuenten como la misma palabra.
    texto_limpio = texto_bruto.lower()
    
    # re.findall(patrón, texto): Busca todas las coincidencias del patrón en el texto.
    # r'\b[a-z]+\b': Es el patrón mágico.
    #   \b: Inicio de palabra.
    #   [a-z]: Solo letras de la a a la z (ignora números y puntos).
    #   +: Una o más letras juntas.
    #   \b: Fin de palabra.
    # Resultado: Una lista gigante de palabras sueltas ['the', 'tragedy', 'of', 'romeo'...]
    lista_palabras = re.findall(r'\b[a-z]+\b', texto_limpio)
    
    # Counter(lista): Recorre la lista y crea un diccionario contando repeticiones.
    # Ejemplo interno: {'the': 1500, 'romeo': 300, ...}
    contador = Counter(lista_palabras)
    
    # .most_common(10): Devuelve las 10 palabras con el número más alto.
    top_10 = contador.most_common(10)
    
    return top_10

# 3. EJECUCIÓN
# Llamamos a la función e imprimimos el resultado.
print("Las 10 palabras más frecuentes en Romeo y Julieta son:")
print(contar_palabras_romeo())

#🐈 Ejercicio 2: API de Gatos (Estadísticas)
#Objetivo: Convertir datos de texto (ej: "3 - 5 kgs") en números reales para calcular promedios.

import requests    # Para descargar los datos de la API.
import statistics  # Librería matemática para calcular media, mediana y desviación estándar.

def estadisticas_gatos():
    url = 'https://api.thecatapi.com/v1/breeds'
    
    # .json(): Convierte la respuesta de texto (formato JSON) en una lista de diccionarios de Python.
    # Ahora 'lista_gatos' es una lista donde cada elemento es un diccionario con datos de una raza.
    lista_gatos = requests.get(url).json() # Devuelve un <class 'list'> o una lista de diccionarios.
    # Ejemplo del contenido de lista_gatos[0]:
    # {
    #   'weight': {'imperial': '7 - 10', 'metric': '3 - 5'},
    #   'life_span': '12 - 15',
    #   'name': 'Abyssinian',
    #   ...
    # } 
    
    # Listas vacías donde iremos guardando los números limpios para calcular después.
    pesos_metricos = []
    vidas_anios = []

    # Bucle 'for': Recorre cada raza de gato en la lista descargada.
    for gato in lista_gatos:
        # --- PROCESAMIENTO DEL PESO ---
        # Accedemos al diccionario 'weight' y luego a la clave 'metric'.
        # El valor es un texto tipo "3 - 5".
        # gato es un diccionario con datos de UNA raza específica.
        # Un ejemplo de un gato seria: {'weight': {'imperial': '7 - 10', 'metric': '3 - 5'}, life_span': '12 - 15', ...}
        #Entonces lista_gatos es una lista de esos diccionarios.
        #Denttro weight hay otro diccionario con imperial y metric. Para acceder a metric hacemos gato['weight']['metric']
        texto_peso = gato['weight']['metric']
        
        # .split(' - '): Corta el texto donde haya un guion.
        # Convierte "3 - 5" en una lista ["3", "5"].
        partes_peso = texto_peso.split(' - ')
        
        # float(): Convierte el texto "3" en el número decimal 3.0.
        # Calculamos el promedio entre el mínimo y máximo de ESE gato específico.
        # (3 + 5) / 2 = 4.0
        # Usamos [-1] y [0] por seguridad (por si solo viene un número).
        peso_promedio_raza = (float(partes_peso[0]) + float(partes_peso[-1])) / 2
        
        # .append(): Agrega este número a nuestra lista general de pesos.
        pesos_metricos.append(peso_promedio_raza)

        # --- PROCESAMIENTO DE VIDA ÚTIL ---
        # El dato 'life_span' viene como "12 - 15". Hacemos lo mismo.
        texto_vida = gato['life_span']
        partes_vida = texto_vida.split(' - ')
        
        # Calculamos promedio de vida para esta raza.
        vida_promedio_raza = (float(partes_vida[0]) + float(partes_vida[-1])) / 2
        vidas_anios.append(vida_promedio_raza)

    # Función auxiliar para imprimir bonito (evita repetir print 10 veces).
    def mostrar_datos(nombre_dato, lista_datos):
        print(f"\n--- Estadísticas de {nombre_dato} ---")
        print(f"Mínimo: {min(lista_datos)}") # min(): Busca el valor más pequeño.
        print(f"Máximo: {max(lista_datos)}") # max(): Busca el valor más grande.
        print(f"Media:  {statistics.mean(lista_datos):.2f}") # mean(): Promedio aritmético.
        print(f"Mediana:{statistics.median(lista_datos)}")   # median(): El valor justo en el medio.
        print(f"Desviación Estándar: {statistics.stdev(lista_datos):.2f}") # stdev(): Qué tanto varían los datos.

    # Llamamos a la función auxiliar con nuestras listas llenas.
    mostrar_datos("Peso (kg)", pesos_metricos)
    mostrar_datos("Vida (años)", vidas_anios)

# Ejecutamos la función principal
estadisticas_gatos()


#🌍 Ejercicio 3: API de Países (Ordenamiento y Conteo)

#Objetivo: Ordenar una lista de diccionarios (países) y extraer datos anidados (idiomas).

import requests
from collections import Counter

def analizar_paises():
    # URL de la API de países.
    url = 'https://restcountries.com/v2/all'
    paises = requests.get(url).json() # Descargamos y convertimos a lista de Python.
    # Paises es una lista donde cada elemento es un diccionario con datos de un país.
    #Un ejemplo de la lista de diccionarios:
    #[
    #  {
    #    'name': 'Afghanistan',
    #    'area': 652230,
    #    'languages': [{'name': 'Pashto'}, {'name': 'Uzbek  '}, {'name': 'Turkmen'}],
    #    ...
    #  },....

    # --- PARTE A: 10 PAÍSES MÁS GRANDES ---
    
    # Paso 1: Filtrar.
    # Creamos una lista nueva solo con los países que tienen la clave 'area'.
    # Algunos países pequeños o nuevos pueden no tener ese dato y romperían el código.
    #Aplicamos "list comprehension" para filtrar.
    #Una lista por comprensión tiene el siguiente formato:
        #[expresión for item in iterable if condición]
    #paises es una lista de diccionarios. Cada pais es un diccionario.
    #Si cada pais tiene la clave 'area', lo incluimos en la nueva lista.
    # Cada 'pais' se evalúa individualmente.
    # Si el diccionario tiene la clave 'area', se incluye en la nueva lista.
    paises_con_area = [pais for pais in paises if 'area' in pais]
    #paises_con_area contiene solo los países que tienen el dato 'area'.
    #Ejemplo: [{'name': 'Afghanistan', 'area': 652230, ...}, {'name': 'Albania', 'area': 28748, ...}, ...]
    
    # Paso 2: Ordenar (sorted).
    # key=lambda p: p['area']: Le dice a Python "Ordena basándote en el valor de 'area'".
    # reverse=True: Ordena de Mayor a Menor.
    # [:10]: "Slicing". Toma solo los primeros 10 elementos de la lista ordenada.
    
    # sorted(): tiene el siguiente formato: sorted(iterable, key=función, reverse=bool)
    # iterable: es la lista que queremos ordenar.
    # funcion es una lambda con el siguiente formato: lambda parámetro: expresión
    # La función lambda NO recorre la lista.
    # sorted() recorre internamente la lista y le pasa cada elemento a la lambda.
    # Una funcion lambda funciona:
        # Parametro p: recibe un diccionario en el paraámetro p
        # La expresión p['area'] devuelve un número (el área del país).
        # Ese número se usa SOLO como criterio de comparación para ordenar.
        # El resultado final sigue siendo una lista de diccionarios completos.
        #Ejemplo: De lo que recibe top_10_grandes es una lista de diccionarios ordenados por area. Ejemplo: [{'name': 'Russia', 'area': 17098242, ...}, {'name': 'Canada', 'area': 9984670, ...}, ...]
        # reverse=True hace que el orden sea de mayor a menor.
    top_10_grandes = sorted(paises_con_area, key=lambda p: p['area'], reverse=True)[:10]

    print("\n--- Los 10 países más grandes ---")
    for pais in top_10_grandes:
        # Imprimimos nombre y área formateada.
        print(f"{pais['name']}: {pais['area']} km²")

    # --- PARTE B: IDIOMAS MÁS HABLADOS ---

    lista_todos_idiomas = []
    
    # Recorremos cada país de la lista original.
    for pais in paises:
        # Verificamos si el diccionario país tiene la clave 'languages'. Si tiene, procedemos.
        if 'languages' in pais: 
            # 'pais['languages']' es una lista de diccionarios: [{'name': 'Spanish'}, {'name': 'Guaraní'}]  idioma recibe un diccionario a la vez {'name': 'Spanish'}, {'name': 'Guaraní'}....
            for idioma in pais['languages']:
                #Agregamos a lista_todos_idiomas el nombre del idioma actual. Entonces lista_todos_idiomas es una lista con "Spanish", "English", etc.
                lista_todos_idiomas.append(idioma['name'])
    #Counter(lista): Cuenta cuántas veces aparece cada elemento en la lista.
    # Usamos Counter de nuevo para contar cuántas veces aparece "Spanish", "English", etc.
    #Counter devuelve un diccionario especial donde las claves son los idiomas y los valores son las cantidades.
    contador_idiomas = Counter(lista_todos_idiomas)
    
    print("\n--- Los 10 idiomas más frecuentes ---")
    # Imprimimos los 10 más comunes.
    # most_common(10): Devuelve una lista con las claves y valores de los 10 elementos con mayor valor en el contador.
    # Devuelve una lista de tuplas
    # Cada tupla es (idioma, cantidad)
    print(contador_idiomas.most_common(10))
    
    # --- PARTE C: TOTAL DE IDIOMAS ---
    # len(contador_idiomas): Cuenta cuántas claves ÚNICAS hay en el contador.
    print(f"\nNúmero total de idiomas únicos en la API: {len(contador_idiomas)}")

analizar_paises()

# 🕷️ Ejercicio 4: Web Scraping (UCI Datasets)
# Objetivo:
# Leer una página web que NO es una API (es HTML pensado para humanos)
# y extraer información específica utilizando BeautifulSoup.

import requests                      # Librería para hacer peticiones HTTP (GET, POST, etc.)
from bs4 import BeautifulSoup        # Herramienta para analizar (parsear) HTML y XML


def raspar_uci():
    """
    Esta función:
    1) Descarga el HTML de la página del repositorio UCI
    2) Lo analiza con BeautifulSoup
    3) Busca los títulos de los datasets
    4) Imprime los primeros 20 encontrados
    """

    # URL del repositorio de Machine Learning de UCI.
    # Esta página devuelve HTML, NO JSON.
    url = 'https://archive.ics.uci.edu/datasets'
    
    # Hacemos una petición HTTP GET a la URL.
    # response es un objeto Response que contiene:
    # - status_code (200, 404, etc.)
    # - headers
    # - contenido de la página
    response = requests.get(url)

    # response.content contiene el cuerpo de la respuesta en formato binario (bytes).
    # BeautifulSoup puede trabajar directamente con este contenido.
    # Si quisiéramos texto plano, usaríamos response.text
    # Pero para HTML es mejor usar .content
    #content es un <class 'bytes'>
    content = response.content
    
    # Creamos el objeto BeautifulSoup (la "sopa"). beautifulSoup es una herramienta para analizar HTML.
    #beautifulSoup es una herramienta para analizar HTML. Proviene de la librería bs4.
    # bs4 no viene instalada por defecto con Python.
    # Se instala con: pip install beautifulsoup4
    # Parámetros:
    # - content: El HTML crudo descargado de la web.
    # - 'html.parser': El motor que usará para interpretar el HTML.
    # BeautifulSoup:
    # - Toma el HTML crudo
    # - Lo convierte en un árbol de nodos (DOM)
    # - Permite buscar etiquetas, atributos y texto fácilmente
    #
    # 'html.parser' es el motor interno de Python para interpretar HTML.
    soup = BeautifulSoup(content, 'html.parser')
    
    # soup.find_all('h2'):
    # - Busca TODAS las etiquetas <h2> en el documento HTML, Solo las etiquetas <h2> no busca clases ni ids.
    # - Devuelve una lista de objetos h2 Tag de BeautifulSoup.
    #Devuelve una lista de objetos Tag
    #Cada Tag representa una etiqueta <h2> del HTML
    #Incluye:
        #la etiqueta <h2>
        #su texto interno
        #cualquier etiqueta anidada dentro (si existiera)
        #atributos (class, id, etc.)
    #
    # En la página actual de UCI, muchos nombres de datasets
    # están dentro de etiquetas <h2>.
    #nombres_datasets es una lista de objetos Tag h2
    nombres_datasets = soup.find_all('h2')
    
    print("\n--- Datasets encontrados en UCI (Scraping) ---")
    
    # Recorremos solo los primeros 20 elementos tag h2 de la lista.
    # [:20] es slicing de listas y evita imprimir demasiados resultados.
    for titulo in nombres_datasets[:20]:
        
        # titulo es un objeto Tag de BeautifulSoup que representa:
        # <h2>Nombre del dataset</h2>
        #
        # titulo.text:
        # - Extrae solo el texto interno de la etiqueta
        #
        # .strip():
        # - Elimina espacios en blanco y saltos de línea al inicio y al final
        # 
        print(f"Dataset: {titulo.text.strip()}")


# NOTA IMPORTANTE:
# El Web Scraping es FRÁGIL.
# Si el sitio web cambia su estructura HTML
# (por ejemplo, reemplaza <h2> por <h3> o <div>),
# este código dejará de funcionar correctamente.
# Esto es normal en scraping.
raspar_uci()
