
#💻 Ejercicios: Día 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicios: Nivel 1

#    Encuentre la longitud del conjunto it_companies
print(len(it_companies))

#    Agregar 'Twitter' a it_companies. Añadir un elemento usando add()
it_companies.add('twitter')

#    Inserte varias empresas de TI a la vez en el set it_companies. 
it_companies.update(['Facebook', 'Google', 'Microsoft']) #No produce elementos repetidos
it_companies.update(["Meta", "NVIDIA"])

#    Retire una de las empresas del conjunto it_companies.
if print('Facebook' in it_companies):
    it_companies.remove(it_companies)

it_companies.pop()

#    ¿Cuál es la diferencia entre eliminar y descartar
""" Diferencia entre remove y discard, es que si remove no encuentra el elemento a eliminar devuelve error"""
#remove() --> If the element is not a member, raise a KeyError.
#discard() --> Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
#
#Ejercicios: Nivel 2

#    Únete a A y B. 
    # Unión Este método devuelve un nuevo conjunto
C = A.union(B)
A.update(B)

#    Encuentra una intersección B. La intersección devuelve un conjunto de elementos que están en ambos conjuntos
C = A.intersection(B)

#    Comprobar si es un subconjunto de B.
#Un conjunto puede ser un subconjunto o un súper conjunto de otros conjuntos:
    #-Subset: issubset()
    #-Superset : issuperset
print(A.issubset(B))


#    ¿Son los conjuntos de disjuntas A y B
# Si dos conjuntos no tienen un elemento común o elementos, los llamamos conjuntos de disjuntos. Podemos comprobar si dos conjuntos son de unión o disjunto usando el método isdisjoint().
print(A.isdisjoint(B)) # False

#    Únete a A con B y B con A
A.update(B) # creates new set
B.update(A) # modifies B in-place

#    ¿Cuál es la diferencia simétrica entre A y B
#Devuelve la diferencia simétrica entre dos series. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A)
print(A.symmetric_difference(B))

#    Borrar los conjuntos por completo
#Si queremos eliminar el conjunto en sí utilizamos del operador del
del A, B, it_companies

#Ejercicios: Nivel 3

#    Convertir las edades en un conjunto y comparar la longitud de la lista y el conjunto, ¿cuál es más grande?
#   Al convertir la lista en set, se pierde informacion ya que los conjuentos(set), eliminan duplicados (Lossy Conversion)
age_st = set(age)
print(f"Age set bigger than age list: {len(age_st) > len(age)}")

#    Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
""" 
String (Cadena): Texto inmutable.
List (Lista): Colección ordenada y mutable.
Tuple (Tupla): Colección ordenada e inmutable.
Set (Conjunto): Elementos únicos, desordenados y mutables.

CONCEPTOS USADOS:
Mutable: Puedes cambiar el contenido del objeto en el Heap sin cambiar su dirección de memoria (ID).
Inmutable: Si intentas cambiarlo, Python debe crear un objeto completamente nuevo en una dirección diferente.
Ordenado: La estructura mantiene un índice basado en la posición (Base+Offset).
Único (Set): Utiliza la Tabla Hash para garantizar que no existan duplicados, sacrificando el orden posicional por velocidad de búsqueda.

"""

#   "I am a teacher and I love to inspire and teach people.".
#  ¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y establezca para obtener las palabras únicas.
sentence = "I am a teacher and I love to inspire and teach people."
print(f"Unique words: {len(set(sentence.split()))}")

"""
1. sentence.split() (Creación de Lista)
El método .split() toma el string y lo divide cada vez que encuentra un espacio en blanco.
    Resultado: Crea una lista con todas las palabras: ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.'].
    Estado en memoria: En esta etapa, palabras como "I" y "and" aparecen repetidas (están dos veces cada una).

2. set(...) (Filtrado de Unicidad)
Aquí es donde ocurre la "magia". Al convertir esa lista en un Set (Conjunto), Python aplica la lógica de la Tabla Hash que vimos antes.
    Resultado: El set elimina automáticamente los duplicados.
    Proceso: Cuando el set intenta guardar la segunda "I", ve que ya existe en la tabla hash y la ignora.
    Set final: {'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people.'} (el orden puede variar).

3. len(...) (Conteo)
La función len simplemente cuenta cuántos elementos quedaron en el conjunto final.

4. f"Unique words: {...}" (Interpolación)
Finalmente, el resultado se inserta dentro de la cadena de texto usando un f-string para imprimirlo de forma elegante.

"""