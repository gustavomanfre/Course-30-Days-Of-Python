from flask import Flask, render_template, request, redirect, url_for
import os

#Crear la aplicacion Flask
app = Flask (__name__)
#
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Ruta principal
@app.route('/')
def home():
    # Variables Python que queremos mostrar en HTML
    techs = ['HTML', 'CSS', 'FLASK', 'Python']
    name = '30 Days Of Python Programming'
    # render_template hace:
    # 1. Lee templates/home.html
    # 2. Crea contexto: {'techs': techs, 'name': name, 'title': 'Home'}
    # 3. Procesa Jinja2: reemplaza {{ name }}, ejecuta {% for ... %}
    # 4. Retorna HTML final como string
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/post', methods = ['GET','POST'])

def post():

    name='Text Analizer'
    if request.method == 'GET':
        return render_template('post.html',name=name, title=name)
    
    if request.method =='POST':             # Compara si el atributo method del objeto request(Objeto creado en la consulta del usuario) == 'POST': Compara si el método es POST
                                            # Cuándo es POST: Cuando el Usuario envía el formulario: <button type="submit">Submit</button>
                                            # El navegador hace una solicitud POST con los datos del formulario
        content = request.form['content']   # request.form: Diccionario con los datos del formulario enviado: Contiene pares key: value de los campos del formulario
                                            # ['content']: Accede al campo con name="content" del formulario

        #Analisis de Texto.
        word_count = len(content.split())   # content.split(): Divide el string en una lista de palabras
                                            # content = 'This is a test'
                                            # content.split() # ['This', 'is', 'a', 'test']
                                            # len(...): Cuenta cuántos elementos tiene la lista
        char_count = len(content)           # len(content): Cuenta la cantidad de caracteres en el string
                                            # Incluye: letras, números, espacios, puntuación, saltos de línea
                                            # content = 'Hello World'
                                            # char_count = len(content)  # 11 (incluye el espacio)

        from collections import Counter     # from collections: Del módulo collections (biblioteca estándar de Python), import Counter: Importa la clase Counter
                                            # Clase especializada para contar elementos en una lista
                                            # Hereda de dict
                                            # Cuenta automáticamente cuántas veces aparece cada elemento
                                            # from collections import Counter
                                            # items = ['a', 'b', 'a', 'c', 'a', 'b']
                                            # counter = Counter(items)
                                            # print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})

        words = content.lower().split()     # content.lower(): Convierte todo el texto a minúsculas, Propósito: Tratar 'This' y 'this' como la misma palabra
                                            # .split(): Divide en palabras
                                            # 'this is a test'.split()  # ['this', 'is', 'a', 'test']

        word_freq = Counter(words)          # Counter(words): Crea un objeto Counter contando cada palabra
                                            # word_freq =: Asigna el contador a la variable
                                            # words = ['this', 'is', 'a', 'test', 'this', 'test', 'is', 'simple']
                                            # word_freq = Counter(words)
                                            # print(word_freq) # Counter({'this': 2, 'is': 2, 'test': 2, 'a': 1, 'simple': 1})
                                            # Counter({'this': 2, 'is': 2, 'test': 2, 'a': 1, 'simple': 1})

        most_common = word_freq.most_common(5)# word_freq.most_common(5): Método de Counter
                                              # Retorna las 5 palabras más frecuentes
                                              # Devuelve una lista de tuplas: [(palabra, cantidad), ...]
                                              # Ordenadas de mayor a menor frecuencia # [('this', 2), ('is', 2), ('test', 2), ('a', 1), ('simple', 1)]
                                              # Tipo: list de tuple Cada tupla: (palabra_string, cantidad_int)
                                              
        return render_template('result.html', content=content, word_count=word_count, char_count=char_count, most_common=most_common)
                                              # return render_template('result.html', ...): Renderiza el template de resultados
                                              # Múltiples líneas: Por legibilidad, cada argumento en su propia línea
                                              # content=content:

                                              # Izquierda: Nombre en Jinja2
                                              # Derecha: Valor en Python (el texto original del usuario)
                                              # Tipo: str

                                              # word_count=word_count:
                                              # Cantidad de palabras
                                              # Tipo: int
                                              # Ejemplo: 8


                                              # char_count=char_count:
                                              # Cantidad de caracteres
                                              # Tipo: int
                                              # Ejemplo: 39

                                              # most_common=most_common:
                                              # Lista de palabras más frecuentes
                                              # Tipo: list of tuple
                                              # Ejemplo: [('this', 2), ('test', 2), ('is', 2), ...]
    
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)

