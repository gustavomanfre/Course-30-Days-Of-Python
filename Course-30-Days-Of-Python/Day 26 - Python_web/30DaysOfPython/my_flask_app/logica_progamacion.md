#  1️⃣ Primero: entendé el PROBLEMA, no el lenguaje

Leé el enunciado y traducilo a lenguaje humano:

Tengo una lista de edades
Necesito encontrar la edad que más se repite
Y necesito saber cuántas veces se repite
El resultado debe ser un diccionario con esa información

#  3️⃣ Tercero: preguntate qué información falta

Ahora tu mente debe preguntarse:

¿Qué información NO tengo todavía?

Respuesta:

No sé cuántas veces aparece cada número

📌 Entonces el problema real es:

“¿Cómo cuento repeticiones?”

#  4️⃣ Cuarto: pensá como humano, no como código

Imaginá que lo hacés a mano, con lápiz y papel.

Por ejemplo:

Veo 31 → anoto: 31 apareció 1 vez

Veo 26 → anoto: 26 apareció 1 vez

Veo otro 26 → ahora aparece 2 veces

Y así…

📌 Esto ya te revela una estructura mental:

Necesito asociar cada número con un contador

#  5️⃣ Quinto: elegí una herramienta mental (no código)

Ahora preguntate:

¿Qué estructura me permite guardar “valor → cantidad”?

Opciones mentales:

Tabla

Diccionario

Mapa

📌 En Python eso es un dict, pero todavía no escribimos código.

Conceptualmente:

edad → cantidad
26   → 5
27   → 4
32   → 3
...

#  6️⃣ Sexto: separá el problema en fases

Esto es CLAVE.

Fase 1 – Contar

Objetivo mental:

Recorrer la lista y contar cuántas veces aparece cada edad

Resultado intermedio esperado:

{
  31: 2,
  26: 5,
  34: 2,
  ...
}


📌 Esto NO es el resultado final, es un paso intermedio.

Fase 2 – Encontrar el mayor

Ahora preguntate:

De todos los conteos, ¿cuál es el más grande?

Eso implica:

comparar valores

quedarte con el máximo

recordar a qué número pertenece

Fase 3 – Construir el resultado final

Ahora recién:

armás el diccionario pedido

con las claves exactas que pide el ejercicio

7️⃣ Séptimo: evitá el error típico del principiante

❌ Error común:

“Ah, necesito un for, un if, un dict, listo…”

Eso es pensar en código antes de pensar el problema.

✔️ Forma correcta:

problema → pasos → estructura → recién código

8️⃣ Octavo: validá tu lógica con ejemplos chicos

Antes de programar, probá mentalmente:

[1, 2, 2, 3]


¿Qué debería pasar?

Conteo: {1:1, 2:2, 3:1}

Moda: 2

Count: 2

Si tu proceso funciona con esto, funciona con cualquier lista.

9️⃣ Resumen: cómo debe actuar tu mente 🧠

Pensamiento correcto:

¿Qué me piden?

¿Cómo debería verse el resultado?

¿Qué información me falta?

¿Cómo lo haría a mano?

¿Qué estructura mental necesito?

¿Qué pasos tiene el proceso?

Recién ahora escribo código