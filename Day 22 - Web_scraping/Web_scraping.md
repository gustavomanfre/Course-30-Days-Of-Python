📘 Día 22: Web Scraping en Python - Guía Completa
¿Qué es el Web Scraping?
Imagina que tienes una biblioteca gigantesca (Internet) llena de información valiosa, pero toda esa información está dispersa en miles de libros (sitios web). El web scraping es como tener un asistente robot que va a esos libros, lee la información que necesitas, y la organiza en un cuaderno (tu computadora o base de datos) para que puedas usarla fácilmente.
En términos técnicos: Web scraping es el proceso automatizado de extraer datos de sitios web y almacenarlos localmente en tu máquina o en una base de datos.

Preparación: Instalación de Herramientas
Antes de comenzar a "raspar" datos de sitios web, necesitas dos herramientas especiales:
bashpip install requests
pip install beautifulsoup4
Explicación de cada línea:

pip install requests: Instala el paquete requests, que es como un mensajero que va a internet y trae las páginas web que le pides.
pip install beautifulsoup4: Instala BeautifulSoup versión 4, que es como un traductor inteligente que convierte el código HTML (el lenguaje de las páginas web) en algo que Python puede entender y manipular fácilmente.

Nota importante: Para hacer web scraping efectivo, necesitas entender básicamente cómo funcionan las páginas web: HTML tags (etiquetas como <div>, <table>, <p>), clases CSS e IDs.

Ejemplo 1: Importando las Bibliotecas
pythonimport requests
from bs4 import BeautifulSoup
Explicación línea por línea:

import requests: Trae todo el paquete requests a tu programa. Este paquete te permite hacer solicitudes HTTP (pedir páginas web a internet).
from bs4 import BeautifulSoup: De la biblioteca bs4 (BeautifulSoup 4), importa específicamente la clase BeautifulSoup. Esta clase es la que usarás para analizar el HTML.

Analogía: Es como preparar tus herramientas antes de empezar un proyecto de carpintería. requests es tu martillo (para obtener cosas) y BeautifulSoup es tu sierra (para cortar y organizar esas cosas).

Ejemplo 2: Haciendo la Primera Solicitud Web
pythonimport requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful
```

**Explicación línea por línea:**

1. `url = 'https://archive.ics.uci.edu/ml/datasets.php'`: Creas una variable llamada `url` que almacena la dirección web del sitio que quieres "raspar". Es como escribir una dirección en un sobre.

2. `response = requests.get(url)`: Usas el método `get()` del paquete `requests` para solicitar la página web. Es como tocar el timbre de esa dirección y esperar que te abran la puerta. La respuesta completa se guarda en la variable `response`.

3. `status = response.status_code`: Extraes el código de estado de la respuesta. Este código te dice si la solicitud fue exitosa o si hubo algún problema.

4. `print(status)`: Imprime el código de estado en la consola.

**Salida esperada:**
```
200
¿Qué significa 200?
Los códigos de estado HTTP son como señales de tráfico en internet:

200: Todo está bien, la página se obtuvo correctamente
404: Página no encontrada
500: Error en el servidor
403: Acceso prohibido


Ejemplo 3: Parseando (Analizando) el Contenido con BeautifulSoup
pythonimport requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
```

**Explicación detallada línea por línea:**

1. **Primeras tres líneas**: Ya las conoces del ejemplo anterior.

2. `content = response.content`: Extraes el contenido HTML crudo (raw) de la respuesta. Es como abrir el sobre y sacar la carta completa.

3. `soup = BeautifulSoup(content, 'html.parser')`: 
   - Creas un objeto BeautifulSoup llamado `soup` (sopa, en inglés)
   - Le pasas el contenido HTML (`content`)
   - Le especificas qué parser (analizador) usar: `'html.parser'` es el analizador de Python incorporado
   - **Analogía**: Es como verter ingredientes crudos en una licuadora y convertirlos en algo manejable

4. `print(soup.title)`: Imprime la etiqueta `<title>` completa del HTML
   - Salida: `<title>UCI Machine Learning Repository: Data Sets</title>`

5. `print(soup.title.get_text())`: Imprime solo el texto dentro de la etiqueta title, sin las etiquetas HTML
   - Salida: `UCI Machine Learning Repository: Data Sets`

6. `print(soup.body)`: Imprime todo el contenido dentro de la etiqueta `<body>` (el cuerpo de la página web). Esto será MUCHO texto.

7. `print(response.status_code)`: Imprime nuevamente el código de estado (200)

8. `tables = soup.find_all('table', {'cellpadding':'3'})`:
   - **Método `find_all()`**: Busca TODAS las ocurrencias de algo
   - **Primer argumento `'table'`**: Busca todas las etiquetas `<table>`
   - **Segundo argumento `{'cellpadding':'3'}`**: Un filtro adicional - solo tablas que tengan el atributo `cellpadding="3"`
   - **Resultado**: Una lista de todas las tablas que cumplan estos criterios
   - **Analogía**: Es como decirle a alguien "tráeme todos los libros rojos que tengan más de 200 páginas"

9. `table = tables[0]`: 
   - Como `tables` es una lista, usas `[0]` para tomar el primer elemento
   - Ahora `table` contiene solo la primera tabla encontrada

10. `for td in table.find('tr').find_all('td'):`:
    - **`table.find('tr')`**: Encuentra la PRIMERA fila (`<tr>` = table row) dentro de la tabla
    - **`.find_all('td')`**: Encuentra TODAS las celdas (`<td>` = table data) dentro de esa fila
    - **`for td in ...`**: Itera (recorre) cada celda una por una
    - **Analogía**: Es como abrir el primer cajón de un archivero y revisar cada carpeta dentro de él

11. `print(td.text)`: 
    - Para cada celda `td`, imprime solo el texto (sin etiquetas HTML)
    - `.text` es una propiedad que extrae el contenido textual

---

## Conceptos Clave Resumidos

### 1. **Flujo de Trabajo del Web Scraping:**
```
Solicitar página (requests.get) 
    ↓
Recibir HTML crudo (response.content)
    ↓
Parsear HTML (BeautifulSoup)
    ↓
Buscar elementos específicos (find, find_all)
    ↓
Extraer datos (.text, .get_text())
2. Métodos importantes de BeautifulSoup:

find(): Encuentra el PRIMER elemento que coincida
find_all(): Encuentra TODOS los elementos que coincidan
.text o .get_text(): Extrae solo el texto, sin HTML

3. Formas de buscar elementos:

Por etiqueta HTML: soup.find('table')
Por clase CSS: soup.find('div', {'class': 'mi-clase'})
Por ID: soup.find('div', {'id': 'mi-id'})
Por atributos: soup.find('table', {'cellpadding': '3'})


Ejercicios Propuestos
El material termina sugiriendo tres ejercicios progresivamente más difíciles:
Ejercicio 1: Raspar datos de Boston University y guardarlos como JSON

Dificultad: Básica
Objetivo: Practicar extracción básica y conversión a JSON

Ejercicio 2: Extraer la tabla de datasets de UCI y convertirla a JSON

Dificultad: Media
Objetivo: Trabajar con tablas HTML y estructurar datos

Ejercicio 3: Raspar la tabla de presidentes de USA de Wikipedia

Dificultad: Avanzada
Advertencia: La tabla no está bien estructurada, tomará tiempo
Objetivo: Manejar HTML complejo y mal estructurado


Consideraciones Finales
Aspectos Éticos y Legales:

Siempre revisa los términos de servicio del sitio web
Respeta el archivo robots.txt (indica qué se puede raspar)
No sobrecargues servidores con demasiadas solicitudes
Algunos sitios prohíben explícitamente el web scraping

Mejores Prácticas:

Agrega delays entre solicitudes (time.sleep())
Maneja errores con try/except
Verifica que el scraping siga funcionando (los sitios cambian)
Considera usar APIs oficiales cuando estén disponibles

