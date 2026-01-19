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

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# ESCRIBE TU CÓDIGO AQUÍ PARA LA CLASE Statistics
# class Statistics:
#     ...

# --- SECCIÓN DE PRUEBAS (Descomentar cuando la clase esté lista) ---
# data = Statistics(ages)

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range()) # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
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
"""

# ESCRIBE TU CÓDIGO AQUÍ PARA LA CLASE PersonAccount
# class PersonAccount:
#     ...