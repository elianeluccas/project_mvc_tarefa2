# app/models/problema.py

class Problema:
    def __init__(self, enunciado, resposta):
        self.enunciado = enunciado
        self.resposta = resposta

    def get_enunciado(self):
        return self.enunciado

    def get_resposta(self):
        return self.resposta
