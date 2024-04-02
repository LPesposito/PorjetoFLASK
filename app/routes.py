from app import app
from flask import render_template, request, flash, redirect

@app.route("/")
@app.route("/index/")
@app.route("/index/<nome>")
def index(nome="User"):
    return render_template('index.html', nome=nome)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if (usuario,senha) == ('admin','12345'):
        return f'usuario:{usuario} senha:{senha}'
    else: 
        flash("Dados Invalidos!")
        return redirect('/login')