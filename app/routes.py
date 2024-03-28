from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('homePage.html', nome='Romero')

@app.route('/contato')
def contato():
    return render_template('contato.html')