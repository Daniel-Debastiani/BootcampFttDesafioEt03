from personagem_entity import personagem

lista_personagens = []

def criar_personagem(nome, descricao, imagem, programa, animador):        
    novo_personagem = personagem(nome, descricao, imagem, programa, animador)
    lista_personagens.append(novo_personagem)
    return novo_personagem

def obter_personagens():
    if lista_personagens:
        # Converte cada objeto personagem em um dicionário
        personagens_serializaveis = []
        for p in lista_personagens:
            personagem_dict = {
                'nome': p.nome,
                'descricao': p.descricao,
                'imagem': p.imagem,
                'programa': p.programa,
                'animador': p.animador
            }
            personagens_serializaveis.append(personagem_dict)
        return personagens_serializaveis
    print("\nNENHUM PERSONAGEM REGISTRADO!")
    return "Nenhum Personagem Registrado!"