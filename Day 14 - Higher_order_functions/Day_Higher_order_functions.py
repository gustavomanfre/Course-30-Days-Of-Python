#💻 Ejercicios: Día 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Ejercicios: Nivel 1

#   Explique la diferencia entre mapa, filtro y reducción.
"""
map():
Transforma cada elemento de un iterable aplicando una función y devuelve un iterable con los resultados.

filter():
Selecciona los elementos de un iterable según una condición (la función devuelve True o False) y devuelve un iterable con los elementos que cumplen dicha condición.
Aplica una condición booleana a cada elemento de un iterable y devuelve solo los que cumplen la condición.

reduce():
Combina los elementos de un iterable paso a paso usando una función y devuelve un único valor.
"""

#   Explique la diferencia entre la función de orden superior, el cierre y el decorador.
"""
1️⃣ Función de orden superior
Definición simple
Una función de orden superior es una función que:
    #recibe otra función como parámetro, y/o
    #devuelve una función como resultado.

#En Python, una función de orden superior aprovecha que las funciones son objetos de primera clase, por lo que pueden ser pasadas, almacenadas y retornadas.
"""
"""
2️⃣ Cierre (Closure)
Definición simple
Un cierre es una función que:
    recuerda variables de su función externa
    incluso después de que esa función externa haya terminado

📌 Definición técnica
Un cierre ocurre cuando una función anidada captura variables libres del entorno léxico envolvente, 
las cuales se almacenan en closure cells asociadas al objeto función.
"""
"""
3️⃣ Decorador
📌 Definición simple
Un decorador es una función que:
    recibe una función
    la envuelve
    devuelve una nueva función con comportamiento adicional
👉 Un decorador usa cierres, pero tiene un propósito específico.

📌 Definición técnica
Un decorador es una función de orden superior que devuelve un cierre, 
el cual intercepta la llamada a la función original para extender o modificar su comportamiento sin alterar su código fuente.

4️⃣ Relación entre los tres conceptos
Función de orden superior
        ↓
     Decorador
        ↓
      Cierre
Todo decorador:
    es función de orden superior
    usa cierres

Pero:
    no toda función de orden superior es decorador
    no todo cierre es decorador
"""

#   Defina una función de llamada antes de mapear, filtrar o reducir, vea ejemplos.
# Ejemplo con map()
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = map(square, numbers)
print(list(result))

# Ejemplo con filter()
numbers = [1, 2, 3, 4, 5]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, numbers)
print(list(result))

# Ejemplo con reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)


#   Utilice para loop para imprimir cada país de la lista de países.
for i in countries:
    print(i)

#   Utilice para imprimir cada nombre en la lista de nombres.
for i in names:
    print(i)

#   Utilice para imprimir cada número en la lista de números.
for i in numbers:
    print(i)

#Ejercicios: Nivel 2

#    Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
print(list(map(lambda x: x.upper(), countries)))

#    Utilice el mapa para crear una nueva lista cambiando cada número a su cuadrado en la lista de números
print(list(map(lambda x: x**2, numbers)))

#    Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
print(list(map(lambda x: x.upper(), names)))

#    Utilice el filtro para filtrar los países que contienen 'land'.
print(list(filter(lambda x: "land" not in x, countries)))

#    Utilice el filtro para filtrar los países que tienen exactamente seis caracteres.
print(list(filter(lambda x: len(x) != 6, countries)))

#    Utilice el filtro para filtrar los países que contienen seis letras y más en la lista de países.
print(list(filter(lambda x: len(x) < 6, countriesV2)))

#    Utilice el filtro para filtrar los países que comienzan con una "E"
print(list(filter(lambda x: x[0] != "E", countries)))

#    Encadena de dos o más iteradores de lista (por ejemplo: arr.map(callback).filter(callback).reduce(callback))
print(list(map(lambda x: x.upper(), list(filter(lambda x: "land" not in x, countries)))))
# Outputs CAPITALIZED countries filtered to be only "land-less"
# Iterator for map == list output from filter!

#ESTE TEMA NO SE HA VISTO.
# Declarar una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
def get_string_lists(lst: list) -> list[str]:
    return list(map(lambda x: str(x), lst))

#    Utilice reducir para sumar todos los números de la lista de números.
print(reduce(lambda a, b: a+b, numbers))

#    Utilice reducir para concatenar todos los países y para producir esta frase: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print(reduce(lambda acc_countries, next_country: f"{acc_countries}, {next_country}" if next_country != countries[-1] else f"{acc_countries}, and {next_country} are north European countries", countries))
#Como funciona, de countries Estonia = acc_countries, Finland = next_country sino es el ultimo elemento next_country != countries[-1], sino solo next_country
"""
Cómo funciona este reduce()
1-Comienza con el primer país (Estonia) como acumulador inicial
    El acumulador (acc_countries) empieza con el primer elemento de la lista.
2-Para cada país siguiente (next_country):
    Si NO es el último país:
        -Se concatena al acumulador usando ", País" (por ejemplo: ", Finlandia", ", Suecia", etc.).
    Si ES el último país:
        Se concatena usando ", and País are north European countries", cerrando la frase completa correctamente.
3-El resultado final:
    El acumulador va creciendo en cada paso.
    Al finalizar la iteración, contiene la frase completa.

Explicación resumida en una sola frase:
reduce() va uniendo los países uno por uno en una sola cadena de texto, usando el acumulador para construir progresivamente la frase final y aplicando un formato especial al último elemento.
"""
#    Declarar una función llamada categorize_countries que devuelve una lista de países con algún patrón común (puede encontrar la lista de países en este repositorio como countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).
from countries import countries as cnt
def get_multiWord_countries(country_list: list[str]) -> list[str]:
    return list(filter(lambda x: " " in x or "-" in x, country_list))

# Wanted to practice list comprehension (Day_13):
def get_multiWord_countriesV2(country_list: list[str]) -> list[str]:
    return [country for country in country_list if " " in country or "-" in country]

#    Crear una función que devuelve un diccionario, donde las teclas se destacan para iniciar letras de países y valores son el número de nombres de países que comienzan con esa letra.
def get_country_letter_N(country_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    list(map(lambda country: result.update({country[0]: result.get(country[0], 0) + 1}), country_list))
    return result

#    Declarar una función get_first_ten_countries - devuelve una lista de los primeros diez países de la lista de countries.js en la carpeta de datos.
def get_first_ten_countries(country_list: list[str]) -> list[str]:
    return country_list[:10]

#    Declarar una función get_last_ten_countries que devuelve los últimos diez países en la lista de países.
def get_last_ten_countries(country_list: list[str]) -> list[str]:
    return country_list[-10:]

#Ejercicios: Nivel 3

#Utilizar el countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) archivar y seguir las siguientes tareas:
from countries_data import countries_data as c_data

#      Ordenar los países por nombre, por capital, por población
def sort_name(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["name"])

def sort_capital(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["capital"])

def sort_population(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["population"], reverse = True)

#Ordenar los diez idiomas más hablados por ubicación.
def sort_10languages(country_dict: list[dict]) -> list[str]:
    lang_counts: dict = {}
    for country in country_dict:
        for language in country.get("languages", []):
            lang_counts[language] = lang_counts.get(language, 0) + 1 # Count language occurrences

    return [lang for lang, n in sorted(lang_counts.items(), key = lambda item: item[1], reverse = True)][:10]
    # lang_counts.items() gives tuple (language, count) pairs
    # sorted() orders these by count (item[1]) (n) descending
    # [lang for lang, n in...] tuple-unpacks just the language names from the tuple pairs (lang, n); n is not used (by convention should be _), but n helps me visualize it as the count of the language

#Resuelve los diez países más poblados.
def sort_population10(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["population"], reverse = True)[:10]
