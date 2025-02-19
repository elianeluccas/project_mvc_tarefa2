# app/app.py
from flask import Flask
from app.controllers.problema_controller import ProblemaController
from app.controllers.autor_controller import AutorController
from app.controllers.static_controller import StaticController

app = Flask(__name__)

# Rotas
@app.route('/')
def index():
    return StaticController.index()

@app.route('/problema')
def problema():
    return ProblemaController.index()

@app.route('/autor')
def autor():
    return AutorController.index()

if __name__ == "__main__":
    app.run(debug=True)
