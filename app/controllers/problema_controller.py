from flask import Blueprint, render_template, request
from app.models.problema import Problema

problema_bp = Blueprint('problema', __name__)

@problema_bp.route('/problema')
def mostrar_enunciado():
    return render_template('problema/enunciado.html')

@problema_bp.route('/problema/resolver', methods=['POST'])
def resolver_problema():
    entrada = request.form.get('entrada')
    problema = Problema("Exemplo de problema")
    resposta = problema.resolver(entrada)
    return render_template('problema/resposta.html', resposta=resposta)
