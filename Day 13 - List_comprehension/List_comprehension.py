#💻 Ejercicios: Día 13

#Filtre solo negativo y cero en la lista usando la comprensión de la lista
numbers = [-4,-3,-2,-1,0,2,4,6]

positive_numbers = [i for i in numbers if i >= 0 ]
print(positive_numbers)

#Filtre la siguiente lista de listas de listas a una lista unidimensional :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Usando la comprensión de la lista crear la siguiente lista de tuplas:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
#Aplanar la siguiente lista a una nueva lista:

#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

#Cambie la siguiente lista a una lista de diccionarios:

#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

#Cambie la siguiente lista de listas a una lista de cadenas concatenadas:

#names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

#Escriba una función lambda que pueda resolver una pendiente o y-intercept de funciones lineales.

