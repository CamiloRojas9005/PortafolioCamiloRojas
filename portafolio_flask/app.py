from flask import Flask, request, jsonify
import json 



app = Flask(__name__)



@app.route('/')
def home():
    return 'este es mi portafoloio Camilo rojas'



@app.route('/about')
def about():
    return 'about' 

@app.route('/projects')
def projects():
    return 'aqui van los proyectos que hago '

@app.route('/contact')
def contact():
    return 'Contacto'

if __name__ == '__main__':
    app.run(debug=True)