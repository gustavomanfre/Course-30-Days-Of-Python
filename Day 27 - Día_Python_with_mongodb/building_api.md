# Análisis completo de MONGODB_URI
Vamos a desglosar completamente qué es MONGODB_URI, qué tipo de dato es, qué contiene, y cómo funciona cada parte de la cadena de conexión.

# MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority' 

1️⃣ ¿Qué recibe MONGODB_URI?
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'

Tipo de dato que recibe:
MONGODB_URI recibe un string (cadena de texto)

¿Valor o referencia?
MONGODB_URI recibe un VALOR (una copia del string)

¿Qué es?
Es una cadena de conexión (connection string) que contiene toda la información necesaria para conectarse a una base de datos MongoDB. 

●  MONGODB_URI: Es la cadena de conexión a MongoDB Atlas (MongoDB en la nube) es un string. 
●  Contiene: usuario, contraseña, dirección del servidor y opciones de conexión.

# Codigo

MONGODB_URI = 'mongodb+srv://user:pass@host.com/db'

print(type(MONGODB_URI))
# <class 'str'>

print(isinstance(MONGODB_URI, str))
# True

print(len(MONGODB_URI))
# 42 (número de caracteres)

# Es un VALOR, no una referencia
otra_variable = MONGODB_URI
otra_variable = "cambio"
print(MONGODB_URI)  
# 'mongodb+srv://user:pass@host.com/db' (no cambió)
---------------------------------------------------------------------------------------------------------------------------

## 2️⃣ Estructura de la cadena de conexión
Vamos a descomponer la cadena completa parte por parte:

mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority

### Diagrama visual:

┌─────────┬──────────────────────────┬────────────────────────────────────┬──────┬─────────────────────────────┐
│ Esquema │   Autenticación          │              Host                  │  DB  │    Opciones                 │
└─────────┴──────────────────────────┴────────────────────────────────────┴──────┴─────────────────────────────┘
  mongodb+srv://  asabeneh:your_password  @  30daysofpython-twxkr.mongodb.net  /test  ?retryWrites=true&w=majority
      ↓                    ↓                              ↓                      ↓                ↓
   Protocolo          Usuario:Contraseña              Servidor              Base de datos    Parámetros

------------------------------------------------------------------------------------------------------------------------------
## 3️⃣ Desglose detallado de cada componente

### PARTE 1: Esquema/Protocolo
    mongodb+srv://

Elemento        Significado
mongodb         Protocolo de MongoDB
+srv            Usa DNS SRV records (opcional, pero recomendado para MongoDB Atlas)
://             Separador estándar de URLs

¿Qué hace +srv?
Sin +srv: mongodb:// → Debes especificar host:puerto manualmente
Con +srv: mongodb+srv:// → MongoDB resuelve automáticamente los servidores disponibles mediante DNS
______________

### PARTE 2: Autenticación
    asabeneh:your_password@

| Elemento        | Significado      |
|-----------------|------------------|
|asabeneh       | Nombre de usuario|
| :             | Separador        |
| your_password | Contraseña del usuario |
| @             | Separador que indica "fin de credenciales, inicio de host" |

Estructura:
    usuario:contraseña@

## Ejemplo real:
    Usuario: admin
    Contraseña: SecurePass123!
MONGODB_URI = 'mongodb+srv://admin:SecurePass123!@...'
______________

### PARTE 3: Host/Servidor

    30daysofpython-twxkr.mongodb.net

| Elemento               | Significado                         |
|------------------------|-------------------------------------|
| 30daysofpython-twxkr | Nombre del cluster en MongoDB Atlas |
| .mongodb.net         | Dominio de MongoDB Atlas            |

Estructura general:

[nombre-cluster].[proveedor].[dominio]

client recibe un objeto de tipo MongoClient
Recibe una referencia (o puntero) a un objeto MongoClient. Este objeto representa la conexión activa con el servidor de MongoDB.

## Ejemplos:

# MongoDB Atlas
'cluster0.abc123.mongodb.net'

# MongoDB local
'localhost'  # o '127.0.0.1'

# MongoDB en servidor propio
'mi-servidor.com'

# Múltiples servidores (sin SRV)
'host1.com:27017,host2.com:27017,host3.com:27017'

## Puerto por defecto:
Con mongodb+srv://: No necesitas especificar puerto (se resuelve automáticamente)
Con mongodb://: Puerto por defecto es 27017
# Especificar puerto manualmente
MONGODB_URI = 'mongodb://localhost:27017/mydb'


### PARTE 4: Base de datos

/test
Elemento        Significado
/               Separador
test            Nombre de la base de datos por defecto

Importante:
Esta es la base de datos por defecto a la que te conectas
Puedes acceder a otras bases de datos después:

client = pymongo.MongoClient(MONGODB_URI)

# Se conecta a 'test' por defecto

# Pero puedes acceder a otras
db_test = client['test']  # La que está en la URI
db_otro = client['otra_base_de_datos']  # Otra diferente
db_produccion = client['produccion']  # Otra más

### PARTE 5: Opciones/Parámetros

?retryWrites=true&w=majority

| Elemento           | Significado                                     |
|--------------------|-------------------------------------------------|
| ?                | Inicio de parámetros (query string)             |
| retryWrites=true | Reintentar escrituras automáticamente si fallan |
| &                | Separador entre parámetros                      |
| w=majority       | Write concern: esperar confirmación de la mayoría de réplicas |

Estructura:

?parametro1=valor1&parametro2=valor2&parametro3=valor3

5️⃣ Desglose de las opciones del ejemplo

MONGODB_URI = '...?retryWrites=true&w=majority'

retryWrites=true

# ¿Qué significa?
# Si una operación de escritura falla (insert, update, delete)
# MongoDB intentará automáticamente ejecutarla de nuevo

# Ejemplo de escenario:
# 1. Tu app intenta insertar un documento
# 2. Hay un problema de red momentáneo
# 3. Con retryWrites=true: MongoDB reintenta automáticamente
# 4. Sin retryWrites: La operación falla y debes manejarla tú

Valores posibles:
true: Activa reintentos automáticos
false: No reintenta (por defecto en versiones antiguas)


w=majority

# ¿Qué significa?
# Es el "write concern" - nivel de confirmación de escritura

Write Concern (w):

| Valor | Significado |
|-------|-------------|
| w=0 | "Fire and forget" - No espera confirmación |
| w=1 | Espera confirmación del servidor primario solamente |
| w=majority | Espera confirmación de la mayoría de los servidores réplica |
| w=all | Espera confirmación de TODOS los servidores |

Diagrama visual:

w=0 (No espera)
Cliente → [Servidor Primario]
         ✓ Inmediato
         (No sabe si realmente se guardó)

w=1 (Espera al primario)
Cliente → [Servidor Primario] → ✓
         (Sabe que se guardó en 1 servidor)

w=majority (Espera a la mayoría)
Cliente → [Servidor Primario] → ✓
         ↓
         [Réplica 1] → ✓
         ↓
         [Réplica 2] → ✓
         (Sabe que se guardó en la mayoría)

____________________________

1️⃣ ¿Qué recibe client?

# client = pymongo.MongoClient(MONGODB_URI)

Tipo de dato que recibe:
client recibe un objeto de tipo MongoClient

¿Valor o referencia?
client recibe una referencia a un objeto. 
No recibe datos de la base de datos, sino un conector/gestor de conexión.

¿Qué es realmente este objeto?
Piensa en client como un teléfono 📞:
    ● No es la persona con la que quieres hablar
    ● Es el dispositivo que te permite comunicarte con esa persona
    ● Cuando lo "levantas" (lo creas), estableces la posibilidad de hacer llamadas

En términos técnicos:
    client = pymongo.MongoClient(MONGODB_URI)

Lo que sucede aquí:
    ● Python crea una instancia de la clase MongoClient
    ● Esta instancia establece una conexión con el servidor MongoDB
    ● client guarda la referencia a ese objeto conexión
    ● NO descarga ningún dato todavía

¿Qué contiene realmente client? Si imprimes client:

print(client)
# MongoClient(host=['cluster.mongodb.net:27017'], ...)

print(type(client))
# <class 'pymongo.mongo_client.MongoClient'>

Contiene:
    ● La información de conexión (host, puerto, credenciales)
    ● Un pool de conexiones (para manejar múltiples peticiones)
    ● Métodos para interactuar con el servidor
    ● NO contiene datos de tu base de datos

1. Es una conexión "Lazy" (Perezosa)
Cuando ejecutas client = pymongo.MongoClient(MONGODB_URI), PyMongo simplemente crea un objeto en la memoria de tu computadora.
    -Este objeto guarda la dirección (URI), el usuario y la contraseña.
    -Prepara el Connection Pool (el grupo de conexiones que usará después).
    -Pero no abre el túnel de red todavía.

2. ¿Cuándo ocurre la conexión real?
La conexión se establece de forma automática la primera vez que intentas hacer algo real con la base de datos. Por ejemplo:
    -Cuando haces un db.coleccion.find_one().
    -Cuando intentas insertar un documento.
    -Cuando pides una lista de las bases de datos.

En ese momento, PyMongo dice: "Ah, el usuario quiere datos de verdad, ahora sí voy a usar las credenciales que me diste antes para abrir el túnel".

3. ¿Por qué lo hace así?
Lo hace por eficiencia y robustez:

    -Velocidad de arranque: Tu aplicación de Flask inicia instantáneamente porque no tiene que esperar a que el servidor de MongoDB (que puede estar en otro país) responda.
    -Resiliencia: Si el servidor de MongoDB se cae y vuelve a subir, el objeto client sigue siendo válido. Él simplemente intentará reconectarse en la próxima consulta.

4. ¿Cómo puedo "forzar" la conexión para saber si funciona?
Si quieres que tu programa verifique la conexión en ese mismo instante (por ejemplo, para que el código se detenga si la contraseña está mal), puedes usar este truco:


client = pymongo.MongoClient(MONGODB_URI)

try:
    # El comando 'ping' obliga al cliente a conectarse realmente
    client.admin.command('ping')
    print("¡Conexión exitosa al servidor!")
except Exception as e:
    print("Error: No se pudo conectar al servidor", e)

En resumen: MongoClient es como tener el número de teléfono guardado en la agenda y el cable listo, pero todavía no has apretado el botón de "Llamar". La llamada ocurre recién cuando pides los datos.

_______________________________________________________________________________________________________________

2️⃣ ¿Qué recibe db?

# db = client['thirty_days_of_python']

Tipo de dato que recibe:
db recibe un objeto de tipo Database

¿Valor o referencia?
db recibe una referencia a un objeto. Tampoco descarga datos, es solo otra capa de gestión.

¿Qué es realmente este objeto?
Siguiendo la analogía del teléfono:

client = el teléfono 📞
db = la extensión específica que marcas dentro de una empresa 🏢

En términos técnicos:
db = client['thirty_days_of_python']

Lo que sucede aquí:
    1. client['thirty_days_of_python'] es como decir: "Quiero hablar con el departamento 'thirty_days_of_python'"
    2. PyMongo crea un objeto Database que representa esa base de datos
    3. db guarda la referencia a ese objeto
    TODAVÍA no se descarga ningún dato

Analogía completa:
# client = El teléfono conectado a MongoDB S.A.
client = pymongo.MongoClient(MONGODB_URI)

# db = Marcas la extensión del departamento "thirty_days_of_python"
db = client['thirty_days_of_python']

# Aún no has pedido nada, solo estás en la línea correcta

¿Qué contiene realmente db?
print(db)
# Database(MongoClient(...), 'thirty_days_of_python')

print(type(db))
# <class 'pymongo.database.Database'>

Contiene:
    1. Una referencia al client (el teléfono)
    2. El nombre de la base de datos ('thirty_days_of_python')
    3. Métodos para acceder a colecciones
    4. NO contiene los datos de tu base de datos

En ese paso todavía estás en terreno "perezoso" (lazy).

1. La lógica de la "Ruta"
Escribir db = client['thirty_days_of_python'] es como definir una ruta o un camino.

    Línea 1 (client): Creas el mapa y guardas la dirección del servidor.
    Línea 2 (db): Dibujas una flecha en el mapa que apunta a una habitación específica (la base de datos).

Python simplemente crea un nuevo objeto en su memoria que dice: "Si algún día este usuario me pide algo, ya sé que debo usar este 'client' y buscar en esta 'db'". Pero todavía no ha enviado ni un solo bit a través de internet.

2. ¿Cuándo se "despierta" el túnel de red?
La conexión real (el handshake de red) ocurre únicamente cuando ejecutas un comando que obliga a MongoDB a responder.

Ejemplos de cuándo SÍ ocurre la conexión:

    db.list_collection_names() (Porque tiene que ir a mirar qué hay).
    db.users.find_one() (Porque tiene que buscar un dato).
    db.users.insert_one({'name': 'Gustavo'}) (Porque tiene que escribir algo).

3️⃣ Ejemplo completo: ¿Cuándo se descargan los datos?
# PASO 1: Conexión (no hay datos aún)
client = pymongo.MongoClient(MONGODB_URI)
# client = referencia al gestor de conexión

# PASO 2: Selección de base de datos (no hay datos aún)
db = client['thirty_days_of_python']
# db = referencia al objeto Database

# PASO 3: Selección de colección (no hay datos aún)
students_collection = db.students
# students_collection = referencia al objeto Collection

# PASO 4: Consulta - AQUÍ sí se descargan datos 🎯
students = students_collection.find()
# Ahora sí, MongoDB envía los datos a Python

# PASO 5: Iteración - Se procesan los datos
for student in students:
    print(student['name'])  # Aquí usas los datos reales

## 4️⃣ Diagrama visual del flujo

MONGODB_URI (string de conexión)
        ↓
pymongo.MongoClient() crea el objeto
        ↓
client ──────────→ [REFERENCIA] → Objeto MongoClient
                                   ├─ host info
                                   ├─ connection pool
                                   └─ métodos
        ↓
client['thirty_days_of_python']
        ↓
db ───────────────→ [REFERENCIA] → Objeto Database
                                   ├─ referencia a client
                                   ├─ nombre: 'thirty_days_of_python'
                                   └─ métodos
        ↓
db.students  o  db['students']
        ↓
collection ───────→ [REFERENCIA] → Objeto Collection
                                   ├─ referencia a db
                                   ├─ nombre: 'students'
                                   └─ métodos
        ↓
collection.find() ← AQUÍ se hace la petición real
        ↓
cursor ───────────→ [REFERENCIA] → Cursor (iterador)
        ↓                          (los datos se cargan bajo demanda)
for doc in cursor:
    print(doc)    ← AQUÍ se procesan los datos reales

5️⃣ Comparación con una analogía del mundo real

Imagina que quieres pedir comida:

# 1. Abres la app de delivery (conexión)
client = pymongo.MongoClient(MONGODB_URI)
# → Tienes la app abierta, pero no has pedido nada

# 2. Seleccionas un restaurante
db = client['thirty_days_of_python']
# → Entraste al menú del restaurante, pero no has pedido nada

# 3. Seleccionas una categoría del menú
collection = db.students
# → Estás viendo "Hamburguesas", pero no has pedido nada

# 4. Haces el pedido
students = collection.find()
# → AHORA sí, el restaurante prepara tu comida

# 5. Comes
for student in students:
    print(student)
# → Consumes lo que pediste

6️⃣ Entonces, ¿por qué usar referencias?

Ventaja 1: Lazy Loading (Carga perezosa)
db = client['thirty_days_of_python']
# Si tu base de datos pesa 10GB, no hay problema
# Solo estás "apuntando" a ella, no la estás descargando

Ventaja 2: Eficiencia
# Puedes crear múltiples referencias sin costo
students = db.students
teachers = db.teachers
courses = db.courses
# Ninguna de estas líneas descarga datos

Ventaja 3: Control
# Tú decides CUÁNDO y QUÉ datos traer
all_students = db.students.find()  # Trae todos
one_student = db.students.find_one({'name': 'Asabeneh'})  # Solo uno

_______________________________________________________________________________________________________________

# DECORADORES (IR A decoradores.md)

_______________________________________________________________________________________________________________

# Metodos del Modulo json
def students ():
    return Response(json.dumps(student), mimetype='application/json')

-json.dumps(student): Convierte la lista de Python a una cadena JSON

-mimetype='application/json': Le dice al navegador que estamos enviando datos en formato JSON

-Response(): Crea un objeto de respuesta HTTP
_______________________________________________________________________________________________________________

from bson.objectid import ObjectId
MongoDB usa ObjectId como identificador único para cada document

from bson.json_util import dumps
Una versión especializada de dumps que maneja tipos de datos específicos de MongoD
_______________________________________________________________________________________________________________

@app.route('/api/v1.0/students/<id>', methods = ['GET']) 
●  <id>': Es un parámetro variable en la URL. Por ejemplo: /api/v1.0/students/12345 
●  def single_student(id): La función recibe el ID como parámetro
_______________________________________________________________________________________________________________

 student = db.students.find({'_id':ObjectId(id)}) 
    return Response(dumps(student), mimetype='application/json') 

●  db.students.find(): Busca en la colección "students" 
●  {'_id':ObjectId(id)}: Filtra por el campo _id que coincida con el ID proporcionado 

●  ObjectId(id): Convierte el string del ID a un objeto ObjectId que MongoDB entiende 
●  dumps(student): Convierte el resultado (incluyendo tipos especiales de MongoDB) a JSON.

La razón técnica por la cual se utiliza {'_id': ObjectId(id)} y no simplemente {'_id': id} radica en la incompatibilidad de tipos de datos. MongoDB es estricto con los tipos para garantizar la integridad y evitar errores silenciosos.

1. Diferencia de Naturaleza de los Datos
    El String (id): En tu código Python, la variable id suele ser una cadena de texto (str) de 24 caracteres hexadecimales (por ejemplo, '5df68a23...').
    El ObjectId: En la base de datos, el campo _id no se guarda como texto, sino como un objeto binario de 12 bytes. Técnicamente, un string no es igual a un ObjectId, aunque visualmente parezcan iguales. Las fuentes enfatizan que son tipos de datos diferentes e incompatibles.

2. Por qué falla la búsqueda con un String
Si intentas buscar usando {'_id': id} (el string), MongoDB buscará una coincidencia exacta de tipo "texto" en el índice. Como el valor almacenado es de tipo "binario" (ObjectId), la comparación resultará falsa y la consulta devolverá None o ningún resultado, aunque los caracteres coincidan.

Las fuentes utilizan una analogía clara: es como buscar el número entero 25 pero pasando como criterio el texto "25"; para el sistema, no son el mismo valor.

3. La función de ObjectId(id)
Al envolver la variable en ObjectId(), estás realizando una conversión explícita:
    Transformas esos 24 caracteres hexadecimales legibles en su representación binaria real de 12 bytes.
    Esto permite que PyMongo serialice la consulta a BSON de forma correcta, enviando a MongoDB el formato exacto que este espera encontrar en su índice de disco.

4. Razón de diseño de MongoDB
MongoDB no realiza esta conversión automáticamente por seguridad. Si permitiera conversiones automáticas, el sistema se volvería caótico al intentar adivinar si el usuario quiere buscar un string, un número o un identificador de objeto, lo que podría llevar a errores graves en aplicaciones complejas.
En resumen: Usamos ObjectId(id) porque es la única forma de "hablar el mismo idioma" que la base de datos, convirtiendo una referencia textual de Python en el objeto binario real que MongoDB utiliza como clave primaria

1. La regla de oro: El tipo de dato debe coincidir
Tal como sospechas, MongoDB es estricto con los tipos de datos.

    Si guardaste un Entero: Debes buscar con int(150). Si buscas con el string '150', MongoDB no lo encontrará porque para el motor son valores distintos.
    Si usas el _id por defecto: MongoDB genera automáticamente un ObjectId, que es un objeto binario de 12 bytes. Por lo tanto, buscar con el string '5df6...' devolverá None (nada), porque un String no es igual a un objeto binario.

2. ¿Qué hace exactamente ObjectId()?
La función ObjectId(id_string) actúa como un conversor de formato.

    Toma la representación legible (el string hexadecimal que tú ves) y la empaqueta en los 12 bytes binarios reales que están grabados en el disco duro.
    Sin esta conversión, PyMongo enviaría a la base de datos una consulta de tipo "texto", pero el índice de la base de datos está esperando un tipo "binario", por lo que la comparación falla.

3. La restricción técnica del valor (El caso del '150')
Aquí hay un detalle vital: para que la función ObjectId() funcione, el string que le pases debe ser obligatoriamente una cadena de 24 caracteres hexadecimales.

    Si intentas hacer ObjectId('150'): El código te dará un error, porque '150' es muy corto y no cumple con la anatomía de un ObjectId (4 bytes de tiempo + 5 bytes aleatorios + 3 bytes de contador).
    Si tu ID es realmente '150': Significa que tú (o el sistema) lo insertaste manualmente como un string o un número. En ese caso, no debes usar ObjectId(), sino buscarlo exactamente como se guardó: db.students.find_one({'_id': '150'}) o int(150).

Resumen técnico: La respuesta es SÍ. Siempre que trabajes con los identificadores automáticos de MongoDB, debes pasar el string por ObjectId() para convertirlo al "serial binario" que el motor entiende. Si no haces esa conversión, la base de datos te dirá que el documento no existe, aunque los caracteres del ID parezcan iguales a simple vista
_______________________________________________________________________________________________________________

from datetime import datetime 
●  Importamos datetime para registrar cuándo se creó el estudiante python 

@app.route('/api/v1.0/students', methods = ['POST']) 
def create_student (): 
●  Misma ruta que GET, pero ahora acepta método POST 
●  POST se usa para crear nuevos recursos 
    name = request.form['name'] 
    country = request.form['country'] 
    city = request.form['city'] 
    skills = request.form['skills'].split(', ') 
    bio = request.form['bio'] 
    birthyear = request.form['birthyear'] 

●  request.form['name']: Obtiene el valor del campo 'name' del formulario enviado 

●  .split(', '): Convierte la cadena de habilidades en una lista (por ejemplo: 
"Python, Java" → ['Python', 'Java']) 

●  Hacemos esto para cada campo que el usuario envía 
 
   created_at = datetime.now() 

●  Obtiene la fecha y hora actual 
 
   student = { 
        'name': name, 
        'country': country, 
        'city': city, 
        'birthyear': birthyear, 
        'skills': skills, 
        'bio': bio, 
        'created_at': created_at 
    } 

●  Creamos un diccionario con todos los datos del estudiante 

●  Este diccionario se convertirá en un documento de MongoDB 
   db.students.insert_one(student) 
    return ; 
●  insert_one(): Inserta el nuevo estudiante en la base de datos 
●  return: Debería retornar una respuesta (el código está incompleto aquí)

1. ¿Qué es request?
Técnicamente, request es un objeto global proporcionado por el framework Flask que contiene toda la información de la petición HTTP que el cliente (usuario) envía al servidor.

    Cuando un usuario completa un formulario y presiona "Enviar", toda esa información viaja empaquetada. Flask intercepta ese paquete y lo pone a tu disposición dentro del objeto request.

2. El atributo form
Efectivamente, como sospechabas, el objeto request tiene un atributo llamado form.
    Tipo de dato: Técnicamente es un objeto similar a un Diccionario de Python (específicamente un MultiDict).
    Contenido: Este "diccionario" contiene los pares clave-valor de los datos enviados.
        La llave (key) es el nombre (name) que tiene el campo en el HTML (por ejemplo: name="skills").
        El valor (value) es lo que el usuario escribió físicamente en la caja de texto.

3. Análisis del ejemplo: request.form['skills'].split(', ')
En esta línea ocurren varios pasos técnicos:
    Extracción: request.form['skills'] busca en el diccionario de la petición el valor asociado a la llave 'skills'. Supongamos que el usuario escribió el texto "Python, Java, MongoDB". En este punto, el dato es de tipo String.
    Transformación: Se aplica el método .split(', '). Este es un método nativo de Python para cadenas de texto que divide el String cada vez que encuentra una coma y un espacio.
    Resultado en Python: La variable skills ahora contiene una Lista de Python: ['Python', 'Java', 'MongoDB'].

4. Relación con MongoDB
El flujo de estos datos hacia la base de datos es el siguiente:
    Diccionario de Python: Creas el objeto student que es un Diccionario que contiene campos simples (String) y campos complejos como skills, que ahora es una Lista.
    Conversión a BSON: Cuando ejecutas db.students.insert_one(student), la librería PyMongo toma ese diccionario y lo serializa automáticamente a BSON (formato binario).
    Tipos de datos resultantes:
        El nombre y la ciudad se guardan como BSON String.
        La lista skills se guarda como un BSON Array, permitiendo que MongoDB realice búsquedas eficientes dentro de ese arreglo.
        created_at se guarda como un tipo Date, gracias a que usaste el objeto datetime de Python.

Resumen técnico: request.form['name'] accede a un diccionario interno de la petición donde las llaves son los nombres de los campos del formulario. Al procesar estos datos (como con .split()) antes de insertarlos, aseguras que MongoDB almacene estructuras ricas (como arreglos) en lugar de simples cadenas de texto largas.
_______________________________________________________________________________________________________________

@app.route('/api/v1.0/students/<id>', methods = ['PUT']) 
def update_student (id): 
●  PUT se usa para actualizar recursos existentes 
●  Recibe el ID del estudiante a actualizar 
python 
   query = {"_id":ObjectId(id)} 
●  query: Define qué documento queremos actualizar (el que tenga este _id) 
python 
   name = request.form['name'] 
    country = request.form['country'] 
    city = request.form['city'] 
    skills = request.form['skills'].split(', ') 
    bio = request.form['bio'] 
    birthyear = request.form['birthyear'] 
    created_at = datetime.now() 
●  Obtenemos todos los nuevos valores del formulario 
●  Similar al POST, pero estos datos reemplazarán los existentes 
python 
   student = { 
        'name': name, 
        'country': country, 
        'city': city, 
        'birthyear': birthyear, 
        'skills': skills, 
        'bio': bio, 
        'created_at': created_at 
    } 
●  Creamos un diccionario con los datos actualizados 
python 
   db.students.update_one(query, student) 
    return 
●  update_one(): Actualiza el documento que coincide con el query 
●  Primer argumento: qué documento actualizar (query) 
●  Segundo argumento: con qué datos actualizarlo (student)

_______________________________________________________________________________________________________________
@app.route('/api/v1.0/students/<id>', methods = ['DELETE']) 
def delete_student (id): 
●  DELETE se usa para eliminar recursos 
●  Recibe el ID del estudiante a eliminar 
python 
   db.students.delete_one({"_id":ObjectId(id)}) 
    return 
●  delete_one(): Elimina un documento de la base de datos 
●  {"_id":ObjectId(id)}: Busca el documento con este ID específico y lo elimina