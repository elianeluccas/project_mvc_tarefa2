# app/controllers/autor_controller.py
from flask import render_template
from app.models.autor import Autor

class AutorController:
    @staticmethod
    def index():
        # Criar o objeto Autor com um exemplo
        autor = Autor("Nome do Autor", ["Formação 1", "Formação 2"])
        return render_template("autor.html", autor=autor)
