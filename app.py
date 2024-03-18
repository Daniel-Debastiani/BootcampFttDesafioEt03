from flask import Flask, jsonify, request
from personagem_service import criar_personagem, obter_personagens
from personagem_entity import personagem

app = Flask(__name__)

@app.route('/personagens/criar', methods=['POST'])
def criar_personagem_api():
    data = request.json
    nome = data.get('nome')
    descricao = data.get('descricao')
    imagem = data.get('imagem')
    programa = data.get('programa')
    animador = data.get('animador')

    if nome and descricao and imagem and programa and animador:
        novo_personagem = criar_personagem(nome, descricao, imagem, programa, animador)
        return jsonify({'mensagem': 'Personagem criado com sucesso!', 'personagem': novo_personagem.to_json()}), 201
    else:
        return jsonify({'mensagem': 'Erro: Todos os campos (nome, descricao, imagem, programa, animador) são obrigatórios.'}), 400

@app.route('/personagens/obter', methods=['GET'])
def obter_personagens_api():
    personagens = obter_personagens()
    return jsonify({'personagens': personagens}), 200

if __name__ == '__main__':
    app.run(debug=True)
