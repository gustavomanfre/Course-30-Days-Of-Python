from flask import Flask

#Crear la aplicacion Flask
app = Flask (__name__)

#Ruta principal
@app.route('/')
def home():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)

    