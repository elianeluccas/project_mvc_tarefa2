# app/controllers/problema_controller.py
from flask import render_template
from app.models.problema import Problema

class ProblemaController:
    @staticmethod
    def index():
        # Criar o objeto Problema com um exemplo
        problema = Problema("Enunciado do problema", "Resposta do problema")
        return render_template("problema.html", problema=problema)
