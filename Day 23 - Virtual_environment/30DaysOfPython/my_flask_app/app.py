from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return '''
    <h1>¡Mi Primera Aplicación Flask!</h1>
    <p>El entorno virtual está funcionando correctamente.</p>
    <p>Flask versión: 3.0.0</p>
    '''

# Ruta adicional
@app.route('/hola/<nombre>')
def hola(nombre):
    return f'<h2>¡Hola, {nombre}! Bienvenido a mi app Flask.</h2>'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)