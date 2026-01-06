#💻 Ejercicios: Día 8

# 1-Crear un diccionario vacío llamado perro.
perro = {}

#2-Añadir nombre, color, raza, piernas, edad al diccionario del perro.
perro['nombre', 'color', 'raza', 'piernas', 'edad'] =  'Bracko', 'Mixto', 'San Bernardo', 'Largas', 12

#3-Crear un diccionario de estudiantes y añadir first_name, last_name, gender, age, marital status, skills, country, city y address como claves para el diccionario
estudiantes = {}
estudiantes['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'addres'] = 'Lionel', 'Messi', 'Masculino', 36, 'Casado', ['Regate', 'Tiro Libre'], 'Argentina','Rosario','Valle de las Leñas'

#4-Obtenga la longitud del diccionario de estudiantes
print(estudiantes)

#5-Obtenga el valor de las habilidades y verifique el tipo de datos, debería ser una lista.
print(type(estudiantes['skills']))


#6-Modificar los valores de las habilidades añadiendo una o dos habilidades.
estudiantes['skills'][0][1]= 'izquierdo','Pelota Parada'

#7-Obtenga las teclas del diccionario como una lista.
estudiantes_list = estudiantes.keys()

#8-Obtener los valores del diccionario como una lista.
estudiantes_list = estudiantes.values()

#9-Cambiar el diccionario a una lista de tuplas usando el método items().
estudiantes_list = estudiantes.items()

#10-Borrar uno de los elementos del diccionario.
print(estudiantes.clear())

#11-Borrar uno de los diccionarios.
del estudiantes

