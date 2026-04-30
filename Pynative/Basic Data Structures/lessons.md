EJERCICIO1

# 🧠 1. ¿Por qué separar en variables es mejor?

📌 Principio: Legibilidad del código
Referencia: PEP 20 – The Zen of Python (Tim Peters)

“Readability counts”
“Simple is better than complex”

Tu segunda versión:
first = str1[0]
middle = str1[len(str1) // 2]
last = str1[-1]


👉 Hace explícito qué representa cada cosa.
Tu primera versión:
str1[0]+str1[len_str1 // 2-1]+str1[-1]


👉 Es más compacta, pero:
Mezcla lógica + acceso + cálculo en una sola línea
Cuesta más entender qué hace sin pensar

# 🧠 2. Carga cognitiva (base científica real)

📌 Teoría: Cognitive Load Theory (John Sweller)
El cerebro humano tiene memoria de trabajo limitada.
Cuando escribís:

str1[0]+str1[len_str1 // 2-1]+str1[-1]


👉 El lector tiene que:
Recordar qué es len_str1
Entender // 2 - 1
Entender qué índice representa eso
Interpretar todo junto

En cambio:
middle = str1[len(str1) // 2]


👉 Reduce carga cognitiva porque:
Divide el problema en partes
Usa nombres semánticos
✔ Resultado: menos errores, más comprensión

# 🧠 3. Principio de mantenibilidad
📌 Referencia: Clean Code – Robert C. Martin
“Code should be written for humans, not machines.”
Si mañana cambiás la lógica del “middle”:

Caso 1 (compacto):
str1[0]+str1[len_str1 // 2-1]+str1[-1]


👉 Tenés que modificar dentro de una expresión compleja.
Caso 2 (separado):
middle = ...

👉 Cambiás una sola línea, aislada.
✔ Menos riesgo de romper algo.

# 🧠 4. Principio de Single Responsibility (adaptado a código simple)
Cada línea debería hacer una cosa clara.
Tu código compacto:
Calcula índice
Accede
Concatena

Todo junto.

Tu código separado:
Cada línea hace una cosa

✔ Esto mejora:
Debugging
Testing
Reutilización

# 🧠 5. ¿Y la memoria / performance?

Acá viene lo importante:
👉 Tu argumento de memoria no aplica en este contexto.
Variables como first, middle, last son referencias a objetos existentes
Python ya maneja esto internamente (referencias, no copias profundas)
📌 Referencia:
Python Data Model (documentación oficial)
Fluent Python – Luciano Ramalho

👉 Crear esas variables:
No duplica el string
No genera overhead significativo
⚖️ Entonces, ¿cuál es realmente “mejor”?
❌ Tu versión compacta es peor porque:
Mayor carga cognitiva
Más difícil de leer
Más propensa a errores
Menos mantenible

✅ La versión con variables es mejor porque:
Más clara semánticamente
Más fácil de modificar
Más alineada con estándares profesionales
🚀 Pero ojo (nivel avanzado)

En código real, tampoco querés exagerar.
Esto también sería válido y limpio:
print(str1[0] + str1[len(str1)//2] + str1[-1])


✔ Porque:
Es corto
Sigue siendo legible
No tiene lógica innecesaria
🧠 Conclusión fuerte (nivel ingeniería)

No estás optimizando lo que importa.

👉 En software profesional:
❌ No optimizás micro-memoria en variables
✅ Optimizás comprensión, mantenimiento y errores humanos

Porque:
👉 El mayor costo en software no es CPU → es el humano.
_________________________________________________________________________________________________________________________________

La regla general para encontrar el medio
El principio es este: el índice del medio es la posición donde la cadena izquierda y derecha quedan equilibradas.
len par:    "Ault"   → len=4 → medio = 4//2 = 2  → "Au" | "lt"
len impar:  "Aulxt"  → len=5 → medio = 5//2 = 2  → "Au" | "xt"
La regla es simplemente len(s1) // 2, sin el -1. La división entera siempre te da el punto de corte correcto en ambos casos:

Por qué //2 siempre funciona
Con longitud par //2 te da exactamente la mitad. Con longitud impar //2 redondea hacia abajo, dejando un carácter más en la mitad derecha que en la izquierda, lo cual es el comportamiento estándar y esperado. No necesitás ningún ajuste con -1 ni +1.
El -1 que usaste en tu código era innecesario y fue la raíz del error.

_________________________________________________________________________________________________________________________________

Ejercicio 9

🧠 1. Error: mala asignación de variables
❌ Antes
s1 = "ynf", s2 = "PyNative"

✅ Después
s1 = "ynf"
s2 = "PyNative"

🔍 Problema

Eso creaba una tupla, no dos variables:

("ynf", "PyNative")

📚 Fundamentación
📖 Fluent Python

Explica que:

Las comas, no los paréntesis, crean tuplas.

👉 Error conceptual de sintaxis.

🎯 Justificación
Estabas rompiendo el modelo de datos
El código no representaba lo que pensabas
🧠 2. Error: incremento que no hace nada
❌ Antes
is_contain+1

✅ Después
is_contain += 1

🔍 Problema
No había asignación
No modificaba el valor
📚 Fundamentación
📖 Clean Code

Principio:

El código debe hacer explícitamente lo que el programador intenta.

👉 Una operación sin efecto = código engañoso

🎯 Justificación
Código sin efecto = bug silencioso
Difícil de detectar en sistemas grandes
🧠 3. Error: usar contador en problema booleano
❌ Antes
is_contain = 0
...
is_contain += 1
print(bool(is_contain))

✅ Después
is_contain = True
...
is_contain = False

🔍 Problema

Estabas usando:

contador
bandera
resultado final

👉 todo en una sola variable

📚 Fundamentación
📖 Clean Code

Principio:

Una variable debe tener una única responsabilidad.

📖 Refactoring

Principio:

Replace temp with query / Clarify intent

👉 Si una variable cumple múltiples roles → hay que simplificar

🎯 Justificación
Mezcla de responsabilidades → bugs
Código menos legible
Difícil de mantener
🧠 4. Error: lógica basada en cantidad y no en condición
❌ Antes
if i in s2:
    is_contain += 1

✅ Después
if i not in s2:
    is_contain = False
    break

🔍 Problema

El ejercicio pide:

todos los elementos cumplen


Pero vos resolvías:

cuántos cumplen

📚 Fundamentación
📖 Fluent Python

Capítulo de sets:

Membership testing (in) es una operación booleana, no de conteo.

📖 Clean Code

Principio:

Usa el nivel de abstracción correcto

👉 No contar cuando solo necesitás validar

🎯 Justificación
Menos lógica = menos errores
Más alineado con el problema real
🧠 5. Mejora: usar not in en lugar de lógica positiva
❌ Antes
if i in s2:
    is_contain = True
else:
    is_contain = False

✅ Después
if i not in s2:
    is_contain = False
    break

📚 Fundamentación
📖 Clean Code

Principio:

Evitar lógica innecesaria

📖 PEP 8

Recomienda:

Código simple y directo sobre estructuras redundantes

🎯 Justificación
Eliminaste código innecesario
Mejor legibilidad
Menos ramas lógicas
🧠 6. Mejora: uso de break
✅ Código final
if i not in s2:
    is_contain = False
    break

📚 Fundamentación
📖 Fluent Python

Concepto:

Cortar iteraciones innecesarias mejora eficiencia

🎯 Justificación
Evita trabajo innecesario
Optimización temprana correcta (sin sobrecomplicar)
🧠 7. Mejora: normalización con .lower()
s1 = s1.lower()
s2 = s2.lower()

📚 Fundamentación
📖 Fluent Python

Capítulo strings:

Comparaciones deben considerar normalización cuando el dominio lo requiere.

🎯 Justificación
Evita errores por case sensitivity
Hace el programa más robusto
🧠 CONCLUSIÓN GLOBAL

Pasaste de:

❌ Código:

ambiguo
con múltiples responsabilidades
propenso a errores

👉 A:

✅ Código:

claro
booleano puro
alineado con el problema
eficiente

_________________________________________________________________________________________________________________________________

Crítica del Ejercicio 10

✅ Lo que está bien
Antes de criticar, lo que hiciste bien:

Separás correctamente la lógica (lowercase → contar)
Usás str.count() en lugar de comparar char por char, que es más Pythónico
El código funciona y es legible


🔴 Problema 1: Mutás la variable original
pythonstr1 = "Hello World"
str1 = str1.lower()   # ← pisás el dato original
Referencia → A Philosophy of Software Design (Ousterhout, Cap. 2 — Complexity)
Ousterhout habla de que la complejidad emerge cuando las variables tienen múltiples roles a lo largo del código. Acá str1 empieza siendo el dato original y después se convierte en una versión procesada del mismo — son dos cosas distintas metidas en el mismo nombre.
Corrección:
pythonstr1 = "Hello World"
str1_lower = str1.lower()   # dato procesado, nombre que lo dice
O directamente inline si no necesitás str1 después:
pythoncount_vowels += str1.lower().count(i)

🔴 Problema 2: El for itera sobre vocales cuando debería iterar sobre la cadena
pythonfor i in 'aeiou':
    count_vowels += str1.count(i)
Esto funciona, pero conceptualmente está al revés. El problema dice "contar vocales en una cadena", lo que naturalmente se lee como: "recorré la cadena y fijate si cada carácter es vocal". Vos estás recorriendo las vocales y preguntando cuántas veces aparece cada una en la cadena.
Referencia → The Pragmatic Programmer (Hunt & Thomas, Tip 12 — "Use the Power of Command Shells")
Más relevante acá es el Tip general del libro: "Express yourself clearly". El código debe comunicar intención. Un lector que lee for i in 'aeiou' tarda un segundo extra en entender qué estás haciendo.
Referencia → Fluent Python (Ramalho, Cap. 2 — Sequences)
Ramalho muestra que para este tipo de conteo sobre una secuencia, una generator expression con sum() es la forma Pythónica idiomática:
pythoncount_vowels = sum(1 for char in str1 if char in 'aeiou')
Esto se lee casi como español: "sumá 1 por cada char en str1 que esté en las vocales". La dirección del recorrido es la natural.

🟡 Problema 3: Nombre de variable genérico i
pythonfor i in 'aeiou':
Referencia → PEP 8 + Google Python Style Guide
PEP 8 acepta i como índice numérico en rangos (for i in range(n)), pero cuando iterás sobre caracteres, el nombre debe reflejar qué es:
pythonfor vowel in 'aeiou':
    count_vowels += str1.count(vowel)
Google Style Guide agrega: los nombres de variables de loop deben ser descriptivos a menos que el scope sea trivialmente corto (tipo 2 líneas de matemática).

🟡 Problema 4: Mensaje de salida inconsistente con el enunciado
pythonprint('vowel count:', count_vowels)   # minúscula
# Salida Esperada: Vowel Count: 3     # mayúscula
Detalle menor, pero Refactoring (Fowler) y el Pragmatic Programmer coinciden: si hay una spec (aunque sea en un comentario), el output debe matchearla exactamente. En contexto laboral esto es un bug.

✅ Versión final corregida
python# Ejercicio 10. Contador de vocales
str1 = "Hello World"

count_vowels = sum(1 for char in str1.lower() if char in 'aeiou')

print('Vowel Count:', count_vowels)
Tres líneas, legible, sin mutación de variable, dirección de iteración natural, nombre descriptivo. La generator expression es exactamente el tipo de construcción que Ramalho promueve en el Cap. 2 de Fluent Python como forma idiomática de procesar secuencias en Python.
_________________________________________________________________________________________________________________________________