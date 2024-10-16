from flask import Flask, request, jsonify, render_template
import json 



app = Flask(__name__)



@app.route('/home')
def home():
    # return 'este es mi portafoloio Camilo rojas'
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)