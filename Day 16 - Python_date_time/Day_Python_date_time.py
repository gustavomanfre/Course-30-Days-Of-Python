### 💻 Ejercicios: Día 16

#1. Obtenga el día, el mes, el año, la hora, el minuto y la marca de tiempo actuales** desde el módulo de fecha.
from datetime import datetime
now = datetime.now() #Explicación: Llama al método .now() de la clase datetime. Este método consulta el reloj del sistema y guarda un objeto con la fecha y hora exacta del momento actual en la variable now.
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
marca_tiempo = now.timestamp()#Explicación: El Timestamp (o tiempo Unix) es un número que representa los segundos transcurridos desde el 1 de enero de 1970. 
                              #Es muy útil en programación para realizar cálculos matemáticos entre fechas o guardar datos en bases de datos.
#Explicación: Importamos datetime, capturamos el momento exacto con .now() y extraemos cada componente numérico usando sus atributos. El timestamp nos da el total de segundos desde 1970.
print(f"Fecha: {day}/{month}/{year}, Hora: {hour}:{minute}")
print(f"Timestamp: {marca_tiempo}")

#2. Dar formato a la fecha actual** usando este formato: `"%m/%d/%Y, %H:%M:%S"`
formato_especial = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Fecha formateada:", formato_especial)

#Explicación: %m es mes, %d día, %Y año completo. Las comas y espacios dentro de las comillas se mantienen tal cual en el texto resultante.
#El nombre strftime significa "string format time" (formatear objeto tiempo a cadena). 
#Se utiliza para extraer información específica de un objeto datetime y presentarla de forma legible.

#3. Hoy es 5 de diciembre de 2019.** Cambie esta cadena de tiempo a tiempo.
fecha_texto = "5 de diciembre de 2019"
fecha_objeto = datetime.strptime(fecha_texto, "%d %B, %Y")
print("Objeto de fecha:", fecha_objeto)
# Explicación: El patrón "%d %B, %Y" le indica a Python que el texto tiene un día numérico (%d), el nombre del mes completo en inglés (%B), una coma literal y el año (%Y).

#4. Calcule la diferencia de tiempo** entre ahora y el año nuevo.
now = datetime.now()
new_year = datetime(2027,1,1)
diferencia = new_year-now
print(f"Faltan {diferencia.days} días para Año Nuevo.")

#5. Calcule la diferencia de tiempo** entre el 1 de enero de 1970 y ahora.
from datetime import datetime

#Obtenemos la fecha de "ahora"
ahora = datetime.now()

#Creamos la fecha del 1 de enero de 1970
# (Año, Mes, Día)
fecha_unix = datetime(1970, 1, 1)

#Restamos los objetos (Python crea un timedelta automáticamente)
diferencia = ahora - fecha_unix

#Mostramos el resultado
print(f"Han pasado {diferencia.days} días desde el 1 de enero de 1970.")
print(f"En segundos totales: {diferencia.total_seconds()}")

#Explicación de la lógica:
    #datetime(1970, 1, 1): Crea un punto de referencia en el pasado.
    #ahora - fecha_unix: Al restar dos fechas, Python no te da un número simple, te da un objeto timedelta.
    #diferencia.days: Es una propiedad del resultado que te dice únicamente los días completos que han pasado, ignorando las horas sobrantes.

#¿Qué es el Timestamp entonces?
#Si ejecutas now.timestamp(), el número que sale es exactamente la cantidad de segundos que han pasado desde el 1 de enero de 1970 hasta hoy.
# Esto te da el mismo resultado del ejercicio pero directamente en segundos
print(now.timestamp())

# Esto sí funciona: La clase datetime (la plantilla) tiene el método .timestamp(), pero este método necesita un objeto para saber de qué fecha quieres sacar los segundos.
datetime.timestamp(now)

#6. Pi-ense, ¿para qué puede usar el módulo de fecha?** Ejemplos:
#    -Análisis de series temporales
#    -Para obtener una marca de tiempo de cualquier actividad en una aplicación
#    -Añadir publicaciones en un blog

