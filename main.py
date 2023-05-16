import os
import markdown

from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Accueil", stylesheet='index.css')

@app.route('/presentation')
def presentation():
    return render_template('presentation.html', title='Présentation', stylesheet='presentation.css')

if __name__ == "__main__":
    app.run(debug=True)