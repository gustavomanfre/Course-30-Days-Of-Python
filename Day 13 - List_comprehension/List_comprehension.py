#💻 Ejercicios: Día 13

#1- Filtre solo negativo y cero en la lista usando la comprensión de la lista
numbers = [-4,-3,-2,-1,0,2,4,6]

positive_numbers = [i for i in numbers if i >= 0 ]
print(positive_numbers)

#2- Filtre la siguiente lista de listas de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# 3- Comprensión de lista para aplanar los 3 niveles
flattened_list = [number for sublist_externa in list_of_lists for sublist_interna in sublist_externa for number in sublist_interna]

print(flattened_list)
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#4- Usando la comprensión de la lista crear la siguiente lista de tuplas:
numbers = [(i, i**0,i**1,i**2,i**3,i**4, i**5) for i in range(11) ]

numbers = [(i, *(i**j for j in range(6))) for i in range(11)]

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
#5- Aplanar la siguiente lista a una nueva lista:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [[c[0].upper(), c[0][:3].upper(), c[1].upper()] for sub in countries for c in sub]

#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

#6- Cambie la siguiente lista a una lista de diccionarios:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [ dict([c[0],c[1]]) for sub in countries for c in sub]

country_list = [{'country': c[0].upper(), 'city': c[1].upper()} for sub in countries for c in sub]
print(country_list)

#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

#7-Cambie la siguiente lista de listas a una lista de cadenas concatenadas:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [t[0] + " " + t[1] for name in names for t in name]

#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

#8- Escriba una función lambda que pueda resolver una pendiente o y-intercept de funciones lineales.

# Recibe dos tuplas o listas: p1=(x1, y1) y p2=(x2, y2)
calcular_pendiente = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0])

# Ejemplo: puntos (2, 3) y (6, 11)
print(calcular_pendiente((2, 3), (6, 11)))  # Resultado: 2.0