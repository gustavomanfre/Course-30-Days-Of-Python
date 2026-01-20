# ==========================================
# 💻 Ejercicios: Día 21
# ==========================================

# ------------------------------------------
# Ejercicios: Nivel 1
# ------------------------------------------
"""
Python tiene el módulo llamado estadísticas y podemos usar 
este módulo para hacer todos los cálculos estadísticos. Sin embargo, 
para aprender a hacer la función y reutilizar la función, tratemos de 
desarrollar un programa, que calcula la medida de la tendencia central 
de una muestra (media, mediana, modo) y la medida de la variabilidad 
(intervalo, varianza, desviación estándar). 

Además de esas medidas, encuentre la distribución mínima, max, de recuento, 
percentil y de frecuencia de la muestra. 

Puede crear una clase llamada Statistics y crear todas las funciones 
que realizan cálculos estadísticos como métodos para la clase Estadística. 
Compruebe la salida a continuación.
"""

# ESCRIBE TU CÓDIGO AQUÍ PARA LA CLASE Statistics
class Statistics:

    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)
    
    def sum (self):
        return sum(self.ages)
    
    def min (self):
        return min(self.ages)
    
    def max (self):
        return max(self.ages)
    
    def range (self):
        return self.max()- self.min()
    
    # FORMA ANTIGUA
    # Medidas de Tendencia Central (El centro de los datos)
    # def calcular_media(self):
    # Es la suma de todos los números dividida por la cantidad de números.
        # sum_nro = 0
        # for age in self.ages:
        #   sum_nro += age

    def mean(self):
    # Es la suma de todos los números dividida por la cantidad de números.
        return self.sum()/self.count()

    def median(self):
        # Mediana (Median)Es el valor que queda justo en el centro cuando ordenas los datos de menor a mayor.
        ord_ages = sorted(self.ages) #Ordenamos la funcion.
        n = self.count()
        mitad = n // 2
        if n % 2 == 0:
            # Caso Par: Promedio con / para no perder decimales
            return (ord_ages[mitad] + ord_ages[mitad - 1]) / 2
        else:
            # Caso Impar: El centro exacto
            return ord_ages[mitad]
    
    #def mode(self):
        #reps_ages = {}
        #for edad in self.ages:
            #if edad in reps_ages:
                #reps_ages [edad]+=1
            #else:
                #reps_ages [edad]= 1
        # Se puede realizar con Counter: Es la más profesional para producción.

        #dict_frecuency = {}
        #max_key = 0
        #max_value = 0
        #for key, value in reps_ages.items():
            #if value > max_value:
                #max_value = value
                #max_key = key
        #dict_frecuency["mode"] = max_key
        #dict_frecuency["count"] = max_value

        #return dict_frecuency


    def mode(self):

        reps_ages = {}
        for edad in self.ages:
            reps_ages[edad] = reps_ages.get(edad, 0) + 1

        max_key = max(reps_ages, key=reps_ages.get)
        max_value = reps_ages[max_key]
        return {max_key: max_value}
    def var(self):
        # La varianza es el promedio de las diferencias al cuadrado respecto a la media
        mu = self.mean()
        # Usamos una lista de comprensión para elevar al cuadrado cada diferencia
        squared_diffs = [(x - mu) ** 2 for x in self.ages]
        # Retornamos la suma de diferencias dividida el total (usando los métodos que ya creaste)
        variance = sum(squared_diffs) / self.count()
        return round(variance, 1)

    def std(self):
        # La desviación estándar es simplemente la raíz cuadrada de la varianza
        import math
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        # 1. Contamos frecuencias (Reutilizamos tu lógica de dict)
        reps = {}
        for edad in self.ages:
            reps[edad] = reps.get(edad, 0) + 1
        
        # 2. Creamos la lista de tuplas (porcentaje, edad)
        total = self.count()
        dist = []
        for edad, conteo in reps.items():
            porcentaje = (conteo / total) * 100
            dist.append((porcentaje, edad))
        
        # 3. Ordenamos de mayor a menor frecuencia (usando el porcentaje en la posición 0)
        dist.sort(reverse=True)
        return dist

    def describe(self):
        # Este método simplemente imprime el resumen de todos tus cálculos
        return (f"Count: {self.count()}\n"
                f"Sum: {self.sum()}\n"
                f"Min: {self.min()}\n"
                f"Max: {self.max()}\n"
                f"Range: {self.range()}\n"
                f"Mean: {self.mean()}\n"
                f"Median: {self.median()}\n"
                f"Mode: ({self.mode()['mode']}, {self.mode()['count']})\n"
                f"Variance: {self.var()}\n"
                f"Standard Deviation: {self.std()}\n"
                f"Frequency Distribution: {self.freq_dist()}")        

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# --- SECCIÓN DE PRUEBAS (Descomentar cuando la clase esté lista) ---
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) 
# # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# print(data.describe())
# Salida esperada de describe():
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# ------------------------------------------
# Ejercicios: Nivel 2
# ------------------------------------------
"""
Crear una clase llamada PersonAccount. 
Tiene nombre, apellidos, ingresos, propiedades de gastos y tiene métodos:
- total_income
- total_expense
- account_info
- add_income
- add_expense
- account_balance

Los ingresos son un conjunto de ingresos y su descripción. 
Lo mismo ocurre con los gastos.

Para cumplir con la parte de "montos y descripción", 
lo más eficiente en Python es que incomes y expenses sean listas de diccionarios.
"""

# ESCRIBE TU CÓDIGO AQUÍ PARA LA CLASE PersonAccount

class PersonAccount:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        # Estructura : [{'amount': 1000, 'description': 'Salario'}]
        self.ingresos = [] 
        self.gastos = []

    #Ingreso Totales
    def total_income (self):
        return sum(self.ingresos)
    
    #Gastos Totales
    def total_expense (self):
        return sum(self.gastos)

    #Informacion de la cuenta
    def add_income (self, ingreso, descripcion):
        self.ingresos.append({"ingreso":ingreso, "descripcion": descripcion})

    #Añadir Gastos
    def add_expense (self, gasto,descripcion):
        self.gastos.append({"gasto":gasto, "descripcion": descripcion})

    #Saldo cuenta
    def account_balance (self):
        return self.total_income()- self.total_expense()

        