📘 Guía Completa de Sintaxis Jinja2 - Descargable

📋 Índice

Introducción a Jinja2
Variables
Filtros
Estructuras de Control
Herencia de Templates
Macros
Comentarios
Espacios en Blanco
Expresiones y Operadores
Tests (Pruebas)
Asignaciones
Inclusión de Templates
Escapado de HTML
Contexto Global
Ejemplos Prácticos
________________________________________________________________________________________________________________________

# Introducción a Jinja2
Jinja2 es un motor de plantillas moderno y diseñado para Python. Flask lo usa por defecto para generar HTML dinámico.
Tres Tipos de Delimitadores
    {{ ... }}     {# Expresiones - Imprime valores #}
    {% ... %}     {# Declaraciones - Lógica (if, for, etc.) #}
    {# ... #}     {# Comentarios - No aparecen en HTML final #}
________________________________________________________________________________________________________________________
# Variables
Imprimir Variables
{{ variable }}
{{ user.name }}
{{ user['email'] }}
{{ items[0] }}

Ejemplo en Flask

python@app.route('/user')
def user():
    return render_template('user.html', 
                         name='Juan',
                         age=25,
                         email='juan@example.com')
Template:
jinja2<h1>Hola {{ name }}</h1>
<p>Edad: {{ age }}</p>
<p>Email: {{ email }}</p>
Salida HTML:
html<h1>Hola Juan</h1>
<p>Edad: 25</p>
<p>Email: juan@example.com</p>
________________________________________________________________________________________________________________________

# Filtros
Los filtros transforman variables. Se aplican con el pipe |
Filtros Comunes
{{ name|upper }}              {# JUAN #}
{{ name|lower }}              {# juan #}
{{ name|title }}              {# Juan Pérez #}
{{ name|capitalize }}         {# Juan pérez #}

{{ text|length }}             {# Longitud: 15 #}
{{ items|length }}            {# Cantidad de elementos #}

{{ price|round(2) }}          {# Redondea a 2 decimales #}
{{ number|abs }}              {# Valor absoluto #}

{{ text|truncate(20) }}       {# Corta a 20 caracteres... #}
{{ text|wordcount }}          {# Cuenta palabras #}

{{ list|join(', ') }}         {# Une lista: a, b, c #}
{{ list|sort }}               {# Ordena lista #}
{{ list|reverse }}            {# Invierte lista #}

{{ value|default('N/A') }}    {# Valor por defecto si vacío #}
{{ text|safe }}               {# Marca como HTML seguro #}
{{ html|escape }}             {# Escapa caracteres HTML #}

{{ date|date('Y-m-d') }}      {# Formatea fecha: 2025-02-12 #}

Ejemplos de Filtros
jinja2{# Lista de tecnologías #}
{% set techs = ['html', 'css', 'javascript'] %}
{{ techs|join(' | ')|upper }}
{# Salida: HTML | CSS | JAVASCRIPT #}

{# Precio #}
Precio: ${{ 19.999|round(2) }}
{# Salida: Precio: $20.00 #}

{# Texto largo #}
{{ description|truncate(100, True, '...') }}
{# Corta a 100 caracteres con '...' #}
Encadenar Filtros
jinja2{{ name|lower|capitalize }}
{{ list|sort|join(', ') }}
{{ text|striptags|truncate(50) }}
________________________________________________________________________________________________________________________
# Estructuras de Control
If / Elif / Else
{% if user %}
    <h1>Bienvenido {{ user.name }}</h1>
{% endif %}

{% if age >= 18 %}
    <p>Eres mayor de edad</p>
{% else %}
    <p>Eres menor de edad</p>
{% endif %}

{% if role == 'admin' %}
    <a href="/admin">Panel Admin</a>
{% elif role == 'moderator' %}
    <a href="/moderate">Moderar</a>
{% else %}
    <a href="/profile">Mi Perfil</a>
{% endif %}
Operadores en If
jinja2{% if count > 0 %}
{% if name == 'admin' %}
{% if age >= 18 and age <= 65 %}
{% if user or guest %}
{% if not logged_in %}
{% if item in cart %}
{% if email is defined %}
{% if value is none %}

For Loop
jinja2<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
For con Índice
jinja2{% for user in users %}
    {{ loop.index }}: {{ user.name }}
    {# loop.index empieza en 1 #}
{% endfor %}
Variables del Loop
jinja2{% for item in items %}
    {{ loop.index }}      {# Índice actual (desde 1) #}
    {{ loop.index0 }}     {# Índice actual (desde 0) #}
    {{ loop.revindex }}   {# Índice reverso (hasta 1) #}
    {{ loop.revindex0 }}  {# Índice reverso (hasta 0) #}
    {{ loop.first }}      {# True si es el primero #}
    {{ loop.last }}       {# True si es el último #}
    {{ loop.length }}     {# Total de elementos #}
    {{ loop.cycle('odd', 'even') }}  {# Alterna valores #}
{% endfor %}
Ejemplo Práctico de Loop
jinja2<table>
{% for user in users %}
    <tr class="{{ loop.cycle('odd', 'even') }}">
        <td>{{ loop.index }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.email }}</td>
    </tr>
{% endfor %}
</table>
For con Else
jinja2<ul>
{% for user in users %}
    <li>{{ user.name }}</li>
{% else %}
    <li>No hay usuarios</li>
{% endfor %}
</ul>
For con Diccionarios
jinja2{% for key, value in dict.items() %}
    {{ key }}: {{ value }}
{% endfor %}
For con Filtro
jinja2{% for item in items|sort %}
    {{ item }}
{% endfor %}

{% for user in users|selectattr('active') %}
    {{ user.name }}
{% endfor %}

`Importante: En Jinja2, debes cerrar explícitamente los bloques`
________________________________________________________________________________________________________________________

# Herencia de Templates
Template Base (layout.html)

<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block head %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <a href="/">Inicio</a>
            <a href="/about">Acerca de</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        {# Contenido por defecto #}
        {% endblock %}
    </main>
    
    <footer>
        {% block footer %}
        <p>&copy; 2025 Mi Sitio</p>
        {% endblock %}
    </footer>
    
    {% block scripts %}{% endblock %}
</body>
</html>
Template Hijo (home.html)
jinja2{% extends 'layout.html' %}

{% block title %}Inicio - Mi Sitio{% endblock %}

{% block head %}
    <style>
        .special { color: red; }
    </style>
{% endblock %}

{% block content %}
    <h1>Bienvenido a la Página de Inicio</h1>
    <p>Este es el contenido específico de home.</p>
{% endblock %}

{% block scripts %}
    <script src="{{ url_for('static', filename='js/home.js') }}"></script>
{% endblock %}
Super - Heredar Contenido del Padre
jinja2{% extends 'layout.html' %}

{% block footer %}
    {{ super() }}  {# Incluye el footer del padre #}
    <p>Información adicional</p>
{% endblock %}

Macros
Las macros son como funciones reutilizables.
Definir Macro
jinja2{% macro render_input(name, type='text', placeholder='') %}
    <input type="{{ type }}" 
           name="{{ name }}" 
           placeholder="{{ placeholder }}"
           class="form-control">
{% endmacro %}
Usar Macro
jinja2{{ render_input('username', placeholder='Ingresa tu usuario') }}
{{ render_input('email', type='email', placeholder='tu@email.com') }}
{{ render_input('password', type='password') }}
Macro con Argumentos Variables
jinja2{% macro render_field(field, label='') %}
    <div class="form-group">
        {% if label %}
            <label>{{ label }}</label>
        {% endif %}
        {{ field }}
    </div>
{% endmacro %}
Importar Macros de Otro Archivo
macros.html:
jinja2{% macro alert(message, type='info') %}
    <div class="alert alert-{{ type }}">
        {{ message }}
    </div>
{% endmacro %}
En otro template:
jinja2{% from 'macros.html' import alert %}

{{ alert('Operación exitosa', 'success') }}
{{ alert('Error al procesar', 'danger') }}

Comentarios
jinja2{# Este es un comentario #}
{# No aparece en el HTML final #}

{#
    Comentario
    multi-línea
#}

{# TODO: Agregar validación #}

Espacios en Blanco
Controlar Espacios
jinja2{%- if True %}   {# Elimina espacios antes #}
{% if True -%}   {# Elimina espacios después #}
{%- if True -%}  {# Elimina espacios ambos lados #}
Ejemplo
jinja2<ul>
    {%- for item in items %}
    <li>{{ item }}</li>
    {%- endfor %}
</ul>
________________________________________________________________________________________________________________________

# Expresiones y Operadores
Operadores Matemáticos
jinja2{{ 5 + 3 }}       {# 8 #}
{{ 10 - 2 }}      {# 8 #}
{{ 4 * 2 }}       {# 8 #}
{{ 16 / 2 }}      {# 8.0 #}
{{ 17 // 2 }}     {# 8 (división entera) #}
{{ 17 % 2 }}      {# 1 (módulo) #}
{{ 2 ** 3 }}      {# 8 (potencia) #}
Operadores de Comparación
jinja2{{ 5 == 5 }}      {# True #}
{{ 5 != 3 }}      {# True #}
{{ 5 > 3 }}       {# True #}
{{ 5 < 10 }}      {# True #}
{{ 5 >= 5 }}      {# True #}
{{ 3 <= 5 }}      {# True #}
Operadores Lógicos
jinja2{{ True and False }}     {# False #}
{{ True or False }}      {# True #}
{{ not False }}          {# True #}
Concatenación
jinja2{{ 'Hola ' ~ name }}     {# Concatenar strings #}
{{ 'Item ' ~ loop.index }}
________________________________________________________________________________________________________________________

# Tests (Pruebas)
Los tests verifican propiedades de variables con is
Tests Comunes
jinja2{% if variable is defined %}
{% if variable is undefined %}
{% if variable is none %}
{% if variable is number %}
{% if variable is string %}
{% if list is iterable %}
{% if value is even %}    {# Par #}
{% if value is odd %}     {# Impar #}
{% if text is lower %}
{% if text is upper %}
{% if list is sequence %}
Ejemplos de Tests
jinja2{% if user is defined %}
    <p>Usuario: {{ user.name }}</p>
{% else %}
    <p>Usuario no definido</p>
{% endif %}

{% if items %}
    {# items existe y no está vacío #}
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endif %}
Tests Personalizados
jinja2{% if count is divisibleby 3 %}
    <p>Es divisible por 3</p>
{% endif %}

{% if email is match('.*@.*\\..*') %}
    <p>Email válido</p>
{% endif %}

Asignaciones
Set - Asignar Variables
jinja2{% set name = 'Juan' %}
{% set age = 25 %}
{% set total = price * quantity %}

{{ name }} tiene {{ age }} años
Asignación con Bloques
jinja2{% set navigation %}
    <nav>
        <a href="/">Inicio</a>
        <a href="/about">Acerca</a>
    </nav>
{% endset %}

{{ navigation }}
Asignaciones Múltiples
jinja2{% set x, y, z = range(3) %}

Inclusión de Templates
Include - Incluir Parciales
_navbar.html:
jinja2<nav>
    <a href="/">Inicio</a>
    <a href="/blog">Blog</a>
    <a href="/contact">Contacto</a>
</nav>
En tu template:
jinja2{% include '_navbar.html' %}

<main>
    <!-- Contenido -->
</main>

{% include '_footer.html' %}
Include con Variables
jinja2{% include 'card.html' with {'title': 'Título', 'content': 'Texto'} %}
Include Ignorando Faltantes
jinja2{% include 'optional.html' ignore missing %}

Escapado de HTML
Automático (por defecto)
jinja2{{ user_input }}  
{# Automáticamente escapa <script>, <, >, etc. #}
Marcar como Seguro
jinja2{{ html_content|safe }}
{# No escapa, renderiza HTML #}
Forzar Escapado
jinja2{{ unsafe_content|escape }}
{# Fuerza el escapado #}
Bloque de Escape
jinja2{% autoescape true %}
    {{ content }}  {# Se escapa #}
{% endautoescape %}

{% autoescape false %}
    {{ content }}  {# NO se escapa #}
{% endautoescape %}

Contexto Global
Variables Globales en Flask
jinja2{{ request.method }}           {# GET, POST, etc. #}
{{ request.path }}             {# /about #}
{{ request.args.get('id') }}   {# Query parameter #}

{{ session.user_id }}          {# Datos de sesión #}
{{ session.get('cart') }}

{{ config.DEBUG }}             {# Configuración de Flask #}

{{ url_for('home') }}          {# Generar URLs #}
{{ url_for('static', filename='css/style.css') }}

{{ g.user }}                   {# Variable global de request #}

Ejemplos Prácticos
Ejemplo 1: Tabla de Usuarios
Python:
python@app.route('/users')
def users():
    users = [
        {'id': 1, 'name': 'Juan', 'email': 'juan@example.com', 'active': True},
        {'id': 2, 'name': 'María', 'email': 'maria@example.com', 'active': False},
        {'id': 3, 'name': 'Pedro', 'email': 'pedro@example.com', 'active': True},
    ]
    return render_template('users.html', users=users)
Template:
jinja2{% extends 'layout.html' %}

{% block content %}
<h1>Lista de Usuarios</h1>

{% if users %}
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Nombre</th>
            <th>Email</th>
            <th>Estado</th>
        </tr>
    </thead>
    <tbody>
    {% for user in users %}
        <tr class="{{ 'active' if user.active else 'inactive' }}">
            <td>{{ loop.index }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>
                {% if user.active %}
                    <span class="badge success">Activo</span>
                {% else %}
                    <span class="badge danger">Inactivo</span>
                {% endif %}
            </td>
        </tr>
    {% endfor %}
    </tbody>
</table>
{% else %}
    <p>No hay usuarios registrados.</p>
{% endif %}
{% endblock %}

Ejemplo 2: Formulario con Validación
Python:
python@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        errors = []
        if not name:
            errors.append('El nombre es requerido')
        if not email:
            errors.append('El email es requerido')
        if not message:
            errors.append('El mensaje es requerido')
        
        if errors:
            return render_template('contact.html', errors=errors, 
                                 name=name, email=email, message=message)
        
        # Procesar formulario...
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html')
Template:
jinja2{% extends 'layout.html' %}

{% block content %}
<h1>Contacto</h1>

{% if errors %}
<div class="alert alert-danger">
    <ul>
    {% for error in errors %}
        <li>{{ error }}</li>
    {% endfor %}
    </ul>
</div>
{% endif %}

<form method="POST">
    <div class="form-group">
        <label>Nombre:</label>
        <input type="text" name="name" value="{{ name|default('') }}">
    </div>
    
    <div class="form-group">
        <label>Email:</label>
        <input type="email" name="email" value="{{ email|default('') }}">
    </div>
    
    <div class="form-group">
        <label>Mensaje:</label>
        <textarea name="message">{{ message|default('') }}</textarea>
    </div>
    
    <button type="submit">Enviar</button>
</form>
{% endblock %}

Ejemplo 3: Blog con Paginación
Python:
python@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    
    # Simular posts
    all_posts = [{'id': i, 'title': f'Post {i}', 'content': f'Contenido {i}'} 
                 for i in range(1, 51)]
    
    start = (page - 1) * per_page
    end = start + per_page
    posts = all_posts[start:end]
    
    total_pages = len(all_posts) // per_page + (1 if len(all_posts) % per_page else 0)
    
    return render_template('blog.html', 
                         posts=posts, 
                         page=page, 
                         total_pages=total_pages)
Template:
{% extends 'layout.html' %}

{% block content %}
<h1>Blog</h1>

{% for post in posts %}
<article>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content|truncate(100) }}</p>
    <a href="{{ url_for('post_detail', id=post.id) }}">Leer más</a>
</article>
{% endfor %}

<nav class="pagination">
    {% if page > 1 %}
        <a href="{{ url_for('blog', page=page-1) }}">&laquo; Anterior</a>
    {% endif %}
    
    {% for p in range(1, total_pages + 1) %}
        <a href="{{ url_for('blog', page=p) }}" 
           class="{{ 'active' if p == page else '' }}">
            {{ p }}
        </a>
    {% endfor %}
    
    {% if page < total_pages %}
        <a href="{{ url_for('blog', page=page+1) }}">Siguiente &raquo;</a>
    {% endif %}
</nav>
{% endblock %}

Ejemplo 4: Navbar Dinámico
macros.html:
jinja2{% macro nav_link(endpoint, text) %}
    <a href="{{ url_for(endpoint) }}" 
       class="{{ 'active' if request.endpoint == endpoint else '' }}">
        {{ text }}
    </a>
{% endmacro %}
layout.html:
jinja2{% from 'macros.html' import nav_link %}

<nav>
    {{ nav_link('home', 'Inicio') }}
    {{ nav_link('about', 'Acerca de') }}
    {{ nav_link('blog', 'Blog') }}
    {{ nav_link('contact', 'Contacto') }}
</nav>

Referencia Rápida
Sintaxis Básica
SintaxisPropósitoEjemplo{{ }}Imprimir valor{{ name }}{% %}Lógica/Control{% if %}, {% for %}{# #}Comentario{# TODO #}``FiltroisTest{% if x is defined %}
Estructuras de Control
jinja2{% if condition %}...{% endif %}
{% if x %}...{% elif y %}...{% else %}...{% endif %}
{% for item in items %}...{% endfor %}
{% for item in items %}...{% else %}...{% endfor %}
Herencia
jinja2{% extends 'base.html' %}
{% block name %}...{% endblock %}
{{ super() }}
Inclusión
jinja2{% include 'partial.html' %}
{% from 'macros.html' import macro_name %}