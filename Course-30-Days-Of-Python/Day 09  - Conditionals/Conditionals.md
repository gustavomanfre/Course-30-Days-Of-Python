# Ver Teoria:

[https://github.com/Asabeneh/30-Days-Of-Python/blob/master/10_Day_Loops/10_loops.md]

_____________________________________________________________________________________________________________________________________________________________________________________________

# Hacks para resolucion.
**La Lógica del Medio: Explicación Completa**

# El Concepto del "Salto" en sequence.

Cuando las computadoras acceden a posiciones en una lista, no cuentan "primera, segunda, tercera posición" como los humanos. 
En cambio, piensan en **cuántos saltos necesitan dar desde el inicio**.

    - Si quieres el primer elemento, das cero saltos. 
    - Si quieres el segundo, das un salto. Si quieres el tercero, das dos saltos.

Por Qué Restamos Uno

Cuando tienes una lista de cinco elementos, para los humanos el del medio es el tercero. 
Pero en términos de saltos, necesitas dar dos saltos para llegar ahí. 
Entonces, el "número del medio" en lenguaje humano (tres) necesita convertirse en "número de saltos" (dos). Por eso restamos uno.


# La División Entera: El Truco Matemático

Aquí viene lo genial: cuando divides la cantidad total de elementos menos uno entre dos, automáticamente obtienes el número de saltos correctos:

    Si la lista es impar, la división te da exactamente el centro perfecto
    Si la lista es par, la división redondea hacia abajo, dándote el primer elemento de los dos centrales

# El Redondeo Automático

La división entera siempre redondea hacia abajo, descartando decimales. Esto es perfecto porque necesitamos un número entero de saltos, y queremos el elemento ligeramente a la izquierda cuando hay dos posibles centros.

# Conclusión

No necesitas preguntarte si la lista es par o impar. La fórmula "longitud menos uno, dividido entre dos" ya incorpora ambas lógicas: la conversión de posición humana a saltos de computadora, y el redondeo hacia el equilibrio cuando no hay un centro exacto.

Seria como los indices se manejan en salto para llegar a una pocision entonces para llegar al medio seria el numero del medio menos uno que coinice con la division entera que es menos -1 o redondeado hacia abajo.

['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    0             1       2         3          4     = 4 // 2 = 2
                        Muestra                                    

['JavaScript', 'React', 'Node', 'MongoDB']
    0           1       2         3                  =  3 // 2 = 1

_____________________________________________________________________________________________________________________________________________________________________________________________