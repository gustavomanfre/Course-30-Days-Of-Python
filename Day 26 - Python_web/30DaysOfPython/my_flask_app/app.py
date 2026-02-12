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
        




    
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)

