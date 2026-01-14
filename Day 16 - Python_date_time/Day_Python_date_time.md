Cuando llamas a dir(), Python te devuelve una lista ordenada de strings que contiene los nombres de todos los atributos y métodos válidos de ese objeto. Esto incluye:

    Variables y constantes definidas dentro del objeto.

    Funciones y métodos.

    Métodos mágicos (aquellos que empiezan y terminan con __, como el __call__ que vimos antes).

Con un objeto: dir(objeto) Te muestra todo lo que ese objeto "sabe hacer". Es ideal para cuando estás aprendiendo una librería nueva y no recuerdas cómo se llama un método.
Python

import datetime
print(dir(datetime)) # Te mostrará 'date', 'time', 'timedelta', etc.

Imprime: ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
Uso del módulo Datetime

A continuación se detalla qué hace cada línea del código proporcionado:
Python

from datetime import datetime

Explicación: Importa la clase datetime desde el módulo (librería) llamado datetime. Esto nos permite acceder a todas las herramientas relacionadas con fechas y horas.

now = datetime.now()

Explicación: Llama al método .now() de la clase datetime. Este método consulta el reloj del sistema y guarda un objeto con la fecha y hora exacta del momento actual en la variable now.

print(now) # 2021-07-08 07:34:46.549883

Explicación: Muestra por consola el contenido del objeto now. Por defecto, Python lo imprime en formato ISO (Año-Mes-Día Hora:Minuto:Segundo.Microsegundo).
Python

day = now.day       # 8
month = now.month   # 7
year = now.year     # 2021
hour = now.hour     # 7
minute = now.minute # 38
second = now.second

Explicación: Aquí se accede a los atributos del objeto now. Un atributo es como una "variable interna" del objeto. .day, .month, .year, etc., extraen solo la parte numérica que nos interesa de la fecha completa.
Python

timestamp = now.timestamp()

Explicación: El Timestamp (o tiempo Unix) es un número que representa los segundos transcurridos desde el 1 de enero de 1970. Es muy útil en programación para realizar cálculos matemáticos entre fechas o guardar datos en bases de datos.

print(day, month, year, hour, minute)

Explicación: Imprime los valores que extrajimos anteriormente, separados por espacios.

print('timestamp', timestamp)

Explicación: Imprime la etiqueta de texto 'timestamp' seguida del valor numérico generado por el método .timestamp().


print(f'{day}/{month}/{year}, {hour}:{minute}') # 8/7/2021, 7:38

Explicación: Utiliza una f-string (cadena formateada). Las llaves {} permiten insertar las variables directamente dentro del texto para darle un formato legible (como una fecha de calendario).

Puedes usar la función que aprendimos antes en tu consola de Python: print(dir(now))
_____________________________________________________________________________________________________________________________________________________
Método strftime en Python

El nombre strftime significa "string format time" (formatear objeto tiempo a cadena). 
Se utiliza para extraer información específica de un objeto datetime y presentarla de forma legible.

from datetime import datetime
Línea 1: Importa la clase datetime desde el módulo datetime. Esta clase contiene tanto la fecha como la hora.

# current date and time
now = datetime.now()
Línea 2-3: Creamos un comentario descriptivo y luego almacenamos la fecha y hora exacta del sistema en la variable now.

t = now.strftime("%H:%M:%S")
print("time:", t) # time: 18:21:40
Línea 4-5:
    %H: Representa la hora (00-23).
    %M: Representa los minutos (00-59).
    %S: Representa los segundos (00-59).
Resultado: Crea una cadena de texto con la hora actual separada por dos puntos.

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one) # time one: 06/28/2022, 18:21:40
Línea 6-8:
    %m: Mes del año (01-12).
    %d: Día del mes (01-31).
    %Y: Año completo con cuatro dígitos (ej. 2022).
Resultado: Este es el formato estándar Americano (Mes/Día/Año).

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40

Línea 9-11: Se invierte el orden de %d y %m. 
Resultado: Este es el formato estándar Latino/Europeo (Día/Mes/Año).

Tabla de Códigos Comunes para strftime
Código,Significado,Ejemplo
%d,Día del mes,"01, 15, 31"
%m,Mes numérico,"01, 12"
%b,Nombre del mes abreviado,"Jan, Dec"
%B,Nombre del mes completo,January
%y,Año (dos dígitos),"22, 24"
%Y,Año (cuatro dígitos),"2022, 2026"
%A,Día de la semana completo,Monday

_____________________________________________________________________________________________________________________________________________________
🧩 Explicación: String a Tiempo con strptime

El método strptime (donde la p viene de Parse) se utiliza para analizar una cadena de texto y convertirla en un objeto de fecha que Python pueda entender y manipular.

from datetime import datetime
Explicación: Importa la clase datetime del módulo datetime. Es la herramienta necesaria para crear objetos que contienen año, mes y día.

date_string = "5 December, 2019"
Explicación: Definimos una variable de tipo String (texto plano). 
Para Python, esto es solo una frase; no sabe que el "5" es un día o que "December" es un mes hasta que lo procesamos.

print("date_string =", date_string)     # date_string = 5 December, 2019
Explicación: Simplemente muestra en la consola el texto original que acabamos de definir.

date_object = datetime.strptime(date_string, "%d %B, %Y")
Explicación: Esta es la línea más importante. Analicemos sus partes:

date_string: Es el texto que queremos convertir.
"%d %B, %Y": Es la máscara o patrón. Le dice a Python cómo leer el texto:
    %d: Busca un número (el día).
    %B: Busca el nombre completo del mes en inglés.
    ,: Indica que después del mes hay una coma literal en el texto.
    %Y: Busca un año de cuatro dígitos.
Resultado: Python extrae los datos y crea un objeto de la clase datetime guardado en date_object.

print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00
Explicación: Imprime el objeto recién creado. Notarás que el formato cambia al estándar de Python (AAAA-MM-DD).

Dato clave: Como el texto original no tenía información de la hora, Python asigna por defecto las 00:00:00 (medianoche).

⚠️ ¡Cuidado con el Formato!

Para que strptime funcione, el patrón debe ser idéntico al texto.
    Si el texto es "5 December 2019" (sin coma) y tú pones "%d %B, %Y" (con coma), Python lanzará un error porque no encontrará la coma donde le indicaste.

______________________________________________________________________________________________________________________________________________________________

📅 La clase date en Python

A diferencia de datetime, la clase date se especializa únicamente en el calendario, sin tener en cuenta el reloj.

from datetime import date
    Explicación: Importamos específicamente la clase date desde el módulo datetime. Esto nos permite trabajar con objetos que representan días específicos.

d = date(2020, 1, 1)

    Explicación: Estamos creando manualmente un objeto de fecha.
    El orden es estricto: date(año, mes, día).
    En este caso, estamos guardando en la variable d el primer día del año 2020. No tiene información de horas porque es un objeto de tipo date.

print(d)        # 2020-01-01

    Explicación: Al imprimir el objeto, Python lo muestra por defecto en el formato estándar internacional: AAAA-MM-DD.

print('Current date:', d.today()) 

    Explicación: Aquí ocurre algo curioso. El método .today() es un método de clase.

    ¿Qué hace?: Consulta el calendario del sistema y devuelve la fecha de hoy.

Nota importante: Aunque lo llames desde la variable d (que vale el año 2020), .today() siempre te dará la fecha real de hoy (en este caso, 2026), ignorando el valor que tenía d originalmente.
______________________________________________________________________________________________________________________________________________________________
⏳ Calculando diferencias con timedelta

Mientras que date o datetime representan un "punto" en el calendario, timedelta representa cuánto tiempo ha pasado entre dos puntos.

from datetime import timedelta

    Explicación: Importa la clase timedelta. Esta clase se encarga de normalizar el tiempo (por ejemplo, convertir 60 minutos en 1 hora automáticamente).

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)

    Explicación: Definimos una duración de tiempo llamada t1.

    Internamente, Python suma todo esto y lo guarda de forma simplificada (días, segundos y microsegundos).

    12 semanas + 10 días = 94 días.

t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)

    Explicación: Definimos una segunda duración llamada t2. En este caso, de poco más de una semana.

t3 = t1 - t2

    Explicación: Aquí ocurre la magia del Polimorfismo. Python permite usar el operador matemático de resta (-) entre dos objetos timedelta.

    El algoritmo resta el tiempo total de t2 al de t1 y genera un nuevo objeto timedelta con el resultado.

print("t3 =", t3) # t3 = 86 days, 22:56:50

    Explicación: Muestra el resultado de la resta.

    Nota cómo Python hizo los cálculos complejos por ti: al restar 5 horas a 4 horas, "pidió prestado" un día, resultando en 86 días y 22 horas.

_____________________________________________________________________________________________________________________________________________________________________

Para entender la cuenta que hizo Python, hay que entender que timedelta normaliza todas las unidades (semanas, horas, minutos) a solo tres componentes internos: Días, Segundos y Microsegundos.

Aquí tienes el desglose matemático de la resta entre t1 y t2:
1. Desglose de t1

    Semanas: 12×7=84 días.
    Días adicionales: 10 días.
    Total Días en t1: 84+10=94 días.
    Tiempo en t1: 04 horas, 00 minutos, 20 segundos.

2. Desglose de t2

    Total Días en t2: 7 días.
    Tiempo en t2: 05 horas, 03 minutos, 30 segundos.

3. La Operación: t1 - t2

Python no resta simplemente número por número; lo hace como una resta de tiempo tradicional (donde "pides prestado" a la unidad mayor si es necesario):
Unidad	Operación t1 - t2	Resultado Parcial
Días	94−7	87 días
Segundos	04:00:20−05:03:30	- 01:03:10 (negativo)

4. La Normalización (El paso final)

Como el tiempo (horas/minutos/segundos) quedó negativo (porque le restamos 5 horas a 4), Python hace un ajuste:

    Resta 1 día a los 87 días: Nos quedan 86 días.
    Ese día se convierte en 24 horas para compensar el tiempo negativo.
    La nueva cuenta del tiempo es: 24:00:00 (el día prestado) +04:00:20 (de t1) −05:03:30 (de t2).

Paso a paso del tiempo:

    24:00:00+04:00:20=28:00:20
    28:00:20−05:03:30=22:56:50

Resultado Final:

t3 = 86 days, 22:56:50
💡 Resumen para tus apuntes:

Python aplica el mismo algoritmo que usamos los humanos para restar horas:
    Si los segundos son insuficientes, pide prestado a los minutos.
    Si los minutos son insuficientes, pide prestado a las horas.
    Si las horas son insuficientes (como en este caso), pide prestado 1 día completo (24 horas).
____________________________________________________________________________________________________________________________________________________________

La confusión viene de que datetime es un módulo, una clase y tiene métodos, y Python no lo separa visualmente.

1️⃣ Primero: qué es Datetime realmente

En Python pasa esto: 

    from datetime import datetime

datetime → es una CLASE

En Python:

Llamar a una clase como si fuera una función CREA un objeto, Eso sí está creando un objeto, aunque no lo veas explícito.

    datetime(2027, 1, 1)

2️⃣ Formas correctas de crear un objeto datetime:

✔ Opción 1: fecha y hora actual
datetime.now()

✔ Crea un objeto datetime con la fecha y hora actual
✔ Devuelve un objeto

✔ Opción 2: fecha y hora específica
datetime(2027, 1, 1)
✔ Crea un objeto datetime manualmente
✔ Año, mes, día (hora opcional)

Los objetos datetime representan fecha + hora

Ejemplo de objeto:
2027-01-01 00:00:00

3️⃣ La regla de oro (esto aclara todo)

Primero creás un objeto datetime, después llamás métodos sobre ese objeto

4️⃣ Ahora: timestamp().

❌ Lo que dijiste (incorrecto)
datetime.timestamp(2027,1,1)  # ❌

Esto NO funciona porque:

timestamp() NO crea fechas

Es un método que se aplica a un objeto datetime ya creado

✔ Forma correcta
dt = datetime(2027, 1, 1)
dt.timestamp()

✔ timestamp() convierte un objeto datetime
✔ Devuelve un número (segundos desde 1970)

5️⃣ strftime() y strptime() (muy importante distinguirlos)
🔹 strftime → objeto → string
dt = datetime.now()
dt.strftime("%Y-%m-%d")

Se lee:

“Tomá este objeto datetime y formatealo como texto”

🔹 strptime → string → objeto
datetime.strptime("2027-01-01", "%Y-%m-%d")
Se lee:

“Tomá este texto y convertilo en un objeto datetime”

6️⃣ Por qué se te confunde todo

Hay tres niveles distintos:

Nivel	Qué es
Módulo	datetime
Clase	datetime
Objeto	dt = datetime(...)

Y además: algunos métodos se llaman desde la clase (now, strptime), otros desde el objeto (timestamp, strftime)

7️⃣ Tabla Aclaracion.

Qué quiero hacer	Cómo se hace
Fecha actual	    datetime.now()
Fecha específica	datetime(2027, 1, 1)
A timestamp	        dt.timestamp()
A string	        dt.strftime()
De string a fecha	datetime.strptime()

8️⃣ Forma mental correcta:

    ✅ “datetime crea objetos, los objetos hacen cosas”

9️⃣ Ejemplo completo correcto

from datetime import datetime

dt = datetime(2027, 1, 1)
print(dt)

ts = dt.timestamp()
print(ts)

text = dt.strftime("%Y-%m-%d")
print(text)

dt2 = datetime.strptime("2027-01-01", "%Y-%m-%d")
print(dt2)

🔟 Frase final para estudiar
En Python, datetime es una clase que crea objetos de fecha y hora; los métodos de clase crean objetos y los métodos de instancia transforman esos objetos.

____________________________________________________________________________________________________________________________________________________________




