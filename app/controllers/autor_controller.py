from flask import Blueprint, render_template

autor_bp = Blueprint('autor', __name__)

@autor_bp.route('/autor')
def mostrar_autor():
    return render_template('autor/nome.html', nome="Seu Nome")

@autor_bp.route('/autor/formacoes')
def mostrar_formacoes():
    formacoes = ["Graduação em X", "Mestrado em Y"]
    return render_template('autor/formacoes.html', formacoes=formacoes)

@autor_bp.route('/autor/experiencias')
def mostrar_experiencias():
    experiencias = ["Empresa A", "Projeto B"]
    return render_template('autor/experiencias.html', experiencias=experiencias)
