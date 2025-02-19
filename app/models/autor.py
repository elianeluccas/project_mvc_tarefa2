# app/models/autor.py

class Autor:
    def __init__(self, nome, formacoes):
        self.nome = nome
        self.formacoes = formacoes

    def get_nome(self):
        return self.nome

    def get_formacoes(self):
        return self.formacoes

    def get_experiencias(self):
        # Aqui você pode adicionar as experiências, conforme necessário.
        pass
