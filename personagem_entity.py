import json

class personagem:
    def __init__(self, nome, descricao, imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

    def to_json(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "imagem": self.imagem,
            "programa": self.programa,
            "animador": self.animador
        }
