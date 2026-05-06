#💻 Ejercicios: Día 6
#Ejercicios: Nivel 1

#1-Crear una tupla vacía.
empty_tuple = tuple()

#2-Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien).
south_american_tuple = tuple("Argentina", "Brazil", "Uruguay")
north_american_tuple = ("Canada", "Mexico", "Estados Unidos")

#3-Únete a los hermanos y hermanas tuplas y asignalo a los hermanos
american = south_american_tuple + north_american_tuple
#4-¿Cuántos hermanos tienes?
print(len(american))

#5-Modifique la tupla de los hermanos y agregue el nombre de su padre y madre y asignelo a familiares miembros.
american = list[american]
american.append("Panama")
american.append("Paraguay")

#Ejercicios: Nivel 2
#1-Desempaque hermanos y padres de familiares_miembros.
south_american_tuple = american[0:3]
north_american_tuple = american[4:7]

#Desempaque Pais
#El desempaque profesional (Pythonic) utiliza el operador * para capturar múltiples elementos. 
#Como en tu lista los últimos dos elementos son el padre y la madre, lo hacemos así:
*american, american_center1, american_center2 = american

#2-Crear frutas, verduras y productos animales tuplas. Únete a las tres tuplas y asigna a una variable llamada food_stuff_tp.
frutas = tuple("Banana, Manzana")
verduras = tuple("Brocoli", "Espinaca")
animal = tuple("Perro", "Gato")

food_stuff_tp = frutas + verduras + animal

#3-Cambiar el sobre food_stuff_tp tupla a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)

#4-Corta el artículo del medio o los artículos de la lista food_stuff_tp tuple o food_stuff_lt.
food_stuff = food_stuff_lt[0:]

#5-Reduzca los tres primeros elementos y los tres últimos elementos de la lista food_staff_lt
food_stuff = food_stuff_lt[0:3]

#6-Borrar la tupla food_staff_tp completamente
del food_stuff

#7-Compruebe si existe un artículo en tupla:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#    a-Comprueba si 'Estonia' es un país nórdico
boolean_tuple = 'Estonia' in nordic_countries
print(boolean_tuple)

#    b-Comprueba si 'Islandia' es un país nórdico
boolean_tuple = 'Islandia' in nordic_countries
print(boolean_tuple)


